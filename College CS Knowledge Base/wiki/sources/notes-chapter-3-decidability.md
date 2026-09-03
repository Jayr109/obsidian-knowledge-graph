---
title: "Course Notes — Chapter 3: Decidability and Undecidability"
type: source
tags: [csce411, notes, decidability, undecidability, turing-machines, halting-problem]
sources: []
course: CSCE 411
updated: 2026-04-09
---

# Course Notes — Chapter 3: Decidability and Undecidability

**Source files:**
- `raw/CSCE_411_Notes_Sp26_Chapter_3_Decidability_and_Undecidability (2).pdf`
- `raw/CSCE_411_Notes_Sp26_Chapter_3_Decidability_and_Undecidability (3).pdf`

> **Note on duplicates:** Files `(2).pdf` and `(3).pdf` are identical — same file size, same content. Only one unique document exists. This page covers that single document.

**Course:** CSCE 411, Spring 2026
**Type:** Official course reading notes

## Content Overview

### Turing Machines
- Formal definition: states, tape alphabet, transition function
- Configurations and computation steps
- TM variants (multi-tape, nondeterministic) and their equivalence

### Languages and Decidability
- **Decidable language:** a TM that always halts and accepts/rejects correctly
- **Semi-decidable (recognizable) language:** a TM that accepts all strings in L; may loop on strings not in L
- Relationship: decidable ⊂ semi-decidable ⊂ all languages

### The Halting Problem
- HTM = {⟨M, w⟩ : M is a TM and M halts on w}
- **Theorem:** HTM is undecidable.
- Proof by diagonalization (Cantor-style): assume a decider D for HTM exists, construct machine H that contradicts D's behavior on its own encoding.

### Turing Reductions
- A ≤T B: "A reduces to B" — if we can decide B, we can decide A
- Used to show undecidability: if A is undecidable and A ≤T B, then B is undecidable
- Technique: given a supposed decider for B, construct a decider for A (contradiction)

### Examples of Undecidable Problems
- ATM = {⟨M, w⟩ : M accepts w} — undecidable
- ETM = {⟨M⟩ : L(M) = ∅} — undecidable
- EQTM = {⟨M₁, M₂⟩ : L(M₁) = L(M₂)} — undecidable
- **Post Correspondence Problem (PCP):** undecidable combinatorial problem often used as a reduction source

## See Also

- [[Decidability and Undecidability]]
- [[Turing Reductions]]
- [[Halting Problem]]
- [[CSCE 411]]
