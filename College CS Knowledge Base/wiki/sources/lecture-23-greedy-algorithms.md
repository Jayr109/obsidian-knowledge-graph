---
title: "Lecture 23 — Greedy Algorithms"
type: source
tags: [greedy, CSCE 411, lecture]
sources: []
course: CSCE 411
updated: 2026-04-09
---

Lecture 23 of [[CSCE 411]], taught by [[Calvin Beideman]]. The largest lecture in this batch (45 slides). Introduces [[Greedy Algorithms]] as a design paradigm, covering two full case studies: [[Interval Scheduling]] and [[Huffman Coding]].

## Source File

`raw/Lecture23_Greedy_Algorithms.pptx` — 45 slides

## Learning Objectives

- Know what greedy algorithms are and when they are useful.
- Understand optimal substructure and the greedy choice property.
- Design greedy algorithms.
- Prove the correctness of a greedy algorithm.

## Key Topics

### Making Change (Motivating Example)

Greedy (largest coin first) works for US denominations but fails for arbitrary denominations:
- 6¢ with coins {1, 3, 4}: greedy gives 4+1+1 (3 coins), optimal is 3+3 (2 coins).

### What is a Greedy Algorithm?

No formal definition. Key characteristics:
- Make small incremental decisions without backtracking.
- Locally optimal choices without considering global picture.
- Simple fixed priority rules.
- Usually fast, but fails for many problems.

### When Greedy Works

Requires both:
1. **Optimal Substructure** (shared with DP and D&C).
2. **Greedy Choice Property** — can reach global optimum via local choices.

### Paradigm Comparison

All three (D&C, DP, Greedy) rely on optimal substructure. Greedy applies when the greedy choice property holds — only 1 subproblem needs to be explored at each step (vs. all subproblems in DP).

### Interval Scheduling

Rejected strategies: earliest start time, shortest duration, fewest conflicts.
Correct strategy: **earliest finish time**.
See [[Interval Scheduling]] for algorithm and proof.

### Exchange Arguments

Standard technique for proving greedy algorithms:
1. Assume an optimal solution differs from greedy.
2. Find the first difference.
3. Show swapping in the greedy choice doesn't worsen the solution.

### Prefix-Free Codes & Huffman Coding

Prefix-free codes represented as binary trees. Goal: minimize total encoded length given character frequencies.
**[[Huffman Coding]]**: merge two least-frequent characters greedily; provably optimal.
**Theorem**: Huffman code has minimum cost among all prefix-free codes (proof via exchange argument + greedy choice property).

## See Also

- [[Greedy Algorithms]]
- [[Interval Scheduling]]
- [[Huffman Coding]]
- [[CSCE 411]]
