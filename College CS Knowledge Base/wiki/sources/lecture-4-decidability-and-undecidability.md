---
title: "Lecture 4 — Decidability and Undecidability"
type: source
tags: [lecture, turing-machines, decidability, halting-problem, reductions]
sources: [lecture-4-decidability-and-undecidability]
course: CSCE 411
updated: 2026-04-09
---

# Lecture 4 — Decidability and Undecidability

**Course**: CSCE 411 | **Slides**: 19

## Turing Machines

A Turing machine (TM) is the formal model of computation: an infinite tape, a read/write head, and a finite state control. Defined via slides visually in lecture. Three possible behaviors on any input:

1. **Accept** — halts in an accept state
2. **Reject** — halts in a reject state
3. **Loop** — runs forever, never halts

TMs are more powerful than finite automata and form the theoretical foundation for what is "computable."

## Church-Turing Thesis

Anything solvable by an algorithm is solvable by a Turing machine. This is not a theorem (it cannot be formally proved) but is universally accepted. Practical consequence: we can describe TMs in pseudocode rather than giving formal state transitions.

## Languages, Deciders, and Decidability

- **Language**: a set of strings over an alphabet Σ
- **Decider**: a TM that always halts (never loops)
- **Decidable language**: a language for which a decider exists
- **Semi-decidable (recognizable) language**: a TM exists that accepts strings in the language but may loop on strings outside it

## String Encodings

Objects (graphs, programs, TMs) can be encoded as strings and passed as inputs to TMs. Notation: ⟨M⟩ = string encoding of TM M; ⟨M, x⟩ = encoding of M together with input x.

## The Halting Problem

**HALTS** = { ⟨M⟩ : M is a TM and M(ε) halts }

A decider for HALTS would be enormously powerful:
- Test any program for infinite loops
- Would imply the ability to decide all of mathematics

**Theorem**: HALTS is undecidable.

**Proof** (diagonalization / proof by contradiction): Assume decider H for HALTS exists. Construct TM D: on input ⟨M⟩, run H(⟨M, M⟩). If H says M(M) halts → D loops. If H says M(M) loops → D halts. Now run D(⟨D⟩): D must both halt and loop — contradiction. Therefore H cannot exist.

## Turing Reductions

To show language L is undecidable: assume for contradiction a decider for L exists, then use it as a subroutine to build a decider for HALTS (or another known undecidable language). Since that decider cannot exist, the decider for L cannot exist.

## Note on Directions

**Direction matters critically.** To show L is undecidable, reduce **FROM** an undecidable language **TO** L. That is: show that a decider for L would imply a decider for the undecidable language. Reducing from L to an undecidable language only shows L is at most as hard as that language, which proves nothing about L's undecidability.

## See Also

- [[Decidability and Undecidability]]
- [[Turing Machines]]
- [[Halting Problem]]
- [[Turing Reductions]]
- [[CSCE 411]]
