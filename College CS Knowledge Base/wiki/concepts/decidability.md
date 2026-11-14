---
title: "Decidability and Undecidability"
type: concept
tags: [decidability, turing-machines, halting-problem, reductions, computability]
sources: [lecture-4-decidability-and-undecidability, lecture-5-undecidability-reductions]
course: CSCE 411
updated: 2026-08-25
---

# Decidability and Undecidability

Decidability concerns which problems can be solved by algorithms at all — a prerequisite question before asking how efficiently. The formal model used is the Turing machine.

## Definitions

- **Language**: a set of strings over an alphabet Σ
- **Decider**: a TM that always halts (accepts or rejects, never loops)
- **Decidable language**: a language for which a decider exists
- **Semi-decidable (recognizable) language**: a TM exists that accepts strings in the language but may loop on strings not in the language

## Turing Machines

The formal model of computation used throughout: infinite tape, read/write head, finite state control. On any input a TM either **accepts**, **rejects**, or **loops** — the third case is what makes decidability non-trivial. The **Church-Turing Thesis** lets us describe TMs in pseudocode rather than state-transition diagrams.

See [[Turing Machines]] for the full treatment.

## String Encodings

Objects (graphs, TMs, programs) are encoded as strings and passed as TM inputs. Notation: ⟨M⟩ = string encoding of TM M; ⟨M, x⟩ = pair encoding.

## The Halting Problem

**HALTS** = { ⟨M⟩ : M is a TM and M(ε) halts } — the canonical undecidable language, and the standard source for undecidability reductions.

**Theorem**: HALTS is undecidable, by diagonalization — assume a decider H, build a TM that consults H about itself and then does the opposite, and derive a contradiction in both cases.

See [[Halting Problem]] for the full statement and proof.

## Turing Reductions

To show L is undecidable: assume for contradiction a decider M_L for L exists, then use M_L to build a decider for HALTS (or another known undecidable language). Since that decider cannot exist, M_L cannot exist.

**Direction**: reduce **FROM** a known undecidable language **TO** L.
- Correct framing: "If I could decide L, I could decide HALTS" → L is undecidable.
- Incorrect (proves nothing about undecidability): "If I could decide HALTS, I could decide L."

**Choice of source language**: HALTS is the standard starting point. Use a different undecidable language (e.g., PCP) if L more closely resembles it.

## Examples of Undecidable Problems

- **HALTS**: the canonical example
- { ⟨M⟩ : |L(M)| = 1 } — TMs accepting exactly one string
- { ⟨M⟩ : M(ε) loops forever }
- **PCP** (Post Correspondence Problem) — string matching problem, undecidable via reduction from HALTS

## See Also

- [[Turing Reductions]]
- [[Halting Problem]]
- [[Safety Problem]]
- [[Turing Machines]]
- [[CSCE 411]]
