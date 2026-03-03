# GrayArea — Story-as-Code Architecture

Stack: **TypeScript · Next.js · Expo · Supabase · OpenAI API · MCP**
Monorepo: **Nx** (`@nx/next` · `@nx/expo` · `@nx/node`)
Scripts: **bash · Python · Node.js · ts-node** — no PowerShell (cross-platform: Windows/Mac/Linux)

---

## Layer Map

```
┌──────────────────────────────────────────────────────────────┐
│  Next.js (web)               Expo (mobile)                   │
│  Story management            Reading companion               │
│  Chapter editor              Quick notes / lookup            │
│  Canon dashboard             Offline cache                   │
│  AI writing assistant        AI canon checker                │
└───────────┬────────────────────────┬─────────────────────────┘
            │    TypeScript SDK      │
            ▼                        ▼
     ┌─────────────────────────────────────┐
     │              Supabase               │
     │  Postgres + JSONB  (topics, canon,  │  ← primary store
     │  characters, chapters, timeline)    │
     │  Storage (raw .txt, exports)        │  ← blob store
     │  pgvector extension                 │  ← semantic search
     └──────────────┬──────────────────────┘
                    │
     ┌──────────────┴──────────────┐
     │         AI Layer            │
     │                             │
     │  OpenAI API                 │  ← GPT-4o (writing, QA)
     │    embeddings → pgvector    │  ← semantic topic search
     │    structured output        │  ← canon extraction
     │    function calling         │  ← story tools
     │                             │
     │  MCP Server (GrayArea)      │  ← stdio or HTTP
     │    resources: topics,       │
     │    canon, characters        │
     │    tools: check_canon,      │
     │    search_topics, etc.      │
     └─────────────────────────────┘
            ▲
     ┌──────┴──────┐
     │ AsyncStorage│  ← Expo only, offline cache
     │  (MMKV)     │     current chapter, canon snapshot
     └─────────────┘
```

---

## Supabase Schema

```sql
-- The 83 discussion topics (source material, imported once)
create table topics (
  id           serial primary key,
  number       integer      not null,
  slug         text         not null unique,
  title        text         not null,
  content      text         not null,        -- verbatim Markdown
  tags         text[]       default '{}',
  metadata     jsonb        default '{}',
  created_at   timestamptz  default now()
);

-- Characters
create table characters (
  id           uuid         primary key default gen_random_uuid(),
  name         text         not null,
  aliases      text[]       default '{}',
  description  text,
  arc          text,
  metadata     jsonb        default '{}'     -- hosts, timeline refs, etc.
);

-- Timeline events (Daneel-centric or world)
create table timeline_events (
  id           uuid         primary key default gen_random_uuid(),
  year_offset  integer,                       -- years after X20
  absolute_year integer,
  label        text         not null,
  description  text,
  characters   uuid[]       default '{}',
  location     text,
  event_type   text,                          -- 'host-transfer','world','foundation','x20-echo'
  metadata     jsonb        default '{}'
);

-- Canon decisions (single locked source of truth)
create table canon (
  id           uuid         primary key default gen_random_uuid(),
  key          text         not null unique,  -- e.g. 'daneel.origin', 'x20.year'
  value        jsonb        not null,
  note         text,
  locked       boolean      default false,
  updated_at   timestamptz  default now()
);

-- Book chapters (the actual writing)
create table chapters (
  id           uuid         primary key default gen_random_uuid(),
  book         integer      not null default 1,
  number       integer      not null,
  title        text         not null,
  content      text         not null,        -- Markdown prose
  word_count   integer      generated always as (
                 array_length(regexp_split_to_array(trim(content), '\s+'), 1)
               ) stored,
  status       text         default 'outline',  -- outline|draft|revised|final
  topic_refs   integer[]    default '{}',    -- which topic numbers informed this chapter
  version      integer      default 1,
  created_at   timestamptz  default now(),
  updated_at   timestamptz  default now(),
  unique (book, number)
);

-- Chapter version history (simple)
create table chapter_versions (
  id           uuid         primary key default gen_random_uuid(),
  chapter_id   uuid         references chapters(id) on delete cascade,
  version      integer      not null,
  content      text         not null,
  note         text,
  created_at   timestamptz  default now()
);
```

---

## TypeScript Interfaces

```typescript
// types/story.ts

export type ChapterStatus = 'outline' | 'draft' | 'revised' | 'final'
export type EventType = 'host-transfer' | 'world' | 'foundation' | 'x20-echo' | 'personal'

export interface Topic {
  id: number
  number: number
  slug: string
  title: string
  content: string
  tags: string[]
  metadata: Record<string, unknown>
  createdAt: string
}

export interface Character {
  id: string
  name: string
  aliases: string[]
  description: string | null
  arc: string | null
  metadata: {
    hosts?: string[]
    substrate?: string
    firstAppearance?: number
    [key: string]: unknown
  }
}

export interface TimelineEvent {
  id: string
  yearOffset: number | null     // years after X20
  absoluteYear: number | null
  label: string
  description: string | null
  characters: string[]          // character UUIDs
  location: string | null
  eventType: EventType
  metadata: Record<string, unknown>
}

export interface CanonEntry {
  id: string
  key: string                   // dot-notated: 'daneel.origin', 'x20.year'
  value: unknown
  note: string | null
  locked: boolean
  updatedAt: string
}

export interface Chapter {
  id: string
  book: number
  number: number
  title: string
  content: string               // Markdown
  wordCount: number
  status: ChapterStatus
  topicRefs: number[]           // topic.number[] that informed this chapter
  version: number
  createdAt: string
  updatedAt: string
}
```

---

## Storage Strategy

| Data | Where | Why |
|---|---|---|
| Topic content (83 folders) | Supabase `topics` table | query, search, link to chapters |
| Chapter drafts | Supabase `chapters` table | versioned, accessible everywhere |
| Canon facts | Supabase `canon` table | key/value, lockable, JSONB value |
| Characters, timeline | Supabase tables | relational, queryable |
| Large raw files (original .txt) | Supabase Storage bucket | blob storage, not queried |
| Current working chapter | AsyncStorage / MMKV (Expo) | offline, zero-latency on mobile |
| User preferences | AsyncStorage / MMKV (Expo) | local only |
| Canon snapshot (offline) | AsyncStorage / MMKV (Expo) | read-only local reference |

### Supabase Storage buckets
```
story-files/
  raw/
    discuss-20260301.txt        ← archived original
  exports/
    book1-draft.pdf
    book1-draft.epub
```

---

## Next.js App (Web) — Page Structure

```
app/
  dashboard/          → overview: word count, chapter status
  topics/
    page.tsx          → grid of all 83 topics
    [slug]/page.tsx   → single topic full content
  canon/
    page.tsx          → all canon entries, locked/unlocked
    [key]/page.tsx    → edit a canon entry
  characters/
    page.tsx          → character list
    [id]/page.tsx     → character profile + timeline
  timeline/
    page.tsx          → visual timeline of events
  chapters/
    page.tsx          → chapter list with status
    [id]/
      page.tsx        → read chapter
      edit/page.tsx   → write/edit chapter (Markdown editor)
  build/
    page.tsx          → assemble Book 1 from chapters → export
```

---

## Expo App (Mobile) — Screen Structure

```
screens/
  HomeScreen          → quick stats, recent chapter
  ChapterReadScreen   → read current draft offline
  CanonLookupScreen   → search canon entries
  CharacterScreen     → character quick reference
  NotesScreen         → capture story ideas → saved to Supabase
```

---

## Import Script (One-Time)

Move the 83 `content.txt` files into Supabase:

```typescript
// tools/import-topics.ts
import { createClient } from '@supabase/supabase-js'
import fs from 'fs'
import path from 'path'

const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_SERVICE_KEY!)

const BASE = path.resolve(__dirname, '..')

async function importTopics() {
  const folders = fs.readdirSync(BASE).filter(f => /^\d{2}-/.test(f))

  for (const folder of folders) {
    const match = folder.match(/^(\d+)-(.+)$/)
    if (!match) continue

    const number = parseInt(match[1])
    const slug = match[2].toLowerCase()
    const title = match[2].replace(/-/g, ' ')
    const contentPath = path.join(BASE, folder, 'content.txt')

    if (!fs.existsSync(contentPath)) continue

    const content = fs.readFileSync(contentPath, 'utf8')

    const { error } = await supabase.from('topics').upsert({
      number,
      slug,
      title,
      content,
    }, { onConflict: 'slug' })

    if (error) console.error(`Error importing ${folder}:`, error)
    else console.log(`Imported: ${folder}`)
  }
}

importTopics()
```

Run once: `npx ts-node tools/import-topics.ts`

---

## Recommended Packages

```jsonc
// shared across Next.js and Expo
{
  "@supabase/supabase-js": "^2",       // Supabase client
  "zod": "^3",                          // runtime type validation on canon/story data

  // Next.js only
  "@uiw/react-md-editor": "^4",        // Markdown chapter editor
  "next": "^15",

  // Expo only
  "expo": "^52",
  "@react-native-async-storage/async-storage": "^2",
  "react-native-mmkv": "^2"            // faster alternative to AsyncStorage for canon cache
}
```

---

## Canon Key Convention

```
daneel.origin
daneel.substrate.current
x20.year
x20.scientist_name
foundation.established_year
alejandro.birth_year
alejandro.death_year
deejay.birth_year
entity.nature
book1.chapter_count
book1.word_target
```

Access pattern:
```typescript
const { data } = await supabase
  .from('canon')
  .select('value')
  .eq('key', 'x20.year')
  .single()

const x20Year = data?.value as number  // fully typed
```

---

## AI Layer — OpenAI API

### What it enables

| Feature | How | OpenAI capability |
|---|---|---|
| Semantic topic search | Embed all 83 topics → store in pgvector → query by meaning | `text-embedding-3-small` |
| Canon consistency check | Feed canon + chapter draft → detect contradictions | GPT-4o + structured output |
| Character voice check | Feed character profile + dialogue → flag out-of-voice lines | GPT-4o |
| Draft from topic | Summarise a topic range into a scene outline | GPT-4o |
| Continuity QA | Cross-check chapter against timeline | GPT-4o + function calling |
| Canon extraction | Parse a topic's content → suggest new canon entries | GPT-4o structured output + Zod |

### Embeddings → pgvector

Enable `pgvector` extension in Supabase, then add to `topics` table:

```sql
alter table topics add column embedding vector(1536);

create index on topics using ivfflat (embedding vector_cosine_ops)
  with (lists = 10);
```

Embed once on import:

```typescript
// tools/embed-topics.ts
import OpenAI from 'openai'
import { createClient } from '@supabase/supabase-js'

const openai = new OpenAI()
const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_SERVICE_KEY!)

async function embedTopics() {
  const { data: topics } = await supabase.from('topics').select('id, content')

  for (const topic of topics ?? []) {
    const { data: [{ embedding }] } = await openai.embeddings.create({
      model: 'text-embedding-3-small',
      input: topic.content.slice(0, 8000),   // token limit
    })

    await supabase.from('topics')
      .update({ embedding })
      .eq('id', topic.id)

    console.log(`Embedded topic ${topic.id}`)
  }
}

embedTopics()
```

Semantic search query:

```typescript
async function searchTopics(query: string, limit = 5) {
  const { data: [{ embedding }] } = await openai.embeddings.create({
    model: 'text-embedding-3-small',
    input: query,
  })

  const { data } = await supabase.rpc('match_topics', {
    query_embedding: embedding,
    match_count: limit,
  })

  return data
}
```

### Canon Consistency Check (structured output)

```typescript
import { z } from 'zod'

const ConsistencyReport = z.object({
  consistent: z.boolean(),
  issues: z.array(z.object({
    severity: z.enum(['error', 'warning', 'note']),
    description: z.string(),
    canon_key: z.string().optional(),
    chapter_line: z.string().optional(),
  })),
  suggestions: z.array(z.string()),
})

async function checkConsistency(chapterContent: string, canonEntries: CanonEntry[]) {
  const completion = await openai.beta.chat.completions.parse({
    model: 'gpt-4o',
    messages: [
      {
        role: 'system',
        content: 'You are a story continuity editor for the novel GrayArea. '
               + 'Check the chapter draft for contradictions with the canon.',
      },
      {
        role: 'user',
        content: JSON.stringify({ canon: canonEntries, chapter: chapterContent }),
      },
    ],
    response_format: zodResponseFormat(ConsistencyReport, 'consistency_report'),
  })

  return completion.choices[0].message.parsed
}
```

---

## MCP Server — `grayarea-mcp`

An MCP server gives any MCP-compatible AI client (Claude Desktop, Cursor, custom
chat UI) direct access to the GrayArea story bible — no prompt engineering needed,
just structured tool calls.

### Resources exposed

| Resource URI | Description |
|---|---|
| `grayarea://topics` | List of all 83 topics |
| `grayarea://topics/{slug}` | Full content of one topic |
| `grayarea://canon` | All canon entries (key/value) |
| `grayarea://canon/{key}` | Single canon value |
| `grayarea://characters` | Character list |
| `grayarea://characters/{id}` | Character profile |
| `grayarea://timeline` | All timeline events |
| `grayarea://chapters` | Chapter list with status |
| `grayarea://chapters/{id}` | Chapter content |

### Tools exposed

| Tool | Args | Returns |
|---|---|---|
| `search_topics` | `query: string, limit?: number` | Semantically similar topics |
| `get_canon` | `key: string` | Canon value for key |
| `set_canon` | `key, value, note?` | Upserts canon entry |
| `check_consistency` | `chapter_id` | GPT-4o consistency report |
| `get_character_timeline` | `character_id` | All events for character |
| `find_topic_by_theme` | `theme: string` | Topics matching a theme |

### Minimal MCP server skeleton

```typescript
// mcp/server.ts
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'
import { z } from 'zod'
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_SERVICE_KEY!)
const server = new McpServer({ name: 'grayarea', version: '1.0.0' })

// Resource: single topic
server.resource(
  'topic',
  'grayarea://topics/{slug}',
  async (uri, { slug }) => {
    const { data } = await supabase.from('topics').select('*').eq('slug', slug).single()
    return { contents: [{ uri: uri.href, text: data?.content ?? 'Not found', mimeType: 'text/plain' }] }
  }
)

// Tool: get canon value
server.tool(
  'get_canon',
  'Get a canon fact by its dot-notated key',
  { key: z.string() },
  async ({ key }) => {
    const { data } = await supabase.from('canon').select('value, note').eq('key', key).single()
    return { content: [{ type: 'text', text: JSON.stringify(data) }] }
  }
)

// Tool: semantic topic search
server.tool(
  'search_topics',
  'Find topics by semantic meaning',
  { query: z.string(), limit: z.number().optional().default(5) },
  async ({ query, limit }) => {
    const results = await searchTopics(query, limit)    // uses pgvector fn above
    return { content: [{ type: 'text', text: JSON.stringify(results) }] }
  }
)

const transport = new StdioServerTransport()
await server.connect(transport)
```

Run as stdio process — configure in Claude Desktop's `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "grayarea": {
      "command": "npx",
      "args": ["ts-node", "mcp/server.ts"],
      "env": {
        "SUPABASE_URL": "your-url",
        "SUPABASE_SERVICE_KEY": "your-key"
      }
    }
  }
}
```

---

## Recommended Packages (updated)

```jsonc
{
  // Core
  "@supabase/supabase-js": "^2",
  "openai": "^4",
  "zod": "^3",

  // MCP
  "@modelcontextprotocol/sdk": "^1",

  // Next.js
  "next": "^15",
  "@uiw/react-md-editor": "^4",

  // Expo
  "expo": "^52",
  "@react-native-async-storage/async-storage": "^2",
  "react-native-mmkv": "^2"
}
```

---

## Build Order

```
Phase 1 — Data foundation
  ✓ 83 topic folders exist
  → import-topics.ts        load topics into Supabase
  → embed-topics.ts         generate + store embeddings
  → seed canon.sql          lock known canon facts

Phase 2 — Web app
  → Next.js scaffold
  → /topics browser
  → /canon editor
  → /chapters writer

Phase 3 — AI features
  → semantic search on /topics
  → consistency checker on /chapters
  → canon extraction from topics

Phase 4 — MCP server
  → grayarea-mcp stdio server
  → Claude Desktop integration
  → (optional) HTTP transport for Expo chat screen

Phase 5 — Mobile (Expo)
  → offline canon reader
  → chapter companion
  → voice notes → Whisper → Supabase
```

---

*Last updated: 2026-03-02*
