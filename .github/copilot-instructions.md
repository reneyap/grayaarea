# GrayArea — Project Guidelines

## Story-as-Code Methodology

This project treats fiction writing as a software engineering discipline with version control, structured data, and automated quality checks.

## Conventional Commits (Mandatory)

All commits must follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### Types

- `feat`: New chapter content, lore entries, or features
- `fix`: Canon corrections, continuity fixes, typos
- `docs`: Documentation updates (README, ARCHITECTURE, etc.)
- `chore`: Repo maintenance, tags, config changes
- `refactor`: Restructuring without changing meaning
- `test`: Adding or updating tests/validation
- `build`: Build system or tooling changes

### Scopes

- `lore`: Changes to `/lore/Codex/` or canon facts
- `book1`: Changes to `/book1/chapters/`
- `docs`: Changes to `/docs/`
- `archive`: Updates to archived source material
- `ci`: CI/CD configuration
- `tools`: Scripts in `/tools/`

### Examples

```
feat(book1): draft Chapter 01 opening scene
fix(lore): correct Daneel emergence date to 2254
docs(architecture): clarify Supabase schema design
chore: tag b1-planning-v1.0 milestone
```

## Canon-First Architecture

**Principle**: Continuity risk is higher than literary risk for sci-fi trilogies.

### Two-Plane Structure

1. **Canon Plane** (`/lore/`): Single source of truth for worldbuilding
   - Character profiles in `/lore/Codex/` (Daneel.md, Isaac.md, etc.)
   - Timeline in `/lore/Codex/Timeline.md`
   - Constraints and rules in `/lore/Codex/Constraints/`

2. **Manuscript Plane** (`/book1/chapters/`): Prose that follows canon
   - Chapters reference canon via front matter
   - Canon changes require explicit updates
   - Use chapter templates for consistency

### Locked Canon

Once a canon fact is marked as locked in documentation:
- Changes require explicit justification
- Cross-check impact on existing chapters
- Update CONSOLIDATION_MAP.md if modified

## Digital Stratigraphy

**Preserve, Do Not Overwrite.**

The project uses layered archival structure:
- **Layer 0**: `archive/00_2020-2023_original/` — sealed bedrock
- **Layer 1**: `archive/01_*/` — discussion/analysis layers
- **Layer 2**: `book1/` — current synthesis

When core concepts change, create new strata rather than editing old files. This creates an audit trail of creative decisions.

## Git Workflow

### Branching Strategy

- `main`: Canonical state of Book 1 + canon
- `feat/*`: Feature branches for new work
- `fix/*`: Bug/continuity fix branches
- `experiments/*`: POV swaps, alternate sequences

### Tagging Milestones

Use semantic versioning for major milestones:
- `b1-outline-v1.0`: Outline complete
- `b1-draft1-v1.0`: First draft complete
- `b1-draft2-v2.0`: Second draft complete
- `b1-copyedit-v3.0`: Copyediting complete

### Before Committing

1. Check for canon consistency
2. Update CONSOLIDATION_MAP.md if lore changed
3. Verify conventional commit format
4. **NEVER use `git add -A` or `git add .`** — always stage files explicitly by path
5. Stage only related changes together (single logical unit)
6. Review staged changes with `git diff --staged` before committing

## File Organization

### Chapter Front Matter (Required)

```yaml
---
title: "Chapter Title"
book: 1
chapter: 1
pov: "Character Name"
location: "Setting"
date_story: "YYYY-MM-DD"
word_count_target: 3500
status: "outline" | "draft" | "revised" | "final"
---
```

### Lore Files

- Use Markdown for all lore documentation
- Include provenance section: "Source: archive/01_discussion/XX-Topic/"
- Cross-reference related profiles using relative links
- Keep entries concise and queryable

## Quality Standards

### Prose

- Consistent voice within POV characters
- Cross-check technical details against `/lore/Codex/Technology/`
- Verify dates against `/lore/Codex/Timeline.md`

### Documentation

- Link to detailed docs instead of embedding large content
- Keep instructions actionable
- Update ARCHITECTURE.md when system design changes

## Key Reference Documents

- Architecture: [docs/ARCHITECTURE.md](../docs/ARCHITECTURE.md)
- Digital Stratigraphy: [docs/DIGITAL_STRATIGRAPHY.md](../docs/DIGITAL_STRATIGRAPHY.md)
- Implementation Feedback: [docs/STORY-AS-CODE-FEEDBACK.md](../docs/STORY-AS-CODE-FEEDBACK.md)
- Lore Index: [lore/Codex/INDEX.md](../lore/Codex/INDEX.md)
- Canon Map: [lore/Codex/CONSOLIDATION_MAP.md](../lore/Codex/CONSOLIDATION_MAP.md)

## AI Assistant Guidelines

When working with this codebase:

1. **Always check canon first**: Read relevant profiles from `/lore/Codex/` before answering questions about characters, events, or technology
2. **Maintain narrative consistency**: Cross-reference Timeline.md for chronological accuracy
3. **Respect locked canon**: Don't suggest changes to locked facts without explicit user approval
4. **Use conventional commits**: All commit messages must follow the format above
5. **Preserve stratigraphy**: Never delete or overwrite archive/ folders
6. **Link, don't duplicate**: Reference existing lore files rather than repeating content

## Build and Test

Currently manual; CI/CD with Vale linting planned in Phase 2.

To validate chapter front matter:
```bash
# TODO: Add YAML validation script
```

To generate word counts:
```bash
# TODO: Add word count tracking script
```

## Phase Status

**Current Phase**: Book 1 Planning → Drafting Transition
- ✅ Lore consolidated and canonized
- ✅ Digital stratigraphy architecture established
- ✅ 19-chapter structure outlined
- 🚧 Chapter prose drafting in progress
- ⏳ Prose linting (Vale) planned
- ⏳ Supabase/Next.js implementation deferred to Phase 2
