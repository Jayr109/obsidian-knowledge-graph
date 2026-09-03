---
title: "Turing Machines"
type: concept
tags: [turing-machines, computability, church-turing, decidability, models-of-computation]
sources: [lecture-4-decidability-and-undecidability]
course: CSCE 411
updated: 2026-08-25
---

A Turing machine (TM) is the idealized model of computation used to define what is computable at all. It consists of an infinite tape, a read/write head, and a finite state control. TMs are the formal setting for [[Decidability and Undecidability|decidability]] and for the [[Halting Problem]].

## Model

- **Infinite tape** — unbounded storage, read and written one cell at a time
- **Read/write head** — moves left or right one cell per step
- **Finite state control** — a fixed, finite set of states driving transitions

A TM is strictly more powerful than a finite automaton, and can simulate any algorithm.

## Three Behaviors

On any input, a TM does exactly one of:

1. **Accept** — halts in an accept state
2. **Reject** — halts in a reject state
3. **Loop** — runs forever

The third possibility is what makes decidability non-trivial: a machine that never halts gives no answer.

## Deciders vs. Recognizers

| Term | Meaning |
|---|---|
| **Decider** | A TM that always halts — accepts or rejects, never loops |
| **Decidable language** | A language for which some decider exists |
| **Recognizer (semi-decidable)** | A TM that accepts every string in the language, but may loop on strings outside it |

Every decidable language is recognizable; the converse fails — [[Halting Problem|HALTS]] is recognizable but not decidable.

## Church-Turing Thesis

Anything solvable by an algorithm can be solved by a Turing machine.

The practical payoff for coursework: TMs may be described in pseudocode rather than formal state-transition diagrams, since any clearly-specified algorithm can be taken as a TM.

## String Encodings

Objects — graphs, programs, other TMs — are encoded as strings so they can be fed to a TM as input.

- ⟨M⟩ — the encoding of TM M
- ⟨M, x⟩ — the encoding of a pair

This self-referential capacity, a TM taking another TM's encoding as input, is what enables the diagonalization argument in the [[Halting Problem]].

## See Also

- [[Decidability and Undecidability]]
- [[Halting Problem]]
- [[Turing Reductions]]
- [[CSCE 411]]
