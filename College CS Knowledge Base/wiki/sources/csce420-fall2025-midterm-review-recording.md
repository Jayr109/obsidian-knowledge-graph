---
title: "CSCE 420 Fall 2025 — Midterm Review Recording"
type: source
tags: [csce420, recording, video, midterm, review, prolog, wumpus-world, entailment, fall-2025]
sources: []
course: CSCE 420
semester: Fall 2025
exam: midterm
updated: 2026-09-17
---

A 50-minute class recording from the **Fall 2025** offering — the Wednesday before that semester's midterm. Archived as `raw/CSCE420_Fall2025_Midterm_Review_Recording.mp4` with its caption track. The recording is a screen capture with the instructor's Canvas open, which is why the Canvas "Midterm Review" page could be transcribed from it frame by frame.

> **Semester note.** This is not the user's section. Dates, deadlines, and the "see you Friday" are Fall 2025. The *content* — scope, hints, Prolog demo, Wumpus-world walkthrough — is the same material taught every offering.

## Three Parts

| Time | Segment |
|---|---|
| 0:00–5:35 | Walkthrough of the Canvas Midterm Review page, with hints |
| 5:35–22:30 | Prolog demo — tau-Prolog in the browser, GProlog on the Unix machines, unification queries |
| 22:30–49:30 | Start of Planning: the Wumpus world and entailment |

## Part 1 — The Midterm Review Walkthrough

Fully captured on [[CSCE 420 Midterm Review]]: the complete learning-objectives list per deck, plus every spoken hint. The three that matter most: copy the alpha-beta algorithm onto the cheat sheet; know simulated annealing's accept/reject rule; run a propositional resolution proof end to end. FOL stops at unification.

*"I suggest that you carefully watch the recording from today before you start preparing for the midterm exam, because I've given you some very suggestive hints."*

## Part 2 — Prolog Demo

Two ways to run Prolog:

- **GProlog** on the department Unix machines — `[dating].` loads a program named `dating.pl`; `Ctrl-D` exits.
- **tau-Prolog** at tauprolog.org → sandbox, in the browser. Caveat: no HTTPS, and *"if you wrote your program directly in here, then left the webpage, all your effort would vanish"* — write in a text editor and paste, then re-consult.

### Syntax rules he stated

- Everything is **lowercase** — predicates, constants — **except variables, which are uppercase** (`X`, `Y`).
- `:-` reads as **if**. `animal(X) :- man(X).` corresponds to `forall x, man(x) -> animal(x)`.
- **Comma means AND.** `couple(X,Y) :- loves(X,Y), loves(Y,X).`
- **Facts at the top, rules below.** A program is facts plus rules.
- `write(...)` produces a printed side effect.

### The contiguity gotcha

GProlog rejects clauses of the same predicate that are separated by a different predicate: entering `dog(snoopy). man(socrates). dog(fido).` produces *"discontiguous predicate — clause ignored"*, and `dog(fido)` is silently dropped, so `mortal(X)` then finds only Socrates and Snoopy. Keep all clauses of one predicate together. *"This is relevant to your next homework."*

### The couple example — why mutuality needs two literals

`loves(john,jane). loves(jane,john). loves(jane,mark).` Defining `couple(X,Y) :- loves(X,Y).` is wrong — it is not mutual. With both directions required, `couple(john,X)` returns `jane`; `couple(mark,X)` returns **no**, because Jane loves Mark but Mark does not love Jane back. Queries with a variable retrieve all bindings on `;` — this is [[Answer Extraction]] built into the language.

### Unification at the prompt

Prolog's `=` performs [[Unification]] and reports the unifier:

| Query | Result | Why |
|---|---|---|
| `p(X) = p(john).` | `X = john` | disagreement set {X, john} |
| `p(X,Y) = p(g(Z),Z).` | `X = g(Y), Z = Y` | first D = {X, g(Z)}; second D = {Y, Z}; compose |
| `p(X) = p(f(X)).` | *"cannot display cyclic term"* | occurs check — X inside its own binding |
| `p(a) = p(b).` | `no` | two distinct constants never unify |

The worked reasoning for the second row is the same disagreement-set procedure as HW2's unification problems — see [[CSCE 420 Homework 2 — Game Playing, Logic]].

## Part 3 — Planning: The Wumpus World

Covered in the KB at [[Wumpus World]] and [[CSCE 420 Lecture 4 — Planning]]; the recording adds the instructor's step-by-step belief-state walkthrough.

**The setup**: a grid with a Wumpus (enter its square and die), pits (fall and die), and gold. Percepts in neighbouring squares: *stench* near the Wumpus, *breeze* near a pit, *glitter* on the gold square, *bump* on walls, *scream* when an arrow kills the Wumpus. Rewards: +1000 gold, −1000 death, −1 per action, −10 to fire the arrow.

**The walkthrough**, agent starting at (1,1):

1. (1,1): no breeze, no stench → neighbours (1,2) and (2,1) marked **OK**.
2. Move to (2,1): **breeze** → pit possibly in (2,2) or (3,1). (1,1) already OK, so ruled out.
3. Back to (1,1), up to (1,2): **stench, no breeze**. No breeze from (1,2) rules out a pit in (2,2) → so the pit **must** be (3,1) — mark `P!`. Stench means Wumpus in (1,3), (2,2), or (1,1). (1,1) is visited, so no. (2,2)? No stench was felt at (2,1), which neighbours (2,2) → ruled out. So Wumpus **is** at (1,3) — mark `W!`.
4. (2,2) is now known safe; from there, no percepts; go up → gold.

The point of the exercise: everything after step 1 is **inference from the absence of percepts** as much as from their presence.

### Entailment, made concrete

Treat the Wumpus rules as a knowledge base, and add facts as you explore: `visited(1,1)`, `visited(2,1)`, `breeze(2,1)`, tentative `pit?(2,2)`, `pit?(3,1)`. Then ask whether a statement is a [[Logical Consequence]] of the KB.

With (1,1) and (2,1) visited, the three unvisited neighbours (1,2), (2,2), (3,1) give **2³ = 8 possible pit configurations**. The breeze at (2,1) and safety of (1,1) leave **three** consistent with the KB: pit in (2,2) only, pit in (3,1) only, or both.

- **α₁ = "no pit in (1,2)"**: every one of the three KB-consistent worlds has no pit in (1,2). Models(KB) ⊆ Models(α₁), so **KB ⊨ α₁**.
- **α₂ = "no pit in (2,2)"**: one of the three KB-consistent worlds *does* have a pit in (2,2). Models(KB) ⊄ Models(α₂), so **KB ⊭ α₂**.

The definition he drew: **KB entails α iff every model that satisfies KB also satisfies α** — set containment on the space of interpretations. This is the semantic definition that [[Resolution]] implements syntactically.

## See Also

- [[CSCE 420 Midterm Review]]
- [[Prolog]]
- [[Unification]]
- [[Wumpus World]]
- [[Logical Consequence]]
- [[CSCE 420 Lecture 4 — Planning]]
- [[CSCE 420]]
