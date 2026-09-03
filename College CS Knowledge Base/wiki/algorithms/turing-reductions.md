---
title: "Turing Reductions"
type: algorithm
tags: [turing-reductions, undecidability, computability, halting-problem]
sources: [lecture-4-decidability-and-undecidability, lecture-5-undecidability-reductions]
course: CSCE 411
updated: 2026-04-09
---

# Turing Reductions

A Turing reduction from language A to language B provides a way to decide A using a hypothetical decider for B as a subroutine. If no decider for A can exist, and if A reduces to B, then no decider for B can exist either.

## Use in Undecidability Proofs

To prove language L is undecidable:

1. **Assume for contradiction** that a decider M_L for L exists.
2. **Construct** a decider M_HALTS for HALTS using M_L:
   - On input ⟨M, x⟩, build a helper TM M' whose membership in L is equivalent to M(x) halting.
   - Run M_L(⟨M'⟩) and use the output to decide HALTS(⟨M, x⟩).
3. **Contradiction**: HALTS is undecidable, so M_HALTS cannot exist.
4. **Conclude**: M_L cannot exist; L is undecidable.

## Direction Matters

**Reduce FROM HALTS TO L** (not from L to HALTS).

- The argument is: "A decider for L would give us a decider for HALTS."
- If you reduce the other way (from L to HALTS), you only show that L is at most as hard as HALTS — this says nothing about L being undecidable.

## General Proof Template

```
Assume for contradiction: decider M_L for L exists.

Construct M_HALTS(⟨M, x⟩):
  Construct a TM M' such that:
    [define M' behavior in terms of M(x)]
    [M' ∈ L iff M(x) halts — or similar equivalence]
  Run M_L(⟨M'⟩)
  Output the result (possibly negated)

M_HALTS decides HALTS. ↯ (HALTS is undecidable)
Therefore M_L does not exist. L is undecidable. ∎
```

## Choosing the Source Language

- **HALTS** is the default. Use it when the problem asks about whether a TM halts or loops on some input.
- **Different undecidable language** (e.g., PCP — Post Correspondence Problem): use when the structure of L more closely resembles that problem. Any undecidable source language is sufficient.
- The principle is identical regardless of which undecidable language is used as the source.

## Contrast with Many-One Reductions

Turing reductions (also called oracle reductions or Cook reductions) are more general than many-one (Karp) reductions. In a Turing reduction, the decider for B may be called multiple times and with different inputs. In a many-one reduction, the input is transformed once and passed to B exactly once.

## See Also

- [[Decidability and Undecidability]]
- [[Halting Problem]]
- [[CSCE 411]]
