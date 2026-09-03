---
title: "CSCE 420 Lecture 4 — Planning"
type: source
tags: [lecture, csce420, planning, situation-calculus, frame-problem, wumpus-world]
sources: []
course: CSCE 420
updated: 2026-09-01
---

Slide deck 4 of [[CSCE 420]], by [[Yoonsuck Choe]]. 27 slides — the shortest deck of the course. Covers planning, the Wumpus World domain, situation calculus, and the frame problem. Material drawn from Russell & Norvig 7.2, 7.3, 7.7.1 (Wumpus world, frame problem) and 10.4.2 / chapter 11 (situation calculus).

## Structure

| Slides | Section |
|---|---|
| 2–3 | Planning: definition and simple approaches |
| 4–10 | Wumpus World; inference and entailment |
| 11–15 | Situation calculus: situations, fluents, possibility and effect axioms |
| 16–21 | The frame problem and its two forms |
| 22–26 | Other formalisms; truth maintenance; planning approaches |
| 27 | LaTeX overflow artifact — no content |

## The Argument

The deck is a single escalating problem:

1. **Planning needs representation.** Coming up with a sequence of actions to achieve a goal is easy to state; the difficulty is describing states and actions. See [[Planning]].
2. **Propositional logic is not enough.** A propositional [[Wumpus World]] agent needs a separate proposition per square ($Breeze_{x,y}$) and supports only one hard-wired goal — grab the gold. *Can we specify an arbitrary goal and derive a plan?*
3. **[[Situation Calculus]] answers that** by making states into logical terms and actions into functions, so a goal becomes $\exists seq\, At(G_1,[1,1],Result(seq,S_0))$ — planning as theorem proving.
4. **But effect axioms are insufficient**, because they never say what *stays the same*. That is the [[Frame Problem]], and it consumes the rest of the deck.

## Wumpus World as an Entailment Example

The knowledge walkthrough is the deck's best teaching moment. From a stench at [1,2] the agent concludes the wumpus is at [1,3] — by **ruling out** [1,1] (visited) and [2,2] (no stench was detected at the adjacent [2,1]). The conclusion follows from an **absent** percept, which is the kind of inference a knowledge base supports and a reactive agent cannot make.

Entailment is then stated precisely: with three unvisited squares there are $2^3 = 8$ pit configurations, and $KB \models \alpha_1$ ("no pit in [1,2]") while $KB \nvDash \alpha_2$ ("no pit in [2,2]").

## The Frame Problem in Two Forms

- **Representational** — naive frame axioms require $O(AF)$ statements, one per (action, fluent) pair. Solved by **successor-state axioms**, one per *fluent*, using a biconditional that states the complete set of circumstances under which the fluent holds afterward.
- **Inferential** — projecting a $t$-step plan should cost $O(Et)$ in the number of *effects*, not $O(Ft)$ or $O(AEt)$ in the number of fluents. Solved by factoring the axiom through `PosEffect`/`NegEffect` predicates so the engine fetches only the current action's effects.

The **ramification problem** is flagged as remaining: moving while holding something moves that thing too.

## Truth Maintenance

A short but pointed section: if $P$ was derived and later $\neg P$ is found, adding $\neg P$ would invalidate the whole KB, so $P$ must be retracted — carefully, since other facts may depend on it. See [[Truth Maintenance Systems]]. Together with the frame problem, this marks the boundary where classical logic strains, and motivates the move to probability in the next deck.

## Visual-Only Slides

Slides 6 and 7 are the Wumpus World grid diagrams showing knowledge evolving across four board states; the annotations (A, B, G, P, S, W, OK, V) extract as scattered labels without their grid positions, so the figures are not reconstructible from text. Slide 26 is a "google search" placeholder for a Sokoban planning demo. **Slide 27 is a LaTeX artifact** — a "Temporary page!" notice from an unresolved page-count, carrying no course content.

## Pages Created

**New (4)**: [[Planning]], [[Wumpus World]], [[Frame Problem]], [[Truth Maintenance Systems]]

**Reconciled (1)**: [[Situation Calculus]]

## See Also

- [[CSCE 420]]
- [[Yoonsuck Choe]]
- [[Situation Calculus]]
- [[Frame Problem]]
