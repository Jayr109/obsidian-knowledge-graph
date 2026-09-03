---
title: "Homework 6 Solutions — Spring 2026"
type: source
tags: [homework, CSCE-411, greedy, DP, interval-scheduling, balanced-brackets]
sources: []
course: CSCE 411
updated: 2026-05-03
---

Homework 6 for CSCE 411-501, Spring 2026. Due Monday, April 13, 2026. 6 problems covering greedy algorithms, balanced bracket problems, DP on intervals, and tree DP.

## Q1: Alternative Scheduling Algorithms

The canonical [[Interval Scheduling]] algorithm selects the class with the **earliest finish time**. Five alternative greedy strategies are analyzed:

| Strategy | Correct? | Key Reason |
|----------|----------|------------|
| (a) Choose class starting **last** | **Yes** | Exchange argument: any conflicting class must start earlier; OPT can swap it for the latest-starting class without loss |
| (b) Choose class ending **last** | **No** | Counterexample: {(1,10),(2,4),(6,9)} — greedy picks (1,10); OPT picks (2,4)+(6,9) |
| (c) Discard class with **longest duration** | **No** | Counterexample: {(1,5),(6,10),(4,7)} — OPT = 2; greedy discards (4,7) but (1,5) or (6,10) may be next to go |
| (d) Discard class conflicting with **most others** | **No** | Counterexample: {(1,4),(2,7),(3,6),(5,10),(8,13),(9,12),(11,14)} — (5,10) conflicts with 4 others; greedy discards it; OPT={(1,4),(5,10),(11,14)} has size 3, greedy finds only 2 |
| (e) Discard y if fully contained in x; otherwise choose class **ending last** | **Yes** | Two-case induction: (i) if y fully contains x, swapping y→x in OPT gives same-size schedule; (ii) once no containments exist, the class ending last also starts last → apply (a)'s argument |

**Proof technique for (a) and (e)**: induction on number of classes, with exchange argument showing OPT can always be modified to include the greedy choice without losing size. See [[Greedy Algorithms]] for the general exchange argument template.

## Q2: Balanced Parentheses

**(a) Detect balanced string — O(n)**

```
IsBalanced(A[1..n]):
  counter ← 0
  for i from 1 to n:
    if A[i] = '(':  counter ← counter + 1
    elif A[i] = ')':
      counter ← counter − 1
      if counter < 0: return False
  return (counter = 0)
```

Fail if counter goes negative (close before open) or ends non-zero (unmatched opens).

**(b) Length of longest balanced subsequence — O(n)**

```
LongestBalancedSubsequence(A[1..n]):
  counter ← 0; pairs ← 0
  for i from 1 to n:
    if A[i] = '(':  counter ← counter + 1
    elif A[i] = ')' AND counter > 0:
      counter ← counter − 1; pairs ← pairs + 1
  return pairs × 2
```

**Greedy correctness**: whenever we see ')' with an unmatched '(' available, include the pair. To see no balanced subsequence uses more close parens: at the first index i where it would, the counter has reached 0, meaning all k open parens in A[1..i] are already matched — but including one more close paren would require k+1 close parens against k opens, contradicting balance.

## Q3: Balanced Braces (two types: `{}` and `⟨⟩`)

**(a) Detect balanced braces string — O(n)**

Use a **stack** instead of a counter (counter alone can't detect interleaving like `{⟨}⟩`):

```
IsBalanced(A[1..n]):
  S ← empty stack
  for i from 1 to n:
    if A[i] is an open brace: S.push(A[i])
    elif A[i] = '}' and S.top() = '{': S.pop()
    elif A[i] = '⟩' and S.top() = '⟨': S.pop()
    else: return False
  return S.empty()
```

Stack operations are O(1); n iterations → O(n) total.

**(b) Length of longest balanced brace subsequence — O(n³) DP**

Define LBS(i, j) = length of the longest balanced brace subsequence of A[i..j].

**Recurrence**:

```
LBS(i, j) = 0                                                  if i ≥ j
           = max(2 + LBS(i+1, j−1),
                 max_{i≤k≤j}(LBS(i,k) + LBS(k+1,j)))          if A[i],A[j] match
           = max_{i≤k≤j}(LBS(i,k) + LBS(k+1,j))               otherwise
```

- *Match case*: include the outer pair (contributes 2) plus best inside; OR concatenate two independent balanced substrings.
- *No match case*: can only concatenate.
- Edge case: even when A[i],A[j] match, we still consider concatenation — e.g. `{}{}` should not match first and last curly.

**Memoization**: n×n array filled in order of increasing j−i (diagonal order). Answer = LBS(1,n). Θ(n²) subproblems × O(n) work each → **Θ(n³) time, Θ(n²) space**.

See [[Balanced Brackets]] for both problems unified.

## Q4: Delivering Pizzas

**Problem**: pizza shop at position 0 on a number line; n houses at positions A[1..n] (sorted; negative = west). Every minute a house waits, it adds one 1-star review. Minimize total reviews delivering all pizzas.

**Setup**: Insert position 0 (the shop) into A to get A′[1..n+1] at index k. Define:

P(i, j) = minimum reviews to deliver to all stops between A′[i] and A′[j] inclusive, ending at A′[j].

**Recurrence** (case j > k, i.e., final stop is east; symmetric for west):

```
P(k, k) = 0   (at shop, no deliveries yet)
P(i, j) = ∞   if interval doesn't include k (unreachable start)

For j > k ≥ i:
P(i, j) = min(
  P(i, j−1) + (n − (j−i) + 1) × (A′[j] − A′[j−1]),   // arrived from A′[j−1]
  P(j−1, i) + (n − (j−i) + 1) × (A′[j] − A′[i])       // arrived from A′[i]
)
```

- `n − (j−i) + 1` = number of houses still awaiting delivery when we make this drive.
- We never skip a house (drive past without delivering), so the second-to-last stop before A′[j] must be either A′[j−1] or A′[i].

**Memoization**: (n+1)×(n+1) array; fill in order of increasing |j−i|. Answer = min(P(1, n+1), P(n+1, 1)).

**Runtime**: O(n²) subproblems × O(1) each = **O(n²) time and space**.

## Q5: Increment and Triple

**Problem**: starting from x=1, repeatedly increment (+1) or triple (×3). Reach target y in minimum steps.

**Algorithm** (greedy backward):

```
MinSteps(y):
  if y = 1: return 0
  if y mod 3 = 0: return 1 + MinSteps(y/3)
  else: return 1 + MinSteps(y − 1)
```

**Correctness** (induction on y):
- *y not divisible by 3*: last step must be increment, so MinSteps(y) = 1 + MinSteps(y−1). ✓
- *y divisible by 3*: claim last step of any OPT is a triple. If OPT ends with increment: if OPT is all increments, it uses y−1 steps, but our algorithm uses ≤ y/3 steps — contradiction. If OPT has a final triple at step z→3z followed by y−3z increments, we can replace: increment z → y/3 then triple, using (y/3 − z) + 1 = y/3 − z + 1 steps instead of 1 + (y − 3z) = y − 3z + 1. Since y/3 − z < y − 3z for z < y/3, this is shorter — contradiction.

**Runtime**: At least 1 in every 3 steps is a triple → at most 3 log₃ y recursive calls. Each call does O(log y) arithmetic (subtraction) or O(log² y) (division). Total: **O(log³ y)**.

See [[Increment and Triple]] for the full write-up.

## Q6: Blue-Green Trees

**Problem**: binary tree T, color vertices blue/green. Valid coloring: no two consecutive blue vertices on any root-to-leaf path, and no three consecutive green vertices. Count valid colorings.

**Algorithm**: 3-state tree DP. For each vertex v define:
- BG(v, 0) = colorings of subtree at v where v is **blue**
- BG(v, 1) = colorings of subtree at v where v is **green**
- BG(v, 2) = colorings of subtree at v where v is **green** and its children must be **blue**

**Recurrence** (∏ over children x of v):

```
BG(v, 0) = ∏ BG(x, 1)               // blue v → all children must be green
BG(v, 1) = ∏ (BG(x, 0) + BG(x, 2)) // green v → children can be blue, or green with forced-blue grandchildren
BG(v, 2) = ∏ BG(x, 0)               // green v, children forced blue
BG(leaf, ·) = 1 for all states
```

Answer = BG(root, 0) + BG(root, 1).

**Runtime caveat**: the answer can be up to 2ⁿ, so the numbers being multiplied have up to O(n) digits. Each multiplication takes O(n^{log₂3}) using [[Karatsuba's Algorithm]]. With O(n) total multiplications: **O(n^{1 + log₂ 3}) ≈ O(n^{2.585})**.

See [[Blue-Green Trees]] for the full write-up.

## See Also

- [[Greedy Algorithms]]
- [[Interval Scheduling]]
- [[Balanced Brackets]]
- [[Increment and Triple]]
- [[Blue-Green Trees]]
- [[Dynamic Programming]]
- [[Exam 3 Solutions — Spring 2026]]
- [[CSCE 411]]
