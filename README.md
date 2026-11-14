# Obsidian Knowledge Graph

An automated, LLM-maintained knowledge base. Course material and reference documents go in;
a cross-linked Obsidian wiki comes out — with every page carrying structured frontmatter,
citations back to its sources, and `[[wiki-links]]` that render as a navigable graph.

Maintained with Claude Code against a per-vault contract. Six independent vaults, 628
markdown pages.

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
| College CS | 467 | Algorithms, systems, AI, ML, security (CSCE 313 / 411 / 420 / 421 / 465), plus corporate finance and valuation |
| College GEOL101 | 75 | Geology |
| College STAT212 | 47 | Statistics: regression, ANOVA, categorical data, nonparametric methods |
| College MGMT309 | 25 | Survey of management |
| First Trading | 9 | Market structure and strategy notes |
| General | 5 | Everything else |

Counts are pages under each vault's `wiki/` as of 2026-11-13. The CS vault breaks down as
219 concepts, 65 algorithms, 1 data structure, 6 courses, 6 people, 169 sources and an
overview.

The directory names under `wiki/` vary by subject. The statistics vault adds `theorems/`,
`derivations/` and `methods/`; the management vault adds `frameworks/`; the trading vault
adds `strategies/` and `instruments/`.

## On the lint pass

The audit exists because re-running the same check mostly confirms the check, not the data.
A second, independent checker covering 12 problem classes the standing audit ignores — mangled
LaTeX escapes, unbalanced `[[ ]]`, self-links, dangling `sources:` slugs, near-duplicate page
bodies — found four real defects on its first run, three of them introduced by the agent
itself. Generated knowledge bases need adversarial checking, not just generation.

## Tools

Two Python scripts live in `tools/`.

**`kb_lint.py`** is the standing audit. It runs 25 checks over one vault: 21 fail the run
and 4 print `info` only, because every strict version of those four produced mostly false
positives. It needs only the standard library.

```bash
python tools/kb_lint.py "College CS Knowledge Base"
```

Run it from the repository root. It exits 1 if any failing check finds a defect. The
failing checks cover duplicate titles, broken wiki-links, orphans, frontmatter gaps, a
`type:` that disagrees with the page's directory, `sources:` slugs with no source page,
drift between `index.md` and the pages on disk, malformed table rows, missing ledes and
`## See Also` footers, and `raw/` citations that point at nothing.

**`transcribe.py`** turns a lecture recording into ingestable text: a timestamped
transcript, word-level timestamps, and one frame per detected slide change. It needs
`faster-whisper` and `ffmpeg`, plus `yt-dlp` when given a URL.

```bash
python tools/transcribe.py lecture.mp4 --out raw/lecture-12
```

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
