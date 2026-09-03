---
title: "Homework 5 Solutions — Spring 2026"
type: source
tags: [csce411, homework, solutions, bipartite-matching, dynamic-programming, game-theory]
sources: []
course: CSCE 411
updated: 2026-04-09
---

# Homework 5 Solutions — Spring 2026

**Source file:** `raw/CSCE_411_HW5_Sp26_Solutions.pdf`
**Course:** CSCE 411, Spring 2026
**Due:** Monday, March 30, 2026
**Topics:** Bipartite Matching, Dynamic Programming

## Problem 1: A Game on Graphs

**Setup:** Alice and Bob alternately mark vertices in a graph. On each turn, a player must mark a vertex adjacent to the most recently marked vertex (i.e., they move along edges). A player who cannot move loses.

**Claim:** If G has a perfect matching, Bob has a winning strategy regardless of Alice's first move.

**Proof:**

Let M be a perfect matching of G. Bob's strategy:

1. Alice marks any vertex v.
2. Since M is a perfect matching, v has a matched partner u in M. Bob marks u (the match of v under M).
3. Now the current vertex is u. Alice must move to some neighbor w of u.
4. Since M is perfect, w has a matched partner x ≠ u in M. Bob marks x.
5. Repeat.

**Why Bob never gets stuck:** At every point when it is Bob's turn, the current vertex w was just marked by Alice. Since M is a perfect matching, w is matched to some vertex x. That vertex x has not yet been marked (the path traced so far consists of matched pairs, and each pair uses distinct vertices). So Bob can always move to x.

**Why Alice gets stuck:** Alice must move to a neighbor of Bob's last mark. After Bob plays optimally, Alice is always placed at an unmatched position in the current path, and the inductive structure guarantees she will eventually be unable to move.

**Key insight:** The perfect matching provides Bob a "mirror strategy" — he always has a valid response by following the matching.

## See Also

- [[Bipartite Matching]]
- [[Dynamic Programming]]
- [[CSCE 411]]
