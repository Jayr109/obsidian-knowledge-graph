---
title: "CSCE 420 Lecture 5 — Uncertainty and Probabilistic Reasoning"
type: source
tags: [lecture, csce420, probability, bayes, belief-networks, decision-theory]
sources: []
course: CSCE 420
updated: 2026-09-01
---

Slide deck 5 of [[CSCE 420]], by [[Yoonsuck Choe]]. 67 slides. Covers uncertainty, decision theory, probability fundamentals, Bayes' rule, Bayesian updating, and belief networks.

## Structure

| Slides | Section |
|---|---|
| 2–6 | Uncertainty; why FOL fails; prior vs. posterior |
| 7–12 | Decision theory; maximum expected utility |
| 13–21 | Probability basics: notation, axioms, joint distributions |
| 22–32 | Bayes' rule; the disease example |
| 33–38 | Diagnostic vs. causal knowledge; hypothesis ratios; object recognition |
| 39–44 | Bayesian updating and conditional independence |
| 45–55 | Belief networks: semantics and the chain-rule factorization |
| 56–63 | Construction algorithm; node ordering; causal models |
| 64–67 | Probabilistic inference; knowledge engineering |

## Why This Lecture Exists

It is the answer to where [[Planning|the logic unit]] ran out. First-order logic fails in uncertain domains for three distinct reasons, given for medical diagnosis:

- **Laziness** — cannot list all antecedents for an exceptionless rule
- **Theoretical ignorance** — medicine has no complete theory
- **Practical ignorance** — cannot run every test

Only the first could be fixed with more effort. The agent's knowledge can at best supply a **degree of belief** — see [[Uncertainty]].

## The Two Results Worth Remembering

**The base-rate example.** A 99%-accurate test for a disease affecting 1 in 10,000 yields $P(D|T) \approx 1\%$. Testing 10,000 people produces about **100 false positives and one true positive**, and that ratio is the answer. Full working on [[Bayes Rule]].

**The compactness result.** A belief network with $n$ nodes and $k$ parents each needs $n2^k$ CPT entries against the full joint table's $2^n$. This is the entire justification for the representation — and it is destroyed by bad node ordering, which can force a network needing as many entries as the full table. See [[Belief Network Construction]].

## Other Results

- **Causal knowledge is stable, diagnostic knowledge is not.** $P(Symptom|Disease)$ stays fixed while $P(Disease|Symptom)$ fluctuates with prevalence — so a directly-measured diagnostic probability goes stale during an epidemic, whereas recomputing through Bayes' rule stays robust. This is the practical argument for the rule.
- **Comparing two hypotheses cancels $P(E)$**, the awkward term: $\frac{P(C_1|E)}{P(C_2|E)} = \frac{P(E|C_1)P(C_1)}{P(E|C_2)P(C_2)}$.
- **Graphics is one-to-one; vision is one-to-many.** Why $P(Image|Object)$ is easier than $P(Object|Image)$, and why vision can be done by running graphics forward and comparing ratios.
- **Bayesian updating** turns evidence combination into multiplication: $P(Z|X,Y) = \alpha P(Z)P(X|Z)P(Y|Z)$ under [[Conditional Independence]].
- **Explaining away** — $P(Cause|Effect) \gg P(Cause|Effect \land OtherCause)$. Conditioning on a common effect *creates* dependence between independent causes. See [[Probabilistic Inference]].

## A Discrepancy in the Slides

The decision-theory worked example (slides 11–12) lists Action 2's utility as **10000** in the table but computes with **1000**. As computed, Action 3 wins with expected utility 3.995; with 10000 the answer would be Action 2 at 10.0. The stated conclusion follows from the 1000 figure. Noted on [[Decision Theory]] rather than silently normalized, since either value could be the intended one.

## Visual-Only Slides

The conditional-probability Venn diagram (17), the $P(T)$ decomposition diagram (29), the object-recognition hexagon/cube figures (36–38), the belief-network graphs (47–54, 59–61), and the query-support diagram (65) are figures whose structure is not recoverable from the text layer. The burglary network's topology and CPT values *are* recoverable and have been captured on [[Bayesian Networks]].

## Pages Created

**New (7)**: [[Uncertainty]], [[Decision Theory]], [[Probability Basics]], [[Bayes Rule]], [[Conditional Independence]], [[Belief Network Construction]], [[Probabilistic Inference]]

**Reconciled (1)**: [[Bayesian Networks]]

## See Also

- [[CSCE 420]]
- [[Yoonsuck Choe]]
- [[Bayesian Networks]]
- [[Bayes Rule]]
- [[CSCE 420 Final Exam Practice]]
