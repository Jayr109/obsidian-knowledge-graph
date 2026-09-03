---
title: "Exam 1 Solutions — Spring 2026"
type: source
tags: [csce411, exam, solutions, asymptotic-analysis, decidability, divide-and-conquer, graphs]
sources: []
course: CSCE 411
updated: 2026-04-09
---

# Exam 1 Solutions — Spring 2026

**Source file:** `raw/CSCE411_Sp26_Exam_1_Solutions.pdf`
**Course:** CSCE 411, Spring 2026
**Format:** 50-minute exam; 2 pages of exam aids allowed.
**Coverage:** Topics through BFS & DFS — proofs, undecidability, asymptotic analysis, divide & conquer, graphs.

## T/F Key Results

| Statement | Answer | Reasoning |
|-----------|--------|-----------|
| If A⇒B then ¬B⇒¬A | **TRUE** | Contrapositive — logically equivalent to original implication |
| {⟨M⟩ : M is TM with ≥50 states} is undecidable | **FALSE** | Decidable — only finitely many TMs have exactly n states for any fixed n; membership is checkable |
| {⟨M⟩ : \|L(M)\|=1} is undecidable | **TRUE** | Non-trivial property of TM languages → Rice's theorem applies |
| {⟨M⟩ : M(ε) loops forever} is undecidable | **TRUE** | Reduction from Halting Problem |
| n³ = O(10n⁵) | **TRUE** | n³ ≤ 10n⁵ for all n ≥ 1 |
| f(n)=O(g(n)) and g(n)=O(f(n)) → f(n)=Θ(g(n)) | **TRUE** | Definition of Θ is exactly this two-sided bound |
| Binary search works on unsorted array | **FALSE** | Requires sorted input to guarantee correctness |
| Karatsuba multiplies n-digit numbers in O(n^log₂3) | **TRUE** | Recurrence T(n) = 3T(n/2) + O(n) → T(n) = O(n^log₂3) |
| T(n)=5T(n/5)+Θ(n log n) → T(n)=Θ(n log n) | **TRUE** | Master Theorem Case 2 (extended): f(n) = Θ(n^(log_b a) · log n) |
| T(n)=3T(n/2)+Θ(n²) → T(n)=Θ(n²) | **TRUE** | Master Theorem Case 3: f(n) = Θ(n²) dominates n^(log₂3) ≈ n^1.585 |
| T(n)=2T(n/3)+Θ(1) → T(n)=Θ(n^log₂3) | **FALSE** | Correct answer: T(n)=Θ(n^(log₃2)), not log base 2 |
| 3-regular graph with 6 vertices exists | **TRUE** | e.g., K₃,₃ (complete bipartite graph) |
| Adjacency list: Θ(1) time to check edge (u,v) | **FALSE** | O(deg(v)) — must scan neighbor list |

## Long Answer Highlights

### Q2: Asymptotic Proof
**Claim:** n² − n = Ω(n² + 10n)
**Solution:** Find c, n₀ such that n² − n ≥ c(n² + 10n) for all n ≥ n₀.
Setting c = 1/12, n₀ = 2 works. Verified: for n ≥ 2, n² − n ≥ (1/12)(n² + 10n).

### Q3: Summation Induction Proof
Standard mathematical induction on a summation identity. Proof structure: base case + inductive step using the inductive hypothesis.

### Q4: PCP Reduction
**Claim:** PCP-ALL (the variant where all PCP instances have a solution) is undecidable.
**Method:** Turing reduction from a known undecidable problem (likely ATM or Halting Problem) to PCP-ALL. Show that deciding PCP-ALL would allow us to decide the undecidable source problem.

## See Also

- [[Asymptotic Analysis]]
- [[Decidability and Undecidability]]
- [[Karatsuba's Algorithm]]
- [[Master Theorem]]
- [[CSCE 411]]
