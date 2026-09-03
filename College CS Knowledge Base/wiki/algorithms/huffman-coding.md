---
title: "Huffman Coding"
type: algorithm
tags: [greedy, compression, algorithms]
sources: [lecture-23-greedy-algorithms]
course: CSCE 411
updated: 2026-04-09
---

Huffman Coding is a [[Greedy Algorithms|greedy]] algorithm for constructing an optimal prefix-free binary code. Given character frequencies, it builds a binary tree that minimizes the total encoded length, assigning shorter codewords to more frequent characters.

## Background: Prefix-Free Codes

A prefix-free binary code assigns a binary string (codeword) to each character such that no codeword is a prefix of another. This allows unambiguous decoding without separators.

A prefix-free code corresponds to a binary tree where characters are leaves and codewords are root-to-leaf paths (0 = left, 1 = right). The cost of a code is: Σ freq(c) × depth(c) for all characters c.

## Algorithm

**Greedy Idea**: Merge the two least-frequent characters at each step, treating the merged pair as a single new character with combined frequency.

```
Insert all characters into a min-priority queue (keyed by frequency)
while queue has more than 1 element:
    c1 = extract-min(queue)
    c2 = extract-min(queue)
    new_node = merge(c1, c2) with freq = freq(c1) + freq(c2)
    insert new_node into queue
return remaining tree
```

**Time**: O(n log n) — n-1 merges, each O(log n) with a heap.

## Why This is Greedy

The algorithm makes a locally optimal choice at each step: merge the two cheapest characters. This is the greedy choice. It satisfies both conditions for greedy correctness:
1. **Optimal Substructure**: after merging the two least-frequent characters, the resulting smaller problem has the same structure.
2. **Greedy Choice Property**: the two least-frequent characters always appear deepest in an optimal tree (they can always be made siblings without increasing cost).

## Correctness

**Theorem**: For every list of character frequencies, Huffman's algorithm produces a prefix-free code with minimum total cost among all prefix-free codes.

**Proof approach** (Exchange Argument + Greedy Choice Property):
1. Show that in any optimal tree, the two least-frequent characters can be made siblings (at the deepest level) without increasing cost — this is the greedy choice property.
2. Show that after merging them, the resulting subproblem is smaller and has the same optimal substructure.
3. By induction, the greedy algorithm is optimal.

## Example

Characters with frequencies: A=5, B=9, C=12, D=13, E=16, F=45. Huffman tree assigns F the shortest code (depth 1), A and B the longest (depth 4 or similar).

*Note: The step-by-step tree construction in Lecture 23 was visual; the diagrams were not fully captured in text extraction.*

## See Also

- [[Greedy Algorithms]]
- [[Interval Scheduling]]
- [[CSCE 411]]
