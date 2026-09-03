---
title: "Truth Maintenance Systems"
type: concept
tags: [csce420, tms, belief-revision, retraction, nonmonotonic]
sources: [csce420-lecture-04-planning]
course: CSCE 420
updated: 2026-09-01
---

New facts inferred from a knowledge base can turn out to be wrong. A **truth maintenance system (TMS)** manages the consequences of taking something back.

## The Problem

Suppose $P$ was derived in the KB, and later $\neg P$ is discovered.

- Simply **adding $\neg P$ invalidates the entire KB** — a contradiction lets anything be proved, exactly the caveat in [[Logical Consequence]].
- So $P$ must be **removed**: $\text{Retract}(KB, P)$.
- But **care is needed**: other facts may have been *derived from* $P$, and those derivations are now unsupported.

## Why It Is Hard

Retraction is not deletion of one sentence. It is deletion of one sentence plus everything that depended on it, transitively — and a fact may have *multiple* justifications, only some of which passed through $P$. Removing it wholesale would discard conclusions that remain validly supported.

A TMS tracks these dependency structures so that beliefs can be withdrawn and restored coherently.

## The Broader Significance

This is where the course's logical machinery meets its limits. Classical logic is **monotonic** — adding premises never invalidates a conclusion. Real agents revise beliefs constantly, which is non-monotonic, and the [[Frame Problem]] plus truth maintenance are two faces of the same difficulty: **logic describes static truth well and change badly**.

The alternative response is to abandon crisp truth values and represent degrees of belief instead — the move to [[Uncertainty]] and [[Bayesian Networks]] in the following lecture.

## See Also

- [[Planning]]
- [[Frame Problem]]
- [[Logical Consequence]]
- [[Uncertainty]]
- [[CSCE 420]]
