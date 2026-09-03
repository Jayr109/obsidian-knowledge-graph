---
title: "Lecture 5 — Undecidability Reductions"
type: source
tags: [lecture, undecidability, turing-reductions, halting-problem]
sources: [lecture-5-undecidability-reductions]
course: CSCE 411
updated: 2026-04-09
---

# Lecture 5 — Undecidability Reductions

**Course**: CSCE 411 | **Slides**: 10

## Learning Objective

Prove languages undecidable using Turing reductions from known undecidable languages.

## Focus

This lecture is entirely about the mechanics and patterns of undecidability reduction proofs. It builds directly on [[Lecture 4 — Decidability and Undecidability|Lecture 4]].

## General Pattern for Turing Reduction Proofs

To prove language L is undecidable:

1. **Assume for contradiction** that a decider M_L for L exists.
2. **Construct** a new TM M_HALTS that uses M_L as a subroutine:
   - On input ⟨M, x⟩ (a TM and an input), construct a helper TM M' whose behavior relates to whether M(x) halts.
   - Run M_L on ⟨M'⟩.
   - Use the output to decide HALTS.
3. **Conclude** that M_HALTS decides HALTS — a contradiction since HALTS is undecidable.
4. Therefore M_L does not exist and L is undecidable.

## Direction Matters

Reduce **FROM** a known undecidable language **TO** the new language L.

- Correct: "If I could decide L, I could decide HALTS" → L is undecidable.
- Incorrect (proves nothing): "If I could decide HALTS, I could decide L" — this only shows L is semi-decidable or harder than HALTS, not that L is undecidable.

## Choosing the Source Language

- **HALTS** is the standard starting point. Use it when the problem is about TM behavior on some input.
- Use a **different undecidable language** (e.g., PCP — Post Correspondence Problem) if the structure of L more closely resembles that language. The principle is the same: any undecidable source suffices.

## See Also

- [[Turing Reductions]]
- [[Decidability and Undecidability]]
- [[Halting Problem]]
- [[CSCE 411]]
