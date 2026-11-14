---
title: "CSCE 420 Midterm Practice"
type: source
tags: [csce420, exam, practice, search, games, logic]
sources: []
course: CSCE 420
exam: midterm
updated: 2026-09-13
---

Practice midterm for [[CSCE 420]] (`raw/CSCE420_midterm-practice.pdf`, 2 pages, 10 problems × 10 points). It covers the first half of the course: philosophy, search, games, and logic. **No answer key is included** — worked solutions on the linked pages were derived during ingest and are marked as such.

## Problem Index

| # | Topic | Asked | Wiki page |
|---|---|---|---|
| 1 | [[Strong AI and Weak AI]] | Classify the "thought, consciousness, emotions" definition; has ChatGPT reached it? (open-ended) | [[Strong AI and Weak AI]] |
| 2 | [[A* Search]] vs [[IDA*]] | Which nodes stay in memory for each, given a labeled tree with an f-contour | [[A* Search]] |
| 3 | [[Simulated Annealing]] | For $\Delta E > 0$, which $\Delta E$ and $T$ raise the acceptance probability | [[Simulated Annealing]] |
| 4 | [[Constraint Satisfaction Problems]] | Give an example of the least constraining value heuristic on a 4-region map | [[Constraint Satisfaction Problems]] |
| 5 | [[Expectimax]] | Value of the second chance node in a MAX/chance/MIN tree, $p=\frac13$ | [[Expectimax]] |
| 6 | [[Alpha-Beta Pruning]] | Which of two marked cuts is possible, with $\alpha=-\infty$, $\beta=\infty$ at the root | [[Alpha-Beta Pruning]] |
| 7 | [[Logical Inference]] | Why domain independence of the inference engine is both good and bad | [[Logical Inference]] |
| 8 | [[First-Order Logic]] | Why $\forall x \exists y\, Loves(x,y) \not\equiv \exists y \forall x\, Loves(x,y)$, via skolemization | [[First-Order Logic]] |
| 9 | [[Unification]] | Unify two predicate sets or show they clash | [[Unification]] |
| 10 | [[Resolution]] | Propositional resolution refutation from three premises | [[Resolution]] |

## Answer Summary

- **P1** — Strong AI. Part 2 is explicitly open-ended.
- **P2** — A\* holds the explored set plus the whole frontier (A, B, C, D, E, F, G, H, I — everything inside and on the contour); IDA\* holds only the current call stack, the path A → C.
- **P3** — **Lower** $\Delta E$, **higher** $T$. Read directly off $P = e^{-\Delta E/T}$.
- **P4** — With $v_1 = $ Red and $v_2 = $ Green, LCV assigns $v_4 = $ **Red**; Blue would exhaust $v_3$'s last legal value. Note $v_1$ and $v_4$ are not adjacent — the problem's warning to "read the variable number carefully."
- **P5** — $\frac13\min(7,6,9) + \frac13(3) + \frac13(9)$.
- **P6** — **Cut #1 only.** Cut #2 sits at a node whose $\beta$ is still $+\infty$, so no finite $\alpha$ can trigger it.
- **P7** — Bad for efficiency (huge branching in clause generation, no domain knowledge to prune); good for applicability (one engine, any KB).
- **P8** — Skolemize: $Loves(x, f(x))$ vs $Loves(x, A)$. Function vs. constant is the dependency difference.
- **P9** — Set 1 is **not** unifiable ($g$ vs $f$ clash forced by the repeated variable $x$). Set 2 unifies with $\{x/f(A), y/A, z/f(A)\}$ giving $P(f(A), A, g(f(A)))$.
- **P10** — Premise (2) splits into two clauses; with the negated conclusion $Q$ and $\neg S$, resolution reaches False in six steps.

## Notable Framing

- Problem 10's caution — *"Make sure that each clause does not include ∧. If it does, your setup is incorrect"* — flags the CNF-splitting step as the intended trap.
- Problems 5 and 6 both say the formula or the reasoning is the answer; arithmetic is not required.
- Problem 6's hint, "check if cut comparison is between finite values or not," is the entire solution method.

## See Also

- [[CSCE 420]]
- [[CSCE 420 Final Exam Practice]]
- [[Adversarial Search]]
- [[Heuristic Search]]
- [[Minimax]]
- [[Local Search]]
