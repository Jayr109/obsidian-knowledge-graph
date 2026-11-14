---
title: "Halting Problem"
type: concept
tags: [halting-problem, undecidability, diagonalization, turing-machines, computability]
sources: [lecture-4-decidability-and-undecidability, lecture-5-undecidability-reductions]
course: CSCE 411
updated: 2026-08-25
---

The Halting Problem is the canonical undecidable language: no [[Turing Machines|Turing machine]] can decide, for an arbitrary program, whether that program halts. It is the standard starting point for undecidability proofs, since nearly every other undecidability result is established by [[Turing Reductions|Turing-reducing]] HALTS to the language in question.

## Definition

```
HALTS = { ⟨M⟩ : M is a TM and M(ε) halts }
```

where ⟨M⟩ denotes the string encoding of TM M. A decider for HALTS would take any program's source and report — always terminating — whether that program runs forever.

## Why It Matters

A decider for HALTS would allow:

- Testing any program for infinite loops
- Deciding all mathematical theorems, in principle (search for a proof; halt when found)

The second consequence is the reason the result is foundational rather than merely a curiosity about programs.

## Theorem: HALTS Is Undecidable

**Proof** (diagonalization / contradiction). Assume a decider H for HALTS exists. Construct TM D:

```
D(⟨M⟩):
  if H(⟨M, M⟩) accepts:   // H says M(M) halts
    loop forever
  else:                    // H says M(M) loops
    accept
```

Run D on its own encoding ⟨D⟩:

- If D(⟨D⟩) **halts** → H says D(D) halts → D loops forever. Contradiction.
- If D(⟨D⟩) **loops** → H says D(D) loops → D accepts, i.e. halts. Contradiction.

Both cases contradict, so H cannot exist. ∎

The construction is *diagonal*: D is built specifically to disagree with H on D's own input, so no single H can be correct on every program.

## Use as a Reduction Source

To prove a language L undecidable, assume a decider for L and use it to build a decider for HALTS.

**Direction matters** — reduce **from** HALTS **to** L:

- Correct: "If I could decide L, I could decide HALTS" → L is undecidable.
- Incorrect (proves nothing): "If I could decide HALTS, I could decide L."

HALTS is the default source language. Use a different undecidable language (e.g. PCP) when L more closely resembles it. See [[Turing Reductions]] for the full proof template.

## Related Undecidable Languages

- { ⟨M⟩ : |L(M)| = 1 } — TMs accepting exactly one string
- { ⟨M⟩ : M(ε) loops forever } — the complement flavor of HALTS
- **PCP** (Post Correspondence Problem) — undecidable via reduction from HALTS
- **The safety problem in computer security** — whether a protection system can ever leak a given right. Undecidable by reduction from HALTS; see [[Safety Problem]].

## See Also

- [[Decidability and Undecidability]]
- [[Safety Problem]]
- [[Turing Machines]]
- [[Turing Reductions]]
- [[CSCE 411]]
