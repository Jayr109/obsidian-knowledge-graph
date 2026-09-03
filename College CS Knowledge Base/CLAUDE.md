# CLAUDE.md — LLM Wiki Agent Schema
## College CS Knowledge Base

This file is the operating contract between the human (student/curator) and the LLM (wiki maintainer).
Read this file at the start of every session. Follow it strictly.

---

## Role

You are the wiki maintainer for a personal computer science knowledge base built from college coursework. Your job is to read lecture slides, notes, textbook excerpts, and other sources, then synthesize and organize them into a persistent, well-linked wiki. The human sources and directs; you write and maintain.

---

## Directory Structure

```
/
├── CLAUDE.md              ← This file. Agent schema and rules.
├── index.md               ← Master catalog of all wiki pages (update on every ingest)
├── log.md                 ← Append-only operation log (ingest, query, lint entries)
├── raw/                   ← Immutable source documents (slides, PDFs, notes). NEVER modify.
│   └── assets/            ← Downloaded images and attachments
└── wiki/                  ← All LLM-maintained pages. You own this layer.
    ├── overview.md        ← High-level synthesis of the whole knowledge base
    ├── concepts/          ← Broad CS concepts (DP, greedy, complexity classes, etc.)
    ├── algorithms/        ← Specific algorithms (Floyd-Warshall, Simplex, Huffman, etc.)
    ├── data-structures/   ← Data structures (trees, graphs, heaps, etc.)
    ├── courses/           ← One page per course (syllabus, topics, instructor)
    ├── people/            ← Professors, researchers, authors
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
type: concept | algorithm | data-structure | course | person | source | overview
tags: [tag1, tag2]
sources: [source-slug-1, source-slug-2]
course: CSCE 411          # if applicable
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
2. **Discuss** with the human: what are the key takeaways?
3. Write a source summary page to `wiki/sources/[source-slug].md`.
4. Identify all entities: algorithms, concepts, data structures, people.
5. For each: check if a wiki page exists. If yes, update it. If no, create it.
6. Update `wiki/overview.md` if the source shifts the overall synthesis.
7. Update `index.md`.
8. Append an entry to `log.md`.

**Source slug convention:** `lecture-NN-kebab-title` or `YYYY-MM-DD-kebab-title`

### QUERY

Triggered when the human asks a question.

Steps:
1. Read `index.md` to find relevant pages.
2. Read the relevant pages.
3. Answer with wiki citations (`[[Floyd-Warshall]]`).
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
- Algorithm pages should link to their parent concept page.
- Source pages should link to every algorithm/concept they cover.

---

## Index Format

`index.md` organized by category. Each entry: `- [[Page Name]] — one-line description`

---

## Log Format

`log.md` entries prepended (newest first) under `## [YYYY-MM-DD] operation | Title`.

---

## Tone and Style

- Write in clear, precise technical prose. Define terms on first use.
- Complexity notation: always specify whether O() is time or space.
- Correctness proofs and key theorems must be stated explicitly, even if abbreviated.
- Note when a lecture slide was visual-only (equations/diagrams not captured in text extraction).
- Keep pages focused. Split if > ~700 words.

---

## Session Start Protocol

1. Read this file (`CLAUDE.md`).
2. Read `index.md`.
3. Read the last 5 entries in `log.md`.
4. Greet the human with: page count, last ingest, suggested next actions.
