---
title: "Inference Rules"
type: concept
tags: [csce420, modus-ponens, resolution, unit-resolution, inference]
sources: [csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

An inference rule licenses deriving a new sentence from existing ones. The lecture's notation

$$\frac{P,\; Q}{R} \quad\text{means}\quad (P \land Q) \rightarrow R$$

— given sentences $P$ and $Q$, you may generate $R$.

## The Three Rules

| Rule | Form | Reading |
|---|---|---|
| **Modus Ponens** | $\dfrac{F \rightarrow G,\; F}{G}$ | If $F$ implies $G$ and $F$ holds, conclude $G$ |
| **Unit Resolution** | $\dfrac{F \lor G,\; \neg G}{F}$ | Either $F$ or $G$; not $G$; so $F$ |
| **Resolution** | $\dfrac{F \lor G,\; \neg G \lor H}{F \lor H}$ | Cancel the complementary pair |

Resolution has an equivalent implication form worth seeing, since it shows the rule is transitivity in disguise:

$$\frac{\neg F \rightarrow G,\; G \rightarrow H}{\neg F \rightarrow H}$$

## The Relationship Among Them

Unit resolution is the special case of resolution where one clause is a single literal ($H$ absent). Modus ponens is resolution in implication clothing: rewrite $F \rightarrow G$ as $\neg F \lor G$, resolve against $F$, and $G$ remains.

**So resolution subsumes the others** — which is why [[Resolution]] alone suffices as a complete inference procedure, and why an automated theorem prover needs only one rule rather than a catalogue.

## See Also

- [[Propositional Logic]]
- [[Resolution]]
- [[Logical Consequence]]
- [[Forward and Backward Chaining]]
- [[CSCE 420]]
