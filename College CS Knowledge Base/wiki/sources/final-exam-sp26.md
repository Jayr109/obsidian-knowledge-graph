---
title: "Final Exam Solutions — Spring 2026"
type: source
tags: [exam, CSCE-411, undecidability, dynamic-programming, divide-and-conquer, max-flow, NP-completeness, approximation, greedy]
sources: []
course: CSCE 411
updated: 2026-05-06
---

CSCE 411 Final Exam Solutions, Spring 2026. Six problems (students skip one); 120 minutes; 20 points each. Covers the full semester from decidability through approximation algorithms. Allowed: pen, scratch paper, up to 2 pages of exam aids. No electronics.

NP-complete languages assumed on exam: 3-SAT, Clique, Subset-Sum, Ham-Cycle, 3-Col.

## Q1 — True/False (20 pts)

Ten statements, 2 pts each. Key results:

| # | Statement | Answer | Why |
|---|-----------|--------|-----|
| a | Decidable L ⟹ Σ* − L decidable | **T** | Decidable languages closed under complement; swap Accept/Reject states |
| b | 18n = O(n²) provable with n₀=3, c=2 | **F** | Need 18n ≤ 2n² ⟹ n ≥ 9; n₀=3 fails (e.g. n=3: 54 ≤ 18? No) |
| c | Σdeg(x) = \|E\| for undirected G | **F** | [[Graph Theory\|Handshake Lemma]]: Σdeg(x) = **2**\|E\| (each edge contributes degree 1 at each endpoint) |
| d | Bellman-Ford relaxes each edge at most once | **F** | Each edge is relaxed once **per iteration**; n−1 iterations → each edge relaxed up to n−1 times |
| e | Unstable pair (d,h) ⟹ M does not match d and h | **T** | By definition: unstable pair means d and h are not matched to each other but both prefer each other over their current matches |
| f | Earliest-finish-time greedy is optimal for interval scheduling | **T** | Proven by exchange argument in Lecture 23 |
| g | Feasible LP ⟹ LP is bounded | **F** | Feasible means ∃ a solution; bounded means the objective doesn't go to ∞. A feasible LP can be unbounded (e.g. maximize x with x ≥ 0) |
| h | NP-Complete ⟹ L ∈ EXP | **T** | NP ⊆ EXP (try all certificates in exponential time); NP-complete ⊆ NP ⊆ EXP |
| i | FPTAS ⟹ polynomial-time 2-approximation | **T** | Set ε = 1 in the FPTAS definition: outputs a (1+1) = 2-approximation in time polynomial in n and 1/1 = n |
| j | GreedyMaxCut finds cut 100 ⟹ G has ≤ 200 edges | **T** | GreedyMaxCut guarantees cut ≥ \|E\|/2 (each moved vertex increases cut by ≥ 0); 100 ≥ \|E\|/2 ⟹ \|E\| ≤ 200 |

### Tricky T/F clarifications

- **(b)** The constants n₀ and c must satisfy the definition for **all n ≥ n₀**. n₀=3 fails because 18(3) = 54 > 2(3²) = 18. A valid choice would be n₀=9, c=2.
- **(c)** The Handshake Lemma is Σdeg = **2|E|**, not |E|. A common error.
- **(d)** Bellman-Ford runs n−1 outer loop iterations, relaxing **all m edges** each time. Total relaxations = (n−1)·m, not m.
- **(g)** Feasibility and boundedness are independent properties of an LP. A problem can be: feasible+bounded (normal), feasible+unbounded (objective → ∞), infeasible, or infeasible+bounded (vacuously).
- **(i)** FPTAS gives a (1+ε)-approximation for any ε > 0 in time polynomial in n and 1/ε. Plugging in ε=1 gives a 2-approx in polynomial time.

## Q2 — Undecidability: ACCEPTS-ODD-LENGTH (20 pts)

**Problem**: Prove ACCEPTS-ODD-LENGTH := {⟨M⟩: L(M) = {s ∈ Σ*: |s| is odd}} is undecidable.

**Method**: Turing reduction HALTS ≤_T ACCEPTS-ODD-LENGTH.

**Construction**: Given ⟨M, x⟩, build M'(y) that first runs M(x), then accepts iff |y| is odd.

**Correctness**:
- If ⟨M,x⟩ ∈ HALTS: M(x) halts, so M' acts on |y|. L(M') = all odd-length strings. So ⟨M'⟩ ∈ ACCEPTS-ODD-LENGTH.
- If ⟨M,x⟩ ∉ HALTS: M(x) loops forever, M' loops on all inputs. L(M') = ∅ ≠ odd-length strings. So ⟨M'⟩ ∉ ACCEPTS-ODD-LENGTH.

This is a standard **use-M-as-a-filter** Turing reduction: M' "gates" its actual behavior behind a test of whether M(x) halts. See [[Turing Reductions]] and [[Decidability and Undecidability]].

## Q3 — Array Rotation (20 pts)

**Problem**: Given a k-step rotation of a sorted array of distinct integers, find k in O(log n).

**Key insight**: The answer is n − imax, where imax is the index of the maximum element. Elements before (and at) the maximum are ≥ A[1]; elements after the maximum are < A[1]. This creates a binary predicate suited to binary search.

```
FindMax(A[1..n], low=1, high=n):
  if low = high: return n − low
  mid = ⌈(low + high) / 2⌉
  if A[mid] < A[1]: return FindMax(A, low, mid − 1)
  return FindMax(A, mid, high)
```

**Correctness invariant**: low ≤ imax ≤ high at every call. Terminates in O(log n) since search space halves each call.

**Sidenote from solutions**: Also solvable via LDS/LIS DP in O(n²): compute LDS(i) (longest decreasing subseq ending at i) and LIS(i) (longest increasing subseq starting at i), then take max over a formula combining them. This is much slower but connects to [[Longest Increasing Subsequence]] and [[Longest Valley Subsequence]].

See [[Binary Search]] for the binary search variant added from this problem.

## Q4 — Longest Valley Subsequence (20 pts)

**Problem**: A *valley* sequence decreases until the midpoint then increases. Find the longest valley subsequence of A[1..n] in polynomial time.

Example: A = [101,1,40,100,90,80,30,50,43,87,48,46,44,47,103,102] → length 9 (101,100,90,80,30,43,46,47,102).

**DP formulation**: LVS(i,j) = length of longest valley subseq of A[i..j] starting with A[i] and ending with A[j].

$$LVS(i,j) = \begin{cases} 0 & i > j \\ 1 & i = j \\ 2 + \max_{i < i' \le j' < j,\; A[i'] < A[i],\; A[j'] < A[j]} LVS(i', j') & \text{otherwise} \end{cases}$$

**Answer**: max over all 1 ≤ i ≤ j ≤ n of LVS(i,j).

**Fill order**: decreasing i, decreasing j (bottom-to-top, right-to-left). Each cell takes O(n) time to compute (scanning for valid i', j' pairs).

**Complexity**: O(n²) subproblems × O(n) per subproblem = **O(n³) time, O(n²) space**.

See [[Longest Valley Subsequence]] for the full treatment with the complete recurrence, fill order diagram, and comparison to LIS.

## Q5 — Fruit Salad (20 pts)

**Problem**: x fruit types, y customers each with per-fruit maximums B[i][j] and total demand C[i]; inventory A[i]. Can all customers be satisfied simultaneously?

**Reduction to max flow**: Build a flow network:
- Source s → fruit vertex fᵢ with capacity A[i] (inventory constraint)
- Fruit fⱼ → customer cᵢ with capacity B[i][j] (per-fruit willingness)
- Customer cᵢ → sink t with capacity C[i] (total demand)

All customers satisfied iff max flow = Σ C[i].

**Runtime**: Input size n = Θ(xy). Graph has O(x+y) vertices, O(xy) edges. Max-flow runs in O((xy)^{1+o(1)}) = O(n^{1+o(1)}) — polynomial.

See [[Maximum Flow]] for the updated applications list.

## Q6 — NP Completeness: HALF-CYCLE (20 pts)

**Problem**: Prove HALF-CYCLE := {⟨G⟩: G has a cycle visiting ≥ |V|/2 vertices} is NP-complete.

**NP membership**: Certificate = ordered list of vertices. Verifier checks: length ≥ |V|/2, no repeated vertices, consecutive vertices are adjacent (including last→first edge). Runs in O(n).

**NP-hardness**: Reduce HAM-CYCLE ≤_p HALF-CYCLE.
- Given G with n vertices, construct G' = G ∪ {n isolated vertices} (2n vertices total).
- G has Ham-cycle ⟺ G' has a cycle of length n = (2n)/2 = |V(G')|/2.
- The isolated vertices block any cycle in G' from using them (no edges), so any half-cycle must be entirely in G.

Construction takes O(n) (just add n isolated vertices).

See [[NP Completeness]] for the updated NP-complete table.

## See Also

- [[Decidability and Undecidability]]
- [[Turing Reductions]]
- [[Binary Search]]
- [[Dynamic Programming]]
- [[Longest Valley Subsequence]]
- [[Maximum Flow]]
- [[NP Completeness]]
- [[Approximation Algorithms]]
- [[Bellman-Ford Algorithm]]
- [[Graph Theory]]
- [[Linear Programming]]
- [[CSCE 411]]
