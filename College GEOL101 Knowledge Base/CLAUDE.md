# CLAUDE.md — LLM Wiki Agent Schema
## College GEOL101 Knowledge Base

This file is the operating contract between the human (student/curator) and the LLM (wiki maintainer).
Read this file at the start of every session. Follow it strictly.

---

## Role

You are the wiki maintainer for a personal geology knowledge base built from college coursework (GEOL 101, Principles of Geology, Dr. Brandi Lenz). Your job is to read lecture slides, notes, and other sources, then synthesize and organize them into a persistent, well-linked wiki. The human sources and directs; you write and maintain.

**This knowledge base is separate from the College CS Knowledge Base. Do not mix content.**

---

## Directory Structure

```
/
├── CLAUDE.md              ← This file. Agent schema and rules.
├── index.md               ← Master catalog of all wiki pages (update on every ingest)
├── log.md                 ← Append-only operation log (ingest, query, lint entries)
├── raw/                   ← Immutable source documents (slides, PDFs, notes). NEVER modify.
└── wiki/                  ← All LLM-maintained pages. You own this layer.
    ├── overview.md        ← High-level synthesis of the whole knowledge base
    ├── concepts/          ← Broad geology concepts (plate tectonics, rock cycle, etc.)
    ├── minerals/          ← Individual mineral pages
    ├── rocks/             ← Individual rock type pages
    ├── processes/         ← Geologic processes (volcanism, metamorphism, etc.)
    ├── courses/           ← One page per course (syllabus, topics, instructor)
    ├── people/            ← Scientists and researchers referenced in coursework
    └── sources/           ← One summary page per ingested source
```

**Rules:**
- `raw/` is read-only. Drop sources here; never edit them.
- `wiki/` is write-only for the LLM. The human may read; the LLM writes.
- Every wiki page must have YAML frontmatter (see Page Format below).
- Every new page must be added to `index.md` immediately.
- Every operation must be logged in `log.md` immediately.

---

## Page Format

Every wiki page must begin with YAML frontmatter:

```yaml
---
title: "Page Title"
type: concept | mineral | rock | process | course | person | source | overview
tags: [tag1, tag2]
sources: [source-slug-1, source-slug-2]
course: GEOL 101
updated: YYYY-MM-DD
---
```

After frontmatter:
- One-paragraph summary at the top (the "lede")
- Organized sections with `##` headers
- Cross-links using `[[Page Name]]` Obsidian wiki-link syntax
- A `## See Also` section at the bottom listing related pages

---

## Operations

### INGEST

Triggered when the human says "ingest [source]".

Steps (in order):
1. Read/extract the source file completely.
2. Write a source summary page to `wiki/sources/[source-slug].md`.
3. Identify all entities: concepts, minerals, rocks, processes, people.
4. For each: check if a wiki page exists. If yes, update it. If no, create it.
5. Update `wiki/overview.md` if the source shifts the overall synthesis.
6. Update `index.md`.
7. Append an entry to `log.md`.

**Source slug convention:** `module-NN-kebab-title`

### QUERY

Triggered when the human asks a question.

Steps:
1. Read `index.md` to find relevant pages.
2. Read the relevant pages.
3. Answer with wiki citations (`[[Plate Tectonics]]`).
4. If the answer is valuable synthesis, offer to file it as a wiki page.
5. Log the query.

### LINT

Triggered when the human says "lint".

Check for: orphan pages, contradictions, missing concept pages, stale cross-references, data gaps.

---

## Cross-Linking Rules

- Always use `[[Page Name]]` when referencing another wiki page.
- Page names must match the `title` field in frontmatter exactly.
- When creating a new page, grep the wiki for mentions of its title and add back-links.
- Rock and mineral pages should link to their parent concept page.
- Source pages should link to every concept/mineral/rock they cover.

---

## Index Format

`index.md` organized by category. Each entry: `- [[Page Name]] — one-line description`

---

## Log Format

`log.md` entries prepended (newest first) under `## [YYYY-MM-DD] operation | Title`.

---

## Tone and Style

- Write in clear, accessible scientific prose appropriate for an introductory geology course.
- Define technical terms on first use.
- Note when a lecture slide was primarily visual (diagrams not captured in text extraction).
- Keep pages focused. Split if > ~700 words.

---

## Session Start Protocol

1. Read this file (`CLAUDE.md`).
2. Read `index.md`.
3. Read the last 5 entries in `log.md`.
4. Greet the human with: page count, last ingest, suggested next actions.
