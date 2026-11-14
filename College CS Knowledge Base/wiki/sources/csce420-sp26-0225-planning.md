---
title: "CSCE 420 Spring 2026 — 02-25 Planning"
type: source
tags: [csce420, lecture-recording, spring-2026, planning, sokoban, wumpus-world, entailment, situation-calculus, fluents, possibility-axiom, effect-axiom, frame-problem]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-02-25
deck: slide04
exam: final
updated: 2026-09-17
---

Spring 2026 lecture, 50 min. Planning from Sokoban through the Wumpus world, entailment by enumeration, why propositional logic does not scale, situation calculus, the two basic axiom types, and the frame problem posed. Slides 04:1–20. Post-midterm material. HW2 due Sunday.

## Sokoban as a Planning Problem

Push-only boxes into goal squares. *"If you push this all the way here, you'll get stuck"* — an irreversible action. *"Each step is a state; in each state you have to make a decision what action to take."* Later levels: *"you have to decide what to do first."* Ordering is the planning problem.

## Wumpus World — Knowledge Evolves

The agent starts knowing **only the rules**. The board walkthrough (also in [[CSCE 420 Fall 2025 — Midterm Review Recording]]) has one point stressed more here: *"It won't be safe to move either way, because there could be a pit. There's no certainty."* After the stench at (1,2) with no breeze, the pit at (2,2) is ruled out **and** the Wumpus at (2,2) is ruled out because no stench was felt at (2,1) — so **Wumpus(1,3) is certain**. All of this goes into the KB as new facts. See [[Wumpus World]].

**The arrow**: no reward for killing the Wumpus, just the scream — and it costs 10 actions' worth. *"You cannot just shoot the arrow around."*

## Entailment by Enumeration

α₁ = no pit in (1,2); α₂ = no pit in (2,2). *"Here I just used human knowledge. How can you mechanically determine this?"* Enumerate the 8 pit configurations over the three frontier squares; keep the 3 consistent with the KB (breeze at (2,1), (1,1) safe). **KB ⊨ α₁** because all 3 lack a pit at (1,2); **KB ⊭ α₂** because one of the 3 has a pit at (2,2). *"KB entails α iff the models of KB are a subset of the models of α."* See [[Logical Consequence]].

## Why Not Propositional Logic?

You cannot write Safe(x,y) with variables — each is a separate atom: **Safe11**, **Breeze21**, … *"You have to create these symbols explicitly, and to describe a rule like 'if breeze then pit nearby' you have to define it for all possible XY combinations. It just blows up massively."* That is the motivation for [[Situation Calculus]].

## Situation Calculus

- **Situations** S₀, S₁, … are identifiers for where you are in the sequence of events. **Result(a, s)** returns the situation after action a in s.
- **Fluents**: predicates whose truth depends on the situation — *"the truth value is kind of fluid."* Alive(agent, S₀) may be true and Alive(agent, S₁) false. Holding(G₁, S₀) false, Holding(G₁, S₁₀) true.
- Some predicates are **stateless**: the Wumpus's age; Gold(G₁) — *"G₁ is gold in S₀, in S₁, and so on. It's not supposed to change."*
- **Sequences**, recursively: Result([], s) = s; **Result([a | seq], s) = Result(seq, Result(a, s))** — apply the first action, then the rest from the resulting situation.
- **Projection**: given a sequence, deduce the outcome. **Planning**: given a goal, find the sequence — ∃seq At(G₁, [1,1], Result(seq, S₀)).

## Possibility and Effect Axioms

His mnemonic: **"possibility appears on the right-hand side; effect appears on the right-hand side"** — i.e. preconditions → Poss(a, s), and Poss(a, s) → what changes in Result(a, s). You cannot get effects unless the action was possible.

| Action | Preconditions (possibility) | Effect |
|---|---|---|
| Go(x, y) | At(Agent, x, s) ∧ Adjacent(x, y) — *"you have to be at x and y has to be next to it"* | At(Agent, y, Result(Go(x,y), s)) |
| Grab(g) | At(Agent, x, s) ∧ At(g, x, s) ∧ **Gold(g)** — *"if g was the Wumpus you cannot grab it, you'll die"* | Holding(g, Result(Grab(g), s)) |
| Release(g) | Holding(g, s) | ¬Holding(g, Result(Release(g), s)) |

*"All of these are in the same situation — make sure the s's match."* See [[Planning]].

## The Frame Problem, Posed

Sequence: Go(1,1 → 1,2), Grab(G₁), Go(1,2 → 1,1). Query: At(G₁, [1,1], Result([a₁,a₂,a₃], S₀))? *"Yes, that's what we normally think. But we cannot deduce it, because G₁ may move around while you move."* Effect axioms say **what changes**, not **what stays the same**. *"When you move, it didn't say anything about whether the gold would move or not."* So the query is **unknown**, not false. The fix — frame axioms — is next lecture. See [[Frame Problem]].

## See Also

- [[CSCE 420 Spring 2026 — 02-23 Cheat Sheet Rules, Prover Demo, Prolog]]
- [[CSCE 420 Spring 2026 — 02-27 Exam Rules, Practice Exam Walkthrough, Frame Problem, Uncertainty]]
- [[CSCE 420 Lecture 4 — Planning]]
- [[Situation Calculus]]
- [[CSCE 420]]
