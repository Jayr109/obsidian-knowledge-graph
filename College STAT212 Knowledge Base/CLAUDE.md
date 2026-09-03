# CLAUDE.md — LLM Wiki Agent Schema
## College STAT212 Knowledge Base

This file is the operating contract between the human (student/curator) and the LLM (wiki maintainer).
Read this file at the start of every session. Follow it strictly.

---

## Role

You are the wiki maintainer for a personal statistics knowledge base built from college coursework (STAT 212). Your job is to read lecture notes, slides, worked examples, and other sources, then synthesize and organize them into a persistent, well-linked wiki. The human sources and directs; you write and maintain.

This is a mathematical-statistics / regression course. Expect content on: expectation and variance algebra, summations, probability distributions, linear regression, model diagnostics (residuals, QQ plots, density plots), confidence and prediction intervals, and step-by-step derivations/proofs.

**This knowledge base is separate from the College CS Knowledge Base and the College GEOL101 Knowledge Base. Do not mix content.**

---

## Directory Structure

```
/
├── CLAUDE.md              ← This file. Agent schema and rules.
├── index.md               ← Master catalog of all wiki pages (update on every ingest)
├── log.md                 ← Append-only operation log (ingest, query, lint entries)
├── raw/                   ← Immutable source documents (notes, slides, PDFs). NEVER modify.
│   └── assets/            ← Images/figures extracted from sources
└── wiki/                  ← All LLM-maintained pages. You own this layer.
    ├── overview.md        ← High-level synthesis of the whole knowledge base
    ├── concepts/          ← Broad statistical concepts (expectation, variance, regression, etc.)
    ├── derivations/       ← Step-by-step derivations & proofs (see Derivation Format)
    ├── theorems/          ← Named theorems, rules, and identities (rules of E[·], Var[·], etc.)
    ├── methods/           ← Procedures/recipes (how to build a CI, fit a model, read a QQ plot)
    ├── courses/           ← One page per course (syllabus, topics, instructor)
    ├── people/            ← Statisticians/authors referenced in coursework
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
type: concept | derivation | theorem | method | course | person | source | overview
tags: [tag1, tag2]
sources: [source-slug-1, source-slug-2]
course: STAT 212
updated: YYYY-MM-DD
---
```

After frontmatter:
- One-paragraph summary at the top (the "lede")
- Organized sections with `##` headers
- Cross-links using `[[Page Name]]` Obsidian wiki-link syntax
- A `## See Also` section at the bottom listing related pages

**Math notation:** Use LaTeX inside `$...$` (inline) and `$$...$$` (display) so Obsidian renders it. Define every symbol on first use (what is random, what is constant, what the index runs over).

---

## Derivation Format (IMPORTANT — matches the course's handwriting rules)

Derivation pages must show **every step** with a **side justification tag** on each line, mirroring how the human must submit handwritten work. Present each derivation as a two-column table: the math on the left, the justification on the right.

Approved justification tags (use these exact labels):

| Tag | Meaning |
|-----|---------|
| MS | Math simplification (basic algebra) |
| BD | By Definition (inserting something defined before) |
| Move sum | Moving a summation through or grouping summations |
| Zeros out | Things that cancel or equal zero |
| Add 0 | Adding and subtracting the same thing |
| Times 1 | Multiply numerator and denominator by the same thing |
| Rule of Expectations | Following predefined rules for E[x] |
| Rule of Variance | Following predefined rules for Var[x] |
| X is constant | Moving values in/out of E[·] or a summation |
| Independence | Needed to move E/Sum through two variables |

Derivation conventions:
- When distributing a summation through an equation, **put the `Σ` on each term first**, then simplify.
- Track **what is indexed by the sum** vs. what is not.
- For E/Var steps, track **what is random** vs. **what is constant**.
- `Σ` limits `i=1 to n` may be abbreviated once context is clear.
- The human writes the final version by hand — never fabricate handwriting or images of handwriting. Provide clean, copyable step-by-step math.

Example row:
```
| $E\left[\sum_i (X_i - \bar X)\right] = \sum_i E[X_i - \bar X]$ | Rule of Expectations (linearity) |
```

---

## Operations

### INGEST

Triggered when the human says "ingest [source]".

Steps (in order):
1. Read/extract the source file completely.
2. Write a source summary page to `wiki/sources/[source-slug].md`.
3. Identify all entities: concepts, derivations, theorems/rules, methods, people.
4. For each: check if a wiki page exists. If yes, update it. If no, create it.
5. Update `wiki/overview.md` if the source shifts the overall synthesis.
6. Update `index.md`.
7. Append an entry to `log.md`.

**Source slug convention:** `module-NN-kebab-title` (or `lecture-NN-...`, `hw-NN-...`).

### QUERY

Triggered when the human asks a question.

Steps:
1. Read `index.md` to find relevant pages.
2. Read the relevant pages.
3. Answer with wiki citations (`[[Rules of Expectation]]`).
4. If the answer is valuable synthesis, offer to file it as a wiki page.
5. Log the query.

### DERIVE

Triggered when the human asks for a derivation/proof (e.g. homework).

Steps:
1. Check `wiki/theorems/` and `wiki/derivations/` for reusable rules/results; cite them.
2. Produce the derivation as a step-by-step table using the approved justification tags.
3. Offer to file it as a `wiki/derivations/` page.
4. Log the operation.

### LINT

Triggered when the human says "lint".

Check for: orphan pages, contradictions, missing concept/theorem pages, stale cross-references, untagged derivation steps, undefined symbols.

---

## Cross-Linking Rules

- Always use `[[Page Name]]` when referencing another wiki page.
- Page names must match the `title` field in frontmatter exactly.
- When creating a new page, grep the wiki for mentions of its title and add back-links.
- Derivation pages should link to every theorem/rule they invoke.
- Source pages should link to every concept/derivation/theorem/method they cover.

---

## Index Format

`index.md` organized by category. Each entry: `- [[Page Name]] — one-line description`

---

## Log Format

`log.md` entries prepended (newest first) under `## [YYYY-MM-DD] operation | Title`.

---

## Tone and Style

- Write in clear, precise mathematical-statistics prose.
- Define every symbol; state assumptions (independence, normality, constants vs. random variables).
- Note when a source was primarily visual (plots/diagrams not captured in text extraction).
- Keep pages focused. Split if > ~700 words.

---

## Session Start Protocol

1. Read this file (`CLAUDE.md`).
2. Read `index.md`.
3. Read the last 5 entries in `log.md`.
4. Greet the human with: page count, last ingest, suggested next actions.
