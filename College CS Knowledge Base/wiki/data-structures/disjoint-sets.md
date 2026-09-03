---
title: "Disjoint Sets"
type: data-structure
tags: [union-find, disjoint-sets, path-compression, union-by-rank, kruskal]
sources: [lecture-11-msts]
course: CSCE 411
updated: 2026-08-25
---

# Disjoint Sets (Union-Find)

The Disjoint Sets data structure (also called Union-Find) maintains a collection of disjoint sets and supports three operations efficiently. It is used in [[Kruskal's Algorithm]] to detect and merge components.

## Operations

- **make_set(x)**: create a new set containing only x
- **find(x)**: return a representative ("name") for x's set — same representative iff same set
- **union(x, y)**: merge the sets containing x and y

## Implementations

### Basic Linked List

Each set is a linked list with head pointers.

- `make_set`: O(1)
- `find`: O(1) — return head
- `union(x, y)`: append y's list to x's list; update all head pointers in y's list → O(|y's list|)
- Worst case over n unions: O(n²)

### Improved Linked List (Union by Size/Rank)

Always merge the smaller list into the larger ("weighted union").

- Any sequence of n `make_set`s and m `find`/`union` operations: O((n + m) log n) total

### Disjoint Forests (Union by Rank + Path Compression)

Each set is a tree; the root is the representative. Two key optimizations:

- **Union by rank**: attach the shorter tree under the taller tree
- **Path compression**: during `find`, make every node on the path point directly to the root

**Amortized cost per operation**: O(α(n)) where α is the inverse Ackermann function. α(n) ≤ 4 for all practical values of n — effectively constant.

This is the implementation used in [[Kruskal's Algorithm]] to achieve near-O(m) total Union-Find cost.

## See Also

- [[Kruskal's Algorithm]]
- [[Minimum Spanning Trees]]
- [[CSCE 411]]
