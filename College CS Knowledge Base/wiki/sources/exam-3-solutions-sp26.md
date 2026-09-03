---
title: "Exam 3 Solutions — Spring 2026"
type: source
tags: [exam, CSCE-411, greedy, dynamic-programming, linear-programming, tree-DP]
sources: []
course: CSCE 411
updated: 2026-08-25
---

Exam 3 for CSCE 411-501, Spring 2026. 50-minute in-class exam covering Dynamic Programming, Greedy Algorithms, and Linear Programming. 4 questions, 100 points total. Up to 2 pages of exam aids permitted.

## Q1: True/False (30 pts, 3 pts each)

| # | Statement | Answer | Rationale |
|---|-----------|--------|-----------|
| a | The Subset Sum recurrence SS(i,x) = SS(i−1,x) ∨ SS(i−1,x−A[i]) (with SS(0,0)=true, SS(0,x≠0)=false) is correct | **T** | Standard DP recurrence: either skip A[i] or include it |
| b | DP can find min-weight independent set in an arbitrary n-vertex graph in O(n) | **F** | MWIS is NP-hard on general graphs; O(n) tree DP only works on trees |
| c | The greedy change-making algorithm uses the minimum number of coins for any integer currency system with smallest coin = 1 | **F** | Fails for e.g. {1, 3, 4}: making 6¢ greedy gives 4+1+1=3 coins, optimal is 3+3=2 |
| d | Interval scheduling: "choose class starting last, discard conflicts, recurse" is optimal | **T** | Proved by exchange argument — see [[Homework 6 Solutions — Spring 2026]] Q1(a) |
| e | Interval scheduling: "choose class with shortest duration, discard conflicts, recurse" is optimal | **F** | Shortest-duration class may conflict with two others; counterexample exists |
| f | Cost of prefix-free code with n codewords w₁,…,wₙ is Σᵢ length(wᵢ) | **F** | Cost is Σᵢ freq(wᵢ)·length(wᵢ); without frequency weights, code cost is undefined |
| g | LP feasibility depends only on the constraints, not on the objective function | **T** | The feasible region is defined by constraints alone; objective only affects the optimum |
| h | Simplex finds optimal in O(mn⁵) for a feasible bounded LP with n variables and m constraints | **F** | Simplex has no known polynomial-time bound; worst case is exponential. (Interior-point methods *are* polynomial — the falsehood is specific to Simplex.) |
| i | Every optimal solution to a feasible bounded LP occurs at a vertex | **F** | *At least one* optimal occurs at a vertex, but if the optimal face is a continuum, optima exist in the interior of an edge or face |
| j | If P is feasible (standard form LP), its dual is also feasible | **F** | Dual of a feasible LP may be infeasible or unbounded; strong duality guarantees equal *optima* only when both are feasible |

## Q2: LP Duality (10 pts)

Given the primal LP:

```
maximize   x₁ + 2x₂ + 3x₄ − 2x₅
subject to          3x₂ − x₃         + 7x₅ ≤ 14
            −x₁         + 4x₃         + 3x₅ ≤ 8
             x₁ + x₂ + x₃ + x₄ + x₅         ≤ 12
             x₁, x₂, x₃, x₄, x₅ ≥ 0
```

**Dual** (one dual variable yᵢ per primal constraint, one dual constraint per primal variable):

```
minimize   14y₁ + 8y₂ + 12y₃
subject to           −y₂ + y₃ ≥ 1     (for x₁)
            3y₁           + y₃ ≥ 2     (for x₂)
            −y₁ + 4y₂    + y₃ ≥ 0     (for x₃)
                           y₃ ≥ 3     (for x₄)
             7y₁ + 3y₂   + y₃ ≥ −2   (for x₅)
             y₁, y₂, y₃ ≥ 0
```

**Dualization rule, matrix form**: primal is max cᵀx s.t. Ax ≤ b, x ≥ 0; dual is min bᵀy s.t. Aᵀy ≥ c, y ≥ 0. Each primal *constraint* → one dual variable (y ≥ 0 because the constraint is ≤). Each primal *variable* → one dual constraint (≥ its objective coefficient, because the primal is a max).

**Construction rule, by hand**: dual objective = primal RHS; the dual constraint for xⱼ sums the coefficient of xⱼ across all primal constraints, weighted by yᵢ, and that sum must be ≥ the objective coefficient of xⱼ.

See [[Linear Programming]] for the full duality procedure.

## Q3: Interval Covering (30 pts)

**Problem**: Given intervals I = {(s₁,f₁),…,(sₙ,fₙ)} with sᵢ < fᵢ, find the minimum-size set S ⊆ ℤ≥0 such that every interval contains at least one integer from S (a *point cover*). Example: I = {(1,7),(2,4),(3,8),(5,6),(7,10)} → S = {2,6,7} (size 3, not unique).

**Distinct from [[Interval Scheduling]]**: Interval Scheduling selects a maximum set of non-conflicting intervals; Interval Covering places a minimum set of points piercing every interval.

**Algorithm** ([[Interval Covering]]): sort by finish time, then always pick the finish point of the current earliest-finishing uncovered interval.

```
IntervalCover(I):
  If I is empty, return ∅
  Sort intervals by finish time (fᵢ ascending)
  Result ← [f₁]   // always add the first finish time
  For i from 1 to n:
    If sᵢ > last element of Result:
      Append fᵢ to Result
  Return Result
```

**Correctness**: Two-part argument:
- *Covers all*: if sᵢ ≤ last result element x = fⱼ (j < i), then since we sorted by finish, fⱼ ≤ fᵢ, so x ∈ [sᵢ, fᵢ].
- *Minimum size*: each chosen fᵢ is the right endpoint of a "forced" interval. These intervals are pairwise disjoint (each starts after the previous one ends), so any covering set must use a different point per interval — lower bound = |Result|.

**Runtime**: sort Θ(n log n) + scan Θ(n) = Θ(n log n), dominated by the sort.

## Q4: Max-Weight Matching in Trees (30 pts)

**Problem**: Given a weighted tree T with n vertices, output the weight of the maximum-weight matching. A matching is a set of edges sharing no vertex. The optimal matching may use fewer edges than the maximum *size* matching.

**Algorithm** ([[Max-Weight Matching in Trees]] — tree DP):

Root T at arbitrary vertex r. Define MWM(u) = max matching weight in the subtree rooted at u.

**Recurrence**:

```
MWM(u) = max(
  Σ_{v ∈ Children(u)} MWM(v),                          // don't use any edge of u
  max_{v ∈ Children(u)} [w(u,v) + Σ_{w ∈ Children(v) ∪ Children(u) − {v}} MWM(w)]
                                                         // use edge {u,v}
)
```

- **Case 1** (skip u's edges): sum independently over each child's subtree.
- **Case 2** (use edge {u,v}): add w(u,v), then sum over all children of u (except v) plus all grandchildren of u through v — because v is now matched and cannot be matched to any of its children.
- **Base case**: if u is a leaf, MWM(u) = 0 (empty sums and maxima over empty sets return 0).
- **Answer**: MWM(r).

**Memoization**: postorder traversal fills each u.mwm bottom-up. Total work = Σ_u (1 + 2|Children(u)| + |Grandchildren(u)|) ≤ n + 2n + n = O(n), since each vertex is the child of at most one vertex and the grandchild of at most one vertex.

**Comparison to [[Maximum Weight Independent Set]]**: MWIS selects a max-weight set of *vertices* with no two adjacent; MWM in trees selects a max-weight set of *edges* with no two sharing a vertex. Both are tree DP problems solvable in O(n).

## See Also

- [[Linear Programming]]
- [[Interval Scheduling]]
- [[Interval Covering]]
- [[Max-Weight Matching in Trees]]
- [[Maximum Weight Independent Set]]
- [[Greedy Algorithms]]
- [[Dynamic Programming]]
- [[Graph DP]]
- [[Homework 6 Solutions — Spring 2026]]
- [[Homework 7 Solutions — Spring 2026]]
- [[CSCE 411]]
