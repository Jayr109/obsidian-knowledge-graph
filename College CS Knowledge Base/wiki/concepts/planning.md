---
title: "Planning"
type: concept
tags: [csce420, planning, actions, goals, state-space]
sources: [csce420-lecture-04-planning]
course: CSCE 420
updated: 2026-09-01
---

**Planning** is the task of coming up with a sequence of actions that will achieve a goal. The lecture's framing is that planning is not a new kind of problem so much as a new demand on **representation**: once you want an arbitrary goal rather than a fixed one, how you describe states and actions becomes the central issue.

## Two Simple Approaches

- **Search-based** — treat action sequences as paths; see [[Search Problem Formulation]]
- **Logic-based** — describe actions as axioms and *deduce* a plan; see [[Situation Calculus]]

> **Representation of states and actions becomes an important issue.** This is the sentence the whole deck elaborates.

## The Limitation That Motivates Situation Calculus

A propositional-logic agent in [[Wumpus World]] can query its KB ("is there a pit in [x,y]?"), add percepts, and decide an action. But two problems appear:

1. **Propositions must be explicit about location** — $Breeze_{x,y}$, $Stench_{x,y}$, $\neg Wumpus_{x,y}$. Every square needs its own set of propositions, so the KB grows with the world.
2. **There is only one goal** — grab the gold. *Can we specify an arbitrary goal and derive a plan?*

Answering yes to the second requires objects, relations, and a way to talk about **states as things** — which is what [[Situation Calculus]] adds.

## Planning Approaches

The deck closes by naming three families:

| Approach | Idea |
|---|---|
| **State-space search** | Forward from the initial state, or backward from the goal |
| **Heuristic search** | Uses the **subgoal independence assumption** — estimate cost by solving subgoals separately |
| **Partial-order planning** | Exploits **problem decomposition**: place two actions in a plan *without* specifying their relative order |

Partial-order planning is the interesting one. A partial order admits several **total order** plans, so the planner commits to ordering only where the problem actually requires it — least commitment. The subgoal independence assumption behind heuristic planning is exactly that: assume subgoals do not interact, which is a **relaxation**, and therefore yields an admissible estimate by the logic in [[Admissible Heuristics]].

## Other Formalisms

- **Event calculus** — fluents hold at *time points* rather than situations; reasoning is over time
- Generalized events (spatiotemporal), processes, intervals
- Formal theories of belief — propositional attitudes, reification

## See Also

- [[Situation Calculus]]
- [[Wumpus World]]
- [[Frame Problem]]
- [[Truth Maintenance Systems]]
- [[CSCE 420]]
