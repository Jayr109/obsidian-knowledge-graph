---
title: "Longest Valley Subsequence"
type: algorithm
tags: [dynamic-programming, sequences, subsequence, algorithms, CSCE-411]
sources: [final-exam-sp26]
course: CSCE 411
updated: 2026-05-06
---

The Longest Valley Subsequence (LVS) problem asks: given a sequence of n positive integers, find the length of the longest subsequence that forms a *valley* — decreasing until its midpoint, then increasing afterward. It is solved with a 2D dynamic programming table in O(n³) time.

## Problem Definition

**Valley sequence**: y₁, y₂, ..., yₖ is a valley if:
- yᵢ > yᵢ₊₁ for all 1 ≤ i < k/2 (strictly decreasing in the first half)
- yᵢ < yᵢ₊₁ for all k/2 < i < k (strictly increasing in the second half)

Note: the middle element is the unique minimum. Both even and odd lengths are valid (for even length k, there is no single "middle" element — the valley just turns at the boundary between positions k/2 and k/2+1).

**Examples of valleys**: 10, 7, 3, 8 and 9, 8, 5, 7, 12.

**Input**: Array A[1..n] of positive integers.
**Output**: Length of the longest valley subsequence of A.

**Example**: A = [101,1,40,100,90,80,30,50,43,87,48,46,44,47,103,102]  
Longest valley: 101, 100, 90, 80, 30, 43, 46, 47, 102 → **length 9**

## Intuition: Why 2D DP?

The standard 1D LIS subproblem (LIS ending at index i) doesn't capture valley structure because a valley has constraints on *both* ends simultaneously — the first element must be large, the last must be large, and everything in between must descend then ascend.

The key insight is to **anchor both ends**: define LVS(i, j) as the longest valley subsequence whose first element is A[i] and last element is A[j]. The recurrence then *peels off* one element from each end at a time.

## DP Subproblem

**Definition**: LVS(i, j) = length of the longest subsequence of A[i..j] that is a valley, includes A[i] as its first element, and includes A[j] as its last element.

## Recurrence

$$LVS(i,j) = \begin{cases}
0 & \text{if } i > j \\
1 & \text{if } i = j \\
2 + \max_{\substack{i < i' \le j' < j \\ A[i'] < A[i] \\ A[j'] < A[j]}} LVS(i', j') & \text{otherwise (if any valid } i',j' \text{ exist)} \\
2 & \text{if no valid } i', j' \text{ exist (just the pair } A[i], A[j]\text{)}
\end{cases}$$

**What the recurrence does**: it selects the **second element** (at index i') and the **second-to-last element** (at index j') of the valley. Both must be smaller than their adjacent endpoints (A[i'] < A[i] and A[j'] < A[j]) and i' ≤ j' (they may be the same element, making an odd-length valley). The interior LVS(i', j') handles everything in between recursively.

**Why this works**: the second element coming after i and before (or at) j', and the second-to-last coming before j and after (or at) i', together with the recursive sub-valley LVS(i', j'), guarantee the decreasing-then-increasing shape.

## Fill Order and Memoization

Each subproblem LVS(i, j) depends only on LVS(i', j') where i < i' and j' < j — strictly smaller subproblems in both dimensions. Therefore:

**Fill order**: decreasing i (outer loop) and decreasing j (inner loop) — equivalently, fill the 2D table from **bottom to top, right to left**.

```
for i from n down to 1:
  for j from n down to i:
    compute LVS(i, j) using previously filled entries
```

## Answer

$$\text{answer} = \max_{1 \le i \le j \le n} LVS(i, j)$$

## Complexity

| Measure | Value |
|---------|-------|
| Subproblems | O(n²) — all pairs (i, j) with i ≤ j |
| Work per subproblem | O(n²) in naïve scan of all (i', j') pairs; O(n) with careful loop |
| **Time** | **O(n³)** |
| Space | O(n²) — the 2D table |

## Connection to LIS

The Longest Valley Subsequence is related to [[Longest Increasing Subsequence]] but strictly harder:

- **LIS**: 1D subproblem; one index anchored (the end).
- **LDS (Longest Decreasing Subsequence)**: symmetric to LIS; length of longest strictly decreasing subsequence ending at i.
- **LVS**: 2D subproblem; both endpoints anchored; captures both a decreasing prefix and an increasing suffix.

**Alternative approach via LIS+LDS** (mentioned in exam Q3 sidenote): compute LDS(i) (longest decreasing subseq ending at A[i]) and LIS(i) (longest increasing subseq starting at A[i]) for all i. Then:

$$\text{LVS} = \max_{1 \le i \le n} \max\!\Big( 2 \cdot \min(LDS(i), LIS(i)) - 1,\quad 2 \cdot \min\!\Big(LDS(i),\, \max_{i < j \le n} LIS(j)\Big) \Big)$$

- The first term handles **odd-length** valleys centered at A[i] (subtract 1 to avoid double-counting A[i]).
- The second term handles **even-length** valleys whose descending half ends at A[i] and whose ascending half starts somewhere after i.

This alternative runs in O(n²) time — faster than the 2D DP — but the 2D DP formulation is more natural to derive.

## Exam Notes

This was Q4 on the CSCE 411 Spring 2026 Final Exam. The exam identified it as the most algorithmically demanding DP problem of the course. Key pitfalls:
- Confusing the fill order (must fill large i, large j first, since you depend on larger-i subproblems)
- Forgetting the base case LVS(i, i) = 1 (single element is a valley of length 1)
- Forgetting to scan all valid (i', j') pairs, not just diagonally adjacent ones

## See Also

- [[Dynamic Programming]]
- [[Longest Increasing Subsequence]]
- [[Subset Sum]]
- [[Final Exam Solutions — Spring 2026]]
- [[CSCE 411]]
