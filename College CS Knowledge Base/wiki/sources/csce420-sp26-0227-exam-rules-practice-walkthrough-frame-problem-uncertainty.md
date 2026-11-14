---
title: "CSCE 420 Spring 2026 — 02-27 Exam Rules, Practice Exam Walkthrough, Frame Problem, Uncertainty"
type: source
tags: [csce420, lecture-recording, spring-2026, midterm-rules, practice-exam, frame-axiom, successor-state-axiom, ramification, truth-maintenance, uncertainty, evidence, prior-posterior]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-02-27
deck: slide04, slide05
exam: midterm / final
updated: 2026-09-17
---

Spring 2026 lecture, 49 min. Complete exam-day rules, a **problem-by-problem walkthrough of the midterm practice exam** (revealed to be the actual Spring 2023 exam), the frame problem solved by successor-state axioms, truth maintenance, and the opening of uncertainty. Slides 04:20–35 and 05:1–8.

## Exam-Day Rules (Spring 2026 — confirm yours)

- Bring **TAMU ID**, driver's license, passport, or any official government ID.
- **Closed book.** No phone, calculator, or other equipment.
- **One sheet, US letter, handwritten, both sides.** *"Because I collect and scan all of these with the exam — a different size becomes an issue. If you're unsure, measure the dimensions exactly."* No notebook pages, no gluing two pages. iPad/tablet handwriting may be printed — on both sides of one sheet.
- **Submit your cheat sheet with the exam; write your name on it.**
- **Scratch paper is provided; answers count only on the exam sheet.**
- **50 minutes** — *"we can go over like 10 minutes, there's usually a 20-minute break."* Six minutes per question; *"question 1 won't take more than one minute."* The final is 2 hours.
- **Range**: slides 1, 2, and 3 **through page 99**. The final is **not cumulative**: *"everything after this will be on the final."*

Full scope on [[CSCE 420 Midterm Review]].

## The Practice Exam Is the Spring 2023 Exam

*"This was an actual exam given in 2023 spring."* One sheet, two sides, 10 questions, answers in the provided space. His problem map — the existing [[CSCE 420 Midterm Practice]] page has the worked problems; this is his own gloss:

| # | Topic | His comment |
|---|---|---|
| 1 | Strong AI vs. weak AI | *"pretty high-level, no issue"* |
| 2 | Greedy best-first — can it loop forever? | **"Just follow the algorithm directly"** — node list [A], expand, sort by h, and the answer is obvious |
| 3 | IDS vs. IDA* — both complete, optimal, linear space; which is better in practice? | conceptual |
| 4 | Simulated annealing — how accept/reject depends on ΔE and T | basic |
| 5 | CSP — least-constraining-value heuristic | *"there's value selection and variable selection; be familiar with all of these"* |
| 6 | Minimax — complete and optimal, and **why** | *"The answer is in the recorded video lecture"* (02-02: finite tree; optimal iff opponent optimal) |
| 7 | Alpha-beta — can these two cuts be made, given α/β from above? | see [[Alpha-Beta Pruning]] |
| 8 | Knowledge-based systems — which part is domain-independent? | see [[Knowledge Base Systems]] |
| 9 | DNF and CNF conversion | simple |
| 10 | Propositional resolution proof | — |

*"Of course, the range includes first-order logic, so study what appears on Homework 2: prenex normal form, skolemization, substitution, and unification."* He also said the Canvas midterm-review page needed updating *"from my previous semester"* — confirming it is the same page captured in [[CSCE 420 Fall 2025 — Midterm Review Recording]].

The lecture-recordings page lists topics per recording, so specific content can be found — *"minimax appears in these two lectures."*

## The Frame Problem, Solved

**Frame axiom** (the first, clumsy fix): At(o, x, s) ∧ o ≠ Agent ∧ ¬Holding(o, s) → At(o, x, Result(Go(y,z), s)). *"We are being extra cautious: the object is just there, not held by anyone."* The trouble: *"you have to write all of this for a lot of fluents — it gets pretty extensive."* That is the **representational** frame problem.

The **inferential** frame problem: with F fluents and T steps, checking every fluent every step is **O(F·T)** work; you want **O(E·T)**, where E is the average number of effects per action, *"only checking the fluents actually affected."*

**Successor-state axiom** — the real fix, and *"one important thing to remember: this whole thing is just one logical formula"*:

> Poss(a, s) → [ Fᵢ true in Result(a, s) ⟺ (a made Fᵢ true) ∨ (Fᵢ true in s ∧ a did not make it false) ]

Example: Poss(a, s) → [ At(Agent, y, Result(a, s)) ⟺ a = Go(x, y) ∨ (At(Agent, y, s) ∧ a ≠ Go(y, z)) ]. Note the link back: Go(x,y) being possible already implies Adjacent(x,y).

**Ramification problem** — implicit effects: *"moving while holding something moves that something as well, like the gold."* A more general successor-state axiom handles it; *"too advanced, we'll skip."*

**Axiom size and work**: axioms average A·E/F in size; per step over all fluents gives **O(A·E·T)** — still mostly *"confirming that the fluent has to stay the same, just copying over."* Reorganize with **PosEffect(a, Fᵢ)** and **NegEffect(a, Fᵢ)** facts defined elsewhere, and the update becomes fetch-the-action's-effects: **O(E·T)**. Fluent calculus does better still — not covered. See [[Frame Problem]].

## Truth Maintenance

As exploration adds facts, a new one may contradict an old derived one — *"P was derived; later you find ¬P. Add ¬P and it invalidates the entire thing, and your theorem prover becomes useless."* So **Retract(P)** — *"but other facts may have been derived from P, so there could be a rippling effect. It's not trivial to maintain integrity."* These are **Truth Maintenance Systems**. See [[CSCE 420 Lecture 4 — Planning]].

## Uncertainty — Opening

*"So far everything was clear and fixed. Logic is either true or false; it doesn't make sense to say it's kind of probably true."*

Three reasons FOL fails in real domains: **laziness** (can't list every antecedent for an exception-free rule), **theoretical ignorance** (medicine has no complete theory), **practical ignorance** (even with the theory, *"20 tests at $1,000 each — maybe I don't want to do that"*).

The airport example, with his own story: driving visitors to Easterwood for a flight to Dallas, the entrance was blocked by police — a **bomb threat**; Easterwood is Texas A&M property, so the campus lockdown closed the airport. *"I just had to drive them to Dallas directly."* Worst cases cannot be enumerated: running out of gas, family emergency, a TSA strike. Leaving 1,440 minutes early (24 hours) is safe and absurd.

**Evidence changes belief.** Locked in the classroom for 100 days, P(rain) is a prior guess — say 0.2. *"Someone walks in with a wet umbrella"* → P(rain | umbrella) ≈ 0.95. Prior (unconditional) → **evidence** → posterior (conditional). *"Analogous to whether a sentence is entailed by the KB — the truth value can change when new facts are added."* Blackjack: belief about the dealer busting updates as cards are drawn. Continues 03-02. See [[Uncertainty]].

## See Also

- [[CSCE 420 Spring 2026 — 02-25 Planning]]
- [[CSCE 420 Spring 2026 — 03-02 Probability, Bayes Rule]]
- [[CSCE 420 Midterm Review]]
- [[CSCE 420 Midterm Practice]]
- [[Frame Problem]]
- [[CSCE 420]]
