---
title: "Balanced Brackets"
type: concept
tags: [greedy, dynamic-programming, strings, algorithms]
sources: [homework-6-solutions-sp26]
course: CSCE 411
updated: 2026-05-03
---

Balanced bracket problems ask whether strings of bracket characters form valid nesting structures, or how to find the longest balanced subsequence. Single-type brackets (parentheses) admit simple greedy counter solutions; multi-type brackets require a stack for detection and O(n³) DP for longest-subsequence.

## Balanced Parentheses (single type)

A balanced string of parentheses is defined recursively:
- ε (empty string) is balanced
- If s is balanced, then (s) is balanced
- If s and t are balanced, then st (concatenation) is balanced

Example: `(())()` is balanced; `)(` is not.

### Detection — O(n)

Greedy counter: increment on `(`, decrement on `)`. Fail immediately if counter goes negative; pass iff counter = 0 at end.

```
IsBalanced(A[1..n]):
  counter ← 0
  for each character c in A:
    if c = '(':  counter += 1
    elif c = ')':
      counter -= 1
      if counter < 0: return False
  return (counter = 0)
```

### Longest Balanced Subsequence — O(n)

Greedy: whenever we see `)` and there is an unmatched `(` available, greedily include the pair.

```
LongestBalancedSubsequence(A[1..n]):
  counter ← 0;  pairs ← 0
  for each character c in A:
    if c = '(':  counter += 1
    elif c = ')' and counter > 0:
      counter -= 1;  pairs += 1
  return pairs × 2
```

**Correctness**: no balanced subsequence can include more `)` characters than this algorithm. At the first position where any competing subsequence would include more, the counter has reached 0 — all available `(` are already matched — so including one more `)` would require more close than open parens (contradiction with balance). Return pairs × 2 since balanced strings always have even length.

## Balanced Braces (multi-type: `{}` and `⟨⟩`)

Multi-type brackets can interleave incorrectly even with matching counts: `{⟨}⟩` has matching totals but is invalid. A counter is insufficient; a **stack** is required.

### Detection — O(n)

```
IsBalanced(A[1..n]):
  S ← empty stack
  for each character c in A:
    if c is an open brace: S.push(c)
    elif c = '}' and S.top() = '{': S.pop()
    elif c = '⟩' and S.top() = '⟨': S.pop()
    else: return False
  return S.is_empty()
```

Push open braces; pop on matching close. Any mismatch (e.g., a `}` while `⟨` is on top) returns False immediately. Stack is O(n) space.

### Longest Balanced Brace Subsequence — O(n³) DP

Let LBS(i, j) = length of longest balanced brace subsequence of A[i..j].

**Recurrence**:

```
LBS(i, j) = 0                                              if i ≥ j

           = max(2 + LBS(i+1, j−1),
                 max_{i≤k<j}(LBS(i,k) + LBS(k+1,j)))      if A[i] and A[j] form a matching pair

           = max_{i≤k<j}(LBS(i,k) + LBS(k+1,j))           otherwise
```

**Three cases**:
1. Base: length-1 substrings have no balanced subsequence.
2. Matching pair (A[i], A[j]): either wrap them around LBS(i+1,j−1) for 2 + inside, OR split at some k and concatenate.
3. No match: only concatenation is possible.

**Why both cases even when A[i],A[j] match**: matching first and last may not be optimal. E.g., `{}{}` — matching first `{` with last `}` leaves `{}` sandwiched with the inner `}` and `{` as the "inside," which has empty balanced content, whereas the concatenation gives 4.

**Memoization**: n×n array; fill in order of increasing j−i (process diagonals). Answer = LBS(1,n).

**Runtime**: Θ(n²) subproblems × O(n) work each (trying all split points k) = **Θ(n³) time, Θ(n²) space**.

## Summary Table

| Problem | Type | Algorithm | Time |
|---------|------|-----------|------|
| Is string balanced? | Single-type () | Counter | O(n) |
| Longest balanced subsequence | Single-type () | Greedy counter | O(n) |
| Is string balanced? | Multi-type {}⟨⟩ | Stack | O(n) |
| Longest balanced subsequence | Multi-type {}⟨⟩ | DP | O(n³) |

## See Also

- [[Dynamic Programming]]
- [[Greedy Algorithms]]
- [[Homework 6 Solutions — Spring 2026]]
- [[CSCE 411]]
