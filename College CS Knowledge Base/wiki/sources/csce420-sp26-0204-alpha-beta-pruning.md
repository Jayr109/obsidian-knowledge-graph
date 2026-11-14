---
title: "CSCE 420 Spring 2026 — 02-04 Alpha-Beta Pruning"
type: source
tags: [csce420, lecture-recording, spring-2026, alpha-beta, pruning, horizon-effect, evaluation-function, minimax, max-value, min-value]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-02-04
deck: slide02
exam: midterm
updated: 2026-09-17
---

Spring 2026 lecture, 50 min, entirely on alpha-beta: resource limits and the horizon effect, the cut logic derived from first principles, the worked exercise done live with number lines, and the Max-Value/Min-Value functions. Slides 112–125. HW1 due Sunday.

> This is the lecture behind HW2 Problem 2 and the midterm hint *"always use the algorithm."* See [[CSCE 420 Homework 2 — Game Playing, Logic]].

## Resource Limits and the Horizon Effect

With a depth cutoff you need an **evaluation function** — *"it could be as simple as white pieces minus black pieces, but that's not the very best."* Weighted features: f_i(s) = (# white piece X) − (# black piece X), or richer ones like control of the centre. **Exact values do not matter as long as the order of successors is correct.**

**Horizon effect**: the values at the cutoff are *approximations*. A branch that looks promising may hide a much worse position just below the horizon, and vice versa. *"If the approximation may be incorrect, that's the horizon effect."* Quality of the evaluation function is what limits the damage.

## Alpha-Beta From First Principles

He built the alpha cut without any notation first:

MAX explores its first child (a MIN node) → gets **4**. Now MAX *tells* the second MIN child: *"I already have a move where I can get 4."* That child looks at its first leaf and sees **2**. Whatever else it finds, it will return **min(2, ?, ?) ≤ 2**. MAX, choosing between 4 and something ≤ 2, takes 4 regardless. *"There's no need to look at these. You can just cut, and you'll get the same outcome."*

**The variant that does not cut:** if the first leaf had been **7**, the child returns min(7, ?, ?) ≤ 7 — which could still be less than 4 or greater. *"There could be a −10 down here. You have to look."* His summary rule: **you cut once you have found a value that is worse (for the parent) than what the parent already has in mind.**

## Naming and Bookkeeping

- **Alpha cut** happens at a **MIN** node, comparing the returned value against **α** from above. **Beta cut** happens at a **MAX** node, comparing against **β**.
- Every node holds **local** α and β, **inherited from its parent**.
- **From below**: a MAX node updates only **α**; a MIN node updates only **β**. **From above**: both are set.
- **The cut compares against the *unmarked* value** — the one this node does *not* update.

The non-obvious consequence he stressed: α and β *propagate down through many levels*. A cut deep in the tree can be triggered by a value set by a **distant ancestor**, not just the neighbouring branch.

## The Worked Exercise — Method

*"Draw the number line."* At each return, place the returned value and the relevant bound on a line and ask *is this worse, as a min (or max), than the bound?* Worse → cut.

Rules that came out of the walkthrough:
- **You cannot cut against an infinite bound.** *"If you have any non-finite value, you cannot use that for cutting."* Early in the search β = +∞ at MAX nodes, so no beta cut is possible until β has been set.
- Result on the slide tree: **three cuts** — two beta cuts (removing leaves 3 and 6) and one alpha cut removing the entire 30-branch. He nearly made an error mid-way and checked against the answer slide: *"I may have made a mistake"* — the algorithm, not intuition, resolved it.

(The HW2 tree is different and has **four** cuts.)

## Ordering

Swap the order of children and a cut may vanish: *"if there was a −10 node here, you cannot cut. Only when these appear in front can you cut."* With perfect ordering, time is **b^(m/2)** — *"effectively double the depth with the same resources"*; 8-ply chess on modest hardware. Equivalently b^(m/2) = (√b)^m, so chess's 35 becomes an effective branching factor of about **6**. See [[Alpha-Beta Pruning]].

## Max-Value and Min-Value

- α and β arrive **as function arguments** from the parent's call and become **local variables**.
- `v` starts at −∞ (Max-Value) or +∞ (Min-Value).
- **The recursion alternates**: Max-Value calls Min-Value on each child; Min-Value calls Max-Value. *"It's not within the same function, but it alternates between these two."*
- After *every* child returns: check for a cut (`v ≥ β` in Max-Value, `v ≤ α` in Min-Value); if so, **return v immediately**; otherwise update α (or β) and continue.

*"The two functions are exactly identical except: the comparison is against α vs. β, the inequality is flipped, either α or β is updated, and Max-Value ↔ Min-Value."* That symmetry is what to write on the cheat sheet.

## See Also

- [[CSCE 420 Spring 2026 — 02-02 Simulated Annealing, CSP, Game Playing]]
- [[CSCE 420 Spring 2026 — 02-06 Chance Games, Game AI History, Logic Intro]]
- [[Alpha-Beta Pruning]]
- [[Minimax]]
- [[CSCE 420 Homework 2 — Game Playing, Logic]]
- [[CSCE 420]]
