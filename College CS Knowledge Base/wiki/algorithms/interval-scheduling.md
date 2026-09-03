---
title: "Interval Scheduling"
type: algorithm
tags: [greedy, scheduling, algorithms]
sources: [lecture-23-greedy-algorithms]
course: CSCE 411
updated: 2026-04-09
---

Interval Scheduling is the problem of selecting the maximum number of non-overlapping intervals (jobs, classes, events) from a set of candidates. It is a canonical [[Greedy Algorithms|greedy]] problem, solved optimally by always selecting the interval with the earliest finish time.

## Problem Definition

**Input**: A set of intervals, each with a start time and finish time.
**Output**: A maximum-size subset of intervals with no two overlapping.

## Greedy Algorithm: Earliest Finish Time

```
Sort intervals by finish time (ascending)
last_finish = -∞
selected = []
for each interval i (in sorted order):
    if i.start >= last_finish:
        selected.append(i)
        last_finish = i.finish
return selected
```

**Why "Earliest Finish Time"?** Intuitively, choosing the interval that ends soonest leaves the most room for future intervals.

## Alternative Greedy Strategies — Which Work?

HW6 and Exam 3 systematically analyzed five alternative greedy strategies:

| Strategy | Optimal? | Evidence |
|----------|----------|---------|
| Earliest **finish** time (canonical) | **Yes** | Exchange argument proof |
| Latest **start** time | **Yes** | Exchange argument; latest-starting class conflicts with at most one other class at a time; any conflict can be swapped out |
| Latest **finish** time (= earliest start last) | **No** | Counterexample: {(1,10),(2,4),(6,9)} — greedy picks (1,10); OPT = {(2,4),(6,9)} |
| Shortest **duration** | **No** | Counterexample: {(1,5),(4,7),(6,10)} — greedy picks (4,7); OPT = {(1,5),(6,10)} |
| Most conflicts (discard) | **No** | Counterexample: {(1,4),(2,7),(3,6),(5,10),(8,13),(9,12),(11,14)} — discard (5,10) is wrong |
| Discard **fully-containing** interval, then choose latest-finish | **Yes** | Two-case induction: if y fully contains x, swap y→x in OPT with no size loss; once no containments exist, latest-ending class must also start latest → apply latest-start argument |

Key insight: **"earliest finish"** and **"latest start"** both work for opposite but symmetric reasons. Duration-based and conflict-count-based heuristics both fail.

See [[Homework 6 Solutions — Spring 2026]] Q1 for full proofs and counterexamples.

## Correctness Proof

**Theorem**: GreedySchedule returns a valid schedule with the maximum possible number of intervals.

**Proof approach** (Exchange Argument):
1. Let G = greedy solution, O = any optimal solution.
2. Find the first interval where G and O differ.
3. Show that swapping O's choice for G's choice (earliest finish time) does not reduce the solution size — because G's interval finishes no later than O's, leaving at least as much room for future intervals.
4. By induction, G is at least as good as O.

## Optimal Substructure

After scheduling the greedy choice (earliest finish interval), the remaining problem is: schedule maximum intervals from those that start after the chosen interval finishes. This is the same problem on a smaller input — optimal substructure holds.

## See Also

- [[Interval Covering]] — related problem: minimum points stabbing all intervals (different goal)
- [[Greedy Algorithms]]
- [[Huffman Coding]]
- [[Homework 6 Solutions — Spring 2026]]
- [[Exam 3 Solutions — Spring 2026]]
- [[CSCE 411]]
