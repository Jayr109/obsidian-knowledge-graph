---
title: "CSCE 420 Final Exam Practice"
type: source
tags: [csce420, exam, practice, logic, probability, machine-learning, deep-learning]
sources: []
course: CSCE 420
updated: 2026-08-25
---

Practice final for [[CSCE 420]] (`raw/CSCE420_final-practice.pdf`, 2 pages, 10 problems, 100 points). It covers the second half of the course: first-order logic, planning, probabilistic reasoning, and machine learning through deep learning. **No answer key is included** — worked solutions on the linked pages were derived during ingest and are marked as such.

## Problem Index

| # | Pts | Topic | Asked | Wiki page |
|---|---|---|---|---|
| 1 | 15 | [[Resolution]] | Clausify three FOL premises, negate the conclusion, derive False | [[Resolution]] |
| 2 | 10 | [[Situation Calculus]] | Classify two axioms as possibility or effect (no partial credit) | [[Situation Calculus]] |
| 3 | 10 | [[Bayesian Networks]] | Compute $P(A, \neg B, C)$ on a 3-node network | [[Bayesian Networks]] |
| 4 | 5 | [[Bayesian Networks]] | Better node ordering for Cavity / Catch / Toothache | [[Bayesian Networks]] |
| 5 | 10 | [[Decision Tree Learning]] | Split on two attributes, compute both info gains, pick the root test | [[Decision Tree Learning]] |
| 6 | 10 | [[Neural Networks]] | Can 2 hidden units + 1 output reach 100% on a 4×4 grid dataset? | [[Neural Networks]] |
| 7 | 10 | [[Neural Networks]] | Spiral data: raw $(x_1,x_2)$ vs. $(x_1,x_2,x_1^2,x_2^2)$ | [[Neural Networks]] |
| 8 | 10 | [[Self-Organizing Map]] | Which ML paradigm does SOM belong to? | [[Machine Learning Paradigms]] |
| 9 | 10 | [[Deep Learning]] | Match CNN / Deep RL / RNN-Transformer to application areas | [[Deep Learning]] |
| 10 | 10 | [[Deep Q-Network]] | What values does a DQN output given input state $s$? | [[Deep Q-Network]] |

## Answer Summary

- **P1** — Skolemize premise 3 to a constant $C$; negated conclusion becomes $R(w)$. Five clauses reach False in four resolution steps with $\{x/C\}, \{y/C\}, \{w/C\}$.
- **P2** — Axiom 1 (with $Poss$ in the antecedent and a $Result$ term) is the **effect axiom**; axiom 2 (preconditions implying $Poss$) is the **possibility axiom**.
- **P3** — $P(A)\,P(C)\,P(\neg B \mid A,C) = 0.2 \times 0.1 \times 0.6$.
- **P4** — Order **(2) Cavity, Catch, Toothache** — causes before effects.
- **P5** — $Gain(E, Attr1) = 2/3$; $Gain(E, Attr2) = 0$. **Attr 1** is tested first.
- **P6** — **No.** Three of the x-points are pairwise blocked by o-points at their midpoints, so no two of them can share a half-plane; two hidden units cannot separate three mutually conflicting groups.
- **P7** — **Second** case needs the much smaller network; squared features let one unit draw a conic. Part (2)'s intended Yes/No is ambiguous as worded — see the page.
- **P8** — **(2) Unsupervised Learning.** No target or reward appears in the update rule.
- **P9** — CNN → **(C)** computer vision; Deep RL → **(B)** robotics / autonomous driving; RNN/Transformer → **(A)** natural language processing.
- **P10** — One **Q-value per available action**, $Q(s,a)$, each estimating expected cumulative discounted future reward; the agent takes the argmax.

## Notable Framing

- Problem 1's two hints — negate the conclusion, don't forget skolemization — are both load-bearing, and the problem demands all substitutions be shown.
- Problem 5's hint that entropies come out to 0 or 1 means no logarithms need evaluating.
- Problem 8's hint supplies the SOM learning equation itself, which is sufficient to answer the question without knowing what a SOM is — the absence of a target term is the whole argument.
- Problems 3 and 5 both waive arithmetic; the formula and setup carry the credit.

## Coverage Gap

The two practice exams together do not touch uninformed search (BFS/DFS/uniform-cost), propositional model checking, Markov decision processes, or hidden Markov models, all of which appear in R&N and may still be examinable.

## See Also

- [[CSCE 420]]
- [[CSCE 420 Midterm Practice]]
- [[Machine Learning Paradigms]]
- [[Deep Learning]]
