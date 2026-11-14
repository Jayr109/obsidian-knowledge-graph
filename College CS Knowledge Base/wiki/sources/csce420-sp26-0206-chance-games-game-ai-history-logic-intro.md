---
title: "CSCE 420 Spring 2026 — 02-06 Chance Games, Game AI History, Logic Intro"
type: source
tags: [csce420, lecture-recording, spring-2026, alpha-beta, move-ordering, expectiminimax, backgammon, othello, alphago, hw2, knowledge-representation]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-02-06
deck: slide02, slide03
exam: midterm
updated: 2026-09-17
---

Spring 2026 lecture, 50 min. Alpha-beta recap with the move-ordering demonstration, games of chance, the game-AI history slides with several stories not on them, a preview of HW2, and the first slides of the logic deck. Slides 02:121–138 and 03:1–5.

## HW1 Coding Tip (asked at the start)

*"Copy and paste the DFS code from above to the bottom and use the node class."* Change the adjacency matrix and the heuristic table to match the HW graph; replace `expand` with `node.expand`; pass a newly instantiated node as the DFS argument. **Get DFS working first** by changing only `goal_p` and `expand`. See [[CSCE 420 Homework 1 — Search]].

## Alpha-Beta: Mark the Value You Update

His board convention, worth adopting for exams: at a **MAX node, mark α** — that is the value updated from below; the cut check is against **β**. At a **MIN node, mark β**; the cut check is against **α**. *"The cut decision is made against the other value, the one that is not updated."* Both are passed to children as arguments and become local variables there.

### Move ordering, demonstrated

A MIN node with children returning 2, 5, 10, 2 and α = 4 from above:

- **2 first**: v = 2 ≤ α = 4 → **cut immediately**; the other three subtrees are never touched.
- **5, 10 first**: 4 ≥ 5? No. 4 ≥ 10? No. You must explore everything below 5 and 10 — the cut only arrives when the 2 finally appears.

*"You want the smaller values to appear first at a MIN node, because they're compared to the best MAX. If you're a MAX node, sort in the reverse order."* Same subtrees, different order, entirely different work. See [[Alpha-Beta Pruning]].

## Games of Chance

**Think of (opponent's move + dice roll) as one unit.** The chance layer knows the move made and the dice outcome, and decides on that basis.

Where the leaf-level values are known, MAX and MIN nodes work as before. The chance node is the new thing: *"You can just say, I'll average that — that doesn't really work,"* because the dice may not be fair (he posited outcomes at 1/2, 1/6, …). The value is the **expected value**: Σ P(outcome) × value(outcome). He then walked the formal Expectiminimax recurrence over Result(s, a) for MAX/MIN and Result(s, r) for chance.

**Backgammon rules**, since most students had not played: roll two dice; enter pieces from off-board or advance pieces on it; the two dice may move two pieces or one piece by their sum; landing on a lone opposing piece captures it.

Two design consequences: **scale now matters** — *"a very small probability with a very, very high value gives a high expected value"* — where minimax needed only order; and complexity is **b^m · n^m** for n distinct dice outcomes. Pruning *"can be done if you are careful."* See [[Expectimax]].

## Game AI History — What He Added to the Slides

- Samuel's 1952 checkers program ran in 10 KB — *"actually a huge amount of memory at that time."*
- Deep Blue vs. Kasparov, 1997: *"This was when I was in graduate school."* The famous photo shows a mixed crowd — some amazed, some shocked and sad.
- **Othello / Reversi** played live on the board: place a piece to flank a contiguous line of opposing pieces and flip them; **corners are decisive** because a corner piece can never be flipped and anchors long captures.
- **Go**: 19×19 = 361 branching factor — *"you cannot solve this using the same search strategy, even with pruning."* Ing Chang-Ki, a Taiwanese businessman, funded a prize in the early 1990s that could be won by beating a 12-year-old amateur; nobody did.
- **AlphaGo 2016** happened during one of his AI classes. Lee Sedol *"was the last human to have beaten AlphaGo and its descendants for many years — he won one match, almost a miracle."*
- **Then an amateur beat AlphaGo's descendants.** Kellin Pelrine, using a strategy found by *another AI* that probed the Go engines for blind spots: build a large loop of stones around the board that the engine fails to perceive as a threat. *"How to beat superhuman Go AI — the YouTube is very interesting."*
- AlphaZero (chess, shogi, Go, knows the rules), **MuZero** (learns without the rules), AlphaStar (StarCraft II, with visualizations of its learned internal map). See [[Game AI Milestones]].

## HW2 Preview

Part 1 (minimax, alpha-beta by hand, alpha-beta in code) is doable now; the logic parts come later. **On the Spring 2026 tree there were 5 cuts** — *"if you get fewer or more than 5, there's some error."* The Fall 2026 sheet says **4** on its tree; do not carry the 5 over. Counting rule: one cut per cut decision, regardless of how many branches it removes.

Coding: *"The most important thing is that alpha and beta should be local variables within the function, distinct from whatever is passed as the argument."* Add a new cell below the provided minimax and follow the algorithm slide almost exactly. See [[CSCE 420 Homework 2 — Game Playing, Logic]].

## Logic — Opening

*"Humans can do theorem proving. The focus here is that we want to automate that. That's where AI comes in."* Two traditional representation classes: **logic** (first-order predicate calculus; propositional logic is *"a very limited form, but we'll use it for inspiration"*) and **frames** — *"similar to objects in an object-oriented language, or a knowledge graph."* See [[Knowledge Representation]].

## See Also

- [[CSCE 420 Spring 2026 — 02-04 Alpha-Beta Pruning]]
- [[CSCE 420 Spring 2026 — 02-09 Knowledge Bases, Propositional Logic]]
- [[Expectimax]]
- [[Game AI Milestones]]
- [[CSCE 420]]
