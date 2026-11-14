---
title: "CSCE 420 Spring 2026 — 03-16 Belief Network Inference"
type: source
tags: [csce420, lecture-recording, spring-2026, belief-networks, cpt, joint-factorization, network-construction, node-ordering, intercausal-inference, explaining-away]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-03-16
deck: slide05
exam: final
updated: 2026-09-17
---

Spring 2026 lecture, 41 min, first day after spring break. The belief-network semantics, the joint-probability factorization derived and worked, the construction algorithm and why node ordering matters, and the four kinds of inference. Slides 05:48–67. Post-midterm; exams were returned.

## Reading a CPT

For Alarm with parents Burglary and Earthquake: each **row** of parent values gives P(A | B, E) and P(¬A | B, E), which **sum to 1 across the row** — *"the columns don't add up to 1; you have to add across the row."* So the table only needs one column; the ¬ column is implicit. Root nodes carry just a prior: P(B) = 0.001, P(E) = 0.002. Leaves: P(J | A) = 0.9, P(J | ¬A) = 0.05 — *"that's a false alarm by John"*; P(M | A) = 0.7.

## Two Semantics of One Network

*"Semantics in logic was true or false. Semantics in belief networks is: what is the probability value?"*

1. **Quantitative** — the network **is** the full joint distribution: 2⁵ = 32 rows summing to 1.
2. **Qualitative** — the **conditional-independence structure**: JohnCalls depends directly on Alarm and on nothing else.

## The Factorization, Derived

**P(x₁, …, xₙ) = Πᵢ P(xᵢ | Parents(Xᵢ))**

Derivation: apply P(A ∧ B) = P(A|B) P(B) repeatedly — peel off xₙ given everything else, then xₙ₋₁ given the rest, down to P(x₁). That gives the chain rule with **all** predecessors in each condition. Then **conditional independence** shrinks each condition to just the parents. *"That's when conditional independence comes in."*

**Worked**: P(J, M, A, ¬B, ¬E) = P(J|A) · P(M|A) · P(A|¬B,¬E) · P(¬B) · P(¬E) = **0.9 × 0.7 × 0.001 × 0.999 × 0.998**. Every factor is a table lookup, using the implicit ¬ columns for 0.999 and 0.998. *"You can compute any arbitrary combination of Boolean values just using this network."* See [[Bayesian Networks]].

## Independence vs. Conditional Independence

Plain independence: P(X ∧ Z) = P(X)P(Z), i.e. P(X|Z) = P(X). Conditional: P(X | Y, Z) = P(X | Y) — *"you need Y to be able to declare X independent of Z."*

Story: Mary is **instructed to respond only to the alarm** — not to earthquakes, not to burglaries. So P(M | J, A, E, B) = P(M | A). But **without** the alarm known, P(M | J) ≠ P(M): *"You're sitting in your office thinking, what's the chance Mary will call? Pretty low. Then John calls — hmm, maybe Mary will call too. It goes up."* Once you know the alarm state, John's call adds nothing.

## Construction Algorithm

Choose an **ordering** of the variables; add them one at a time; for each new node, choose parents **among nodes already in the network** such that P(new | parents) = P(new | all existing); write its CPT.

**Why it works**: *"You can only point an arrow from nodes that already exist to the newly added one. Newly added nodes cannot point backward."* So the result is **acyclic** by construction, and the probability axioms cannot be violated.

**Compactness**: n nodes with ≤ k parents each need **n · 2ᵏ** CPT entries versus **2ⁿ** for the full joint. *"n = 10, k = 3: 80 versus 1024. Linear in n versus exponential in n — and usually k ≪ n."*

### Ordering matters — worked badly on purpose

Order (M, J, A, B, E): adding J after M — *"John will call me? Pretty low. After Mary called? Higher."* So J depends on M → arrow. Adding A needs arrows from both. Result: a tangled network. Order (M, J, E, B, A): *"burglary depends on all three existing ones, and alarm on all four"* — CPT sizes approach the full joint.

*"Regardless of the ordering, if the tables are correct, they all represent the **same** joint probability. But the correctly ordered network is much more convenient and actually represents the conditional independence."*

**Strategy**: **follow the causal order** — a node that directly influences others is added first. Alarm before John and Mary; Burglary and Earthquake before Alarm. Benefits: CPTs are easier to specify, smaller, and the network is easier to reason about.

## Four Kinds of Inference

| Kind | Direction | Example |
|---|---|---|
| **Causal** | cause → effect | P(symptom \| disease) — *"mechanistic, easier"* |
| **Diagnostic** | effect → cause | P(disease \| symptom) — *"the more difficult one"* |
| **Intercausal** | between causes of a shared effect | see below |
| **Mixed** | combine causal and evidential support | P(X \| parents' evidence, children's evidence) |

**Intercausal inference — explaining away.** You have a fever; P(COVID | fever) is some value. Then you learn you also have an **allergy**, another cause of fever. *"This value might actually go down, because the cause you just learned about explains the effect."* Two causes of one common effect compete. He did not use the phrase "explaining away," but that is the standard name.

Singly connected graphs allow efficient exact computation of arbitrary conditionals — *"we won't go into much detail."* Uses beyond inference: decision-theoretic action choice, deciding whether more variables are needed, **sensitivity analysis** (which CPT entries matter most, then refine those), and explaining results.

## See Also

- [[CSCE 420 Spring 2026 — 03-04 Midterm Review, Bayesian Updating, Belief Networks]]
- [[CSCE 420 Spring 2026 — 03-18 HW3 Walkthrough, Machine Learning Intro]]
- [[Bayesian Networks]]
- [[CSCE 420 Lecture 5 — Uncertainty and Probabilistic Reasoning]]
- [[CSCE 420]]
