---
title: "Lecture 26 — NP"
type: source
tags: [complexity, NP, P, decision-problems, CSCE-411]
sources: []
course: CSCE 411
updated: 2026-04-21
---

Lecture 26 introduces the class P and the class NP, motivating complexity theory as the third pillar of a computer scientist's toolbox (alongside algorithm design and data structures). The central question is: which problems are *inherently* hard, and how do we provide evidence of hardness?

## Slide-by-Slide Summary

**Slides 1–4 — Toolbox of a Computer Scientist**
The course frames P/NP as "identifying and dealing with intractable problems" — the third major skill after algorithm design and data structures.

**Slides 5–7 — Languages (visual-only)**
Formal definitions of languages, string encodings, and the accepting/deciding distinction. Content was visual; not captured in text extraction.

**Slides 8–11 — The Class P (partially visual)**
P is the class of decision problems solvable in polynomial time. Slides on "Why polynomial time?", "Historical motivation for P", and "Robustness of P" were visual-only.

**Slide 12 — Closure of P**
Key property: a polynomial number of calls to polynomial-time subroutines, plus polynomial extra work, yields a polynomial-time algorithm overall. Formally: if f is polynomial and M' runs in poly-time, then M runs in poly-time:

```
M(x):
  Repeat f(|x|) times:
    run M'(x)
```

**Slides 13–14 — Proving Membership in P; Search to Decision**
- To prove a language is in P: exhibit a polynomial-time algorithm.
- Many *search* problems (find an optimal value) reduce to *decision* problems (does a solution of value ≥ k exist?). Example: binary search over k reduces "find max flow value" to "is there a flow ≥ k?".

**Slide 15 — Brute Force**
Brute force = enumerate all possible solutions, check each. Works for: shortest paths (try all paths), MST (try all edge subsets), sorting (try all permutations), Subset Sum (try all subsets). Requires: enumerable solution space + efficient checking.

**Slides 16–17 — When Brute Force Fails; Exponential Time (visual-only)**
These slides were visual. The implicit lesson: brute force is exponential when the solution space is exponential and no efficient algorithm exists.

**Slides 18 — Proving a Language is NOT in P**
Proving membership in P is easy (give an algorithm). Proving non-membership is hard — open question for NP. Slide was partially visual.

**Slides 19–22 — Graph Coloring**
*2-Coloring*: Polynomial. Run BFS, alternate colors by level. A valid 2-coloring exists iff the graph is bipartite iff it has no odd-length cycles. Checking is O(n + m).

*3-Coloring*: Brute force requires checking 3^n colorings. Checking any single assignment is easy (O(m)), but exhaustive search is exponential.

**Slide 23 — The Class NP**
A language L is in NP if there exists a polynomial-time verifier V such that:
- For every YES instance x ∈ L, there exists a *certificate* c (with |c| polynomial in |x|) such that V(x, c) = 1.
- For every NO instance x ∉ L, for all c, V(x, c) = 0.

For 3-Coloring: the certificate c is a valid 3-coloring (poly space). The verifier checks that each vertex gets one of 3 colors and no two adjacent vertices share a color — O(n + m).

**Slide 24 — The Class Co-NP (visual)**
Co-NP: class of problems where every NO instance has a short, poly-checkable certificate. Visual slide only.

**Slide 25 — NP & Co-NP**
- NP: every YES instance has a short justification checkable in poly time.
- Co-NP: every NO instance has a short justification checkable in poly time.
- P ⊆ NP and P ⊆ Co-NP (a poly-time algorithm is itself a verifier with empty certificate).
- Whether NP = Co-NP is open; believed to be unequal.

## Key Definitions

| Term | Definition |
|------|-----------|
| P | Languages decidable in polynomial time |
| NP | Languages with poly-time verifiers (YES instances have short certificates) |
| Co-NP | Languages with poly-time verifiers for NO instances |
| Certificate | A witness c for a YES instance; \|c\| = poly(\|x\|) |
| Verifier | A poly-time TM V(x, c) that accepts iff c is a valid certificate for x |

## See Also

- [[NP and Complexity Classes]]
- [[NP Completeness]]
- [[Decidability and Undecidability]]
- [[CSCE 411]]
- [[Lecture 27 — NP Verifiers]]
