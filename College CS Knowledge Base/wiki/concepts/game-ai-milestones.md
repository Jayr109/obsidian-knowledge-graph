---
title: "Game AI Milestones"
type: concept
tags: [csce420, history, deep-blue, alphago, alphazero, muzero]
sources: [csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

The lecture closes the search unit with the historical record of AI game playing — a useful arc because it tracks the shift from **search** to **learning** as the dominant technique.

## Classical Era: Search and Evaluation

| Year | System | Achievement |
|---|---|---|
| 1952 | Samuel's checkers program | Ran on 10 Kbyte |
| 1992 | Tesauro's backgammon neural network | Reached top three |
| 1997 | IBM **Deep Blue** | Defeated Garry Kasparov at chess |
| — | Othello (Reversi) programs | Superhuman — smaller search space |

Genetic algorithms are noted as performing very well on select domains.

## The Go Problem

Go was the standing counterexample to the search paradigm:

- $19 \times 19 = 361$ grid, so the **branching factor is huge**
- **Search methods inevitably fail** — more structured rules were thought necessary
- The stakes were public: a $1,400,000 prize, funded personally by the late Mr. Ing Chang Ki, for the first program to beat a selected 12-year-old player

Go is where [[Alpha-Beta Pruning]]'s $b^{m/2}$ saving stops being enough. Reducing $b = 361$ to $19$ still leaves an intractable tree.

## The Learning Era

| Year | System | Achievement |
|---|---|---|
| 2015 | DeepMind DQN | Atari 2600 games — see [[Deep Q-Network]] |
| 2016 | **AlphaGo** | Beat Go grand master Lee Sedol 4–1 |
| 2017 | Alpha Zero | Chess, Shogi, and Go |
| 2019 | MuZero | Atari plus multiple board games, **without knowledge of the rules** |
| 2019 | AlphaStar | StarCraft II |

## The Pattern

**AlphaGo combined deep reinforcement learning with tree search** — it did not replace search but supplied the two things search could not provide at Go's branching factor: a learned evaluation function and a learned move prior.

The trajectory continues through the table. AlphaZero drops the human game database; MuZero drops even the rules, learning a model of the dynamics. Each step removes hand-supplied knowledge, which connects directly to [[Deep Learning]]'s central claim — learn the representation instead of designing it.

## See Also

- [[Game Playing]]
- [[Deep Q-Network]]
- [[Reinforcement Learning]]
- [[Deep Learning]]
- [[History of AI]]
- [[CSCE 420]]
