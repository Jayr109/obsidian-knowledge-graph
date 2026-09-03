# Obsidian Knowledge Graph

An automated, LLM-maintained knowledge base. Course material and reference documents go in;
a cross-linked Obsidian wiki comes out — with every page carrying structured frontmatter,
citations back to its sources, and `[[wiki-links]]` that render as a navigable graph.

Built with the Claude API. Six independent vaults, ~485 markdown pages.

## The idea

Note-taking apps store what you wrote. This stores what you *learned*, in a form that stays
consistent as it grows. Each vault is governed by a `CLAUDE.md` file — an explicit operating
contract between the curator (me) and the LLM (the wiki maintainer) that fixes the directory
layout, the page schema, the link conventions, and the three operations the agent may perform.

The contract is the interesting part. Without it, an LLM asked to "organize my notes" produces
a different structure every session. With it, the vault converges instead of drifting.

## Layout

```
<Vault>/
├── CLAUDE.md    Agent schema and rules — read at the start of every session
├── index.md     Master catalog of every page; updated on every ingest
├── log.md       Append-only operation log (ingest / query / lint)
├── raw/         Immutable source documents. Read-only, never edited. (not tracked — see below)
└── wiki/        The LLM-maintained layer
    ├── overview.md
    ├── concepts/          broad ideas
    ├── algorithms/        specific procedures
    ├── data-structures/
    ├── courses/           one page per course
    ├── people/            instructors, researchers, authors
    └── sources/           one summary page per ingested document
```

**Invariants:** `raw/` is never modified. `wiki/` is written only by the agent. Every page
carries YAML frontmatter. Every new page is added to `index.md` and logged in `log.md`
immediately — not at the end of a session, when it would be forgotten.

## Page schema

```yaml
---
title: "A* Search"
type: algorithm          # concept | algorithm | data-structure | course | person | source | overview
tags: [csce420, search, heuristics, optimality]
sources: [csce420-midterm-practice, csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---
```

Body: a one-paragraph lede, `##` sections, `[[cross-links]]`, and a `## See Also` footer.
Because `sources:` is required, every claim traces back to the document it came from.

## Operations

| Operation | Trigger | Effect |
|---|---|---|
| **INGEST** | "ingest \[source]" | Read a document in `raw/`, synthesize it into new or existing wiki pages, write a `sources/` summary, update `index.md`, append to `log.md` |
| **QUERY** | a question | Answer from the wiki; if the answer required new synthesis, file it as a page so the work isn't lost |
| **LINT** | "lint" | Audit the vault — dangling links, malformed frontmatter, stub pages, encoding damage, near-duplicate bodies |

## Vaults

| Vault | Pages | Subject |
|---|---|---|
| College CS | 305 | Algorithms, systems, AI, ML, security (CSCE 313 / 411 / 420 / 421 / 465) |
| College GEOL101 | 78 | Geology |
| College STAT212 | 50 | Statistics |
| College MGMT309 | 28 | Corporate finance and valuation |
| First Trading | 14 | Market structure and strategy notes |
| General | 9 | Everything else |

The CS vault indexes 302 pages: 141 concepts, 53 algorithms, 6 courses, 6 people, 94 sources.

## On the lint pass

The audit exists because re-running the same check mostly confirms the check, not the data.
A second, independent checker covering 12 problem classes the standing audit ignores — mangled
LaTeX escapes, unbalanced `[[ ]]`, self-links, dangling `sources:` slugs, near-duplicate page
bodies — found four real defects on its first run, three of them introduced by the agent
itself. Generated knowledge bases need adversarial checking, not just generation.

## A note on `raw/`

The `raw/` directories are excluded from this repository. They hold lecture slides, textbook
excerpts and other course material that belongs to its authors — not something I can
redistribute. The `wiki/` layer, which is the actual work, is fully tracked. Vaults will
therefore clone with their generated notes intact but their source documents absent; the
`sources/` pages record what each note was built from.

## Use

Open any vault folder as an Obsidian vault. The graph view renders the `[[wiki-link]]`
structure. To extend a vault, drop a document in `raw/` and run an INGEST against its
`CLAUDE.md` contract.
