---
title: "Lecture 29 — NP-Hardness Proofs"
type: source
tags: [CSCE-411, NP-hardness, reductions, 3-SAT, 3-COL, gadgets, lecture]
sources: []
course: CSCE 411
updated: 2026-04-27
---

CSCE 411 lecture by Calvin Beideman (31 slides). Continues from [[Lecture 28 — NP-Completeness]] by working through the standard NP-completeness reduction chain — CIRCUIT-SAT → SAT → 3-SAT → 3-COL — and ending with practical advice for designing Karp reductions. Also contains final exam logistics.

## Slides Index

| # | Title | Notes |
|---|-------|-------|
| 1 | Title — NP-Hardness Reductions | Beideman |
| 2 | Final Exam | May 5, 10:30 AM, cumulative, 6 problems pick-5, 1 T/F + 1 NP-completeness + 4 from earlier exams; 2 pages exam aids |
| 3 | Learning Objectives | Practice NP-completeness proofs, examples, reduction techniques |
| 4–6 | NP / Karp / Hardness recap | (visual) |
| 7 | Properties of Karp Reductions (I) | + Theorem 5 (HALTS NP-hard) + Cook-Levin |
| 8 | CIRCUIT-SAT | (visual — circuit gadget) |
| 9 | SAT is NP-Complete | Verifier description |
| 10 | Easy reduction from CIRCUIT-SAT to SAT? | Naïve idea: recursively convert circuit to formula |
| 11–14 | Bad Example for "Easy Reduction" (I–IV) | Naïve recursion blows up exponentially when fan-out > 1 (a gate's output wires feed multiple gates) |
| 15 | SAT is NP-Hard | Correct reduction: introduce auxiliary variable per gate |
| 16 | (CIRCUIT-SAT → SAT diagram) | (visual) |
| 17–18 | (visual — gadget construction) | |
| 19 | 3-SAT | Definition: clause = OR of one or more literals; 3-CNF = clauses of exactly 3 literals |
| 20 | 3-SAT is NP-Hard | Reduction from SAT |
| 21 | Converting to CNF | (visual) |
| 22 | 3-COL is NP-Hard | Reduction from 3-SAT using gadgets |
| 23–25 | (visual — 3-COL gadget construction) | Variable gadget + clause gadget |
| 26 | Karp Reduction Tips: Direction | Reduce *from* known NP-hard *to* new problem |
| 27 | Karp Reduction Tips: Problem Choice | Match structure: formulas → SAT/3-SAT, numbers → SUBSET-SUM, graphs → VC/Clique/IS/3-COL/Ham-Path; 3-SAT often best first try |
| 28 | Karp Reduction Tips: Developing a Function | Map solutions to solutions; use gadgets for constraints |
| 29 | Karp Reduction Tips: Check Your Work! | (visual) |
| 30 | Other NP-Hard Problems (See CLRS) | (visual — list) |
| 31 | Other fun NP-Hard problems | (visual) |

Most reduction-construction slides are visual-only (gadget diagrams, circuit-to-formula derivations, 3-COL color gadgets). Text extraction captured the slide titles and prose explanations.

## Key Takeaways

### The Reduction Chain

The standard NP-completeness chain established in this lecture:

```
CIRCUIT-SAT ≤_p SAT ≤_p 3-SAT ≤_p 3-COL
   (Cook-Levin)   (gadget)  (clause→3)  (graph gadgets)
```

Each step adds one new NP-complete problem to the catalog, all rooted at the Cook-Levin theorem.

### Why "Easy" CIRCUIT-SAT → SAT Fails

The naïve idea: recursively convert each gate's output to a formula in terms of its inputs. **Failure mode**: when a gate's output feeds multiple downstream gates (fan-out > 1), recursive expansion duplicates the entire subformula for each consumer. This produces exponential blowup, violating the polynomial-time requirement of a Karp reduction.

**The fix**: introduce one auxiliary variable per gate. For each gate with output y and inputs x₁, x₂ (and operator op), add clauses encoding y ⟺ op(x₁, x₂). The final formula is satisfiable iff the circuit is. Size grows linearly in the number of gates.

This is a recurring pattern: **avoid duplication by naming intermediate values with fresh variables.**

### 3-SAT and CNF

- **Clause**: OR of one or more literals (a literal is a variable or its negation).
- **CNF formula**: AND of clauses.
- **3-CNF**: every clause has exactly 3 literals.
- **3-SAT**: language of satisfiable 3-CNF formulas.

The reduction SAT ≤_p 3-SAT converts an arbitrary CNF formula to a 3-CNF one, again using auxiliary variables to split long clauses (4+ literals) into chains of 3-literal clauses.

### 3-COL is NP-Hard (Sketch)

Reduce 3-SAT ≤_p 3-COL. Build a graph G with:

- A "palette" triangle on vertices {T, F, X}, fixing the meaning of three colors.
- A **variable gadget**: for each variable x, two vertices x and ¬x both connected to X (forcing them to take T or F) and to each other (forcing them to differ — one T, one F).
- A **clause gadget**: for each 3-clause (ℓ₁ ∨ ℓ₂ ∨ ℓ₃), a small graph (typically 6 vertices forming an OR gadget) that is 3-colorable iff at least one literal is T.

φ is satisfiable iff G is 3-colorable. The construction is poly-time in |φ|.

### Karp Reduction Tips

These tips are the practical core of the lecture and apply to every NP-hardness exam problem.

**1. Direction**: To prove L is NP-hard, reduce **from** a known NP-hard problem **to** L. (Reducing in the wrong direction proves nothing — it would only put L *above* the chosen problem, not below all of NP.)

**2. Problem Choice**: Pick a known NP-hard problem whose structure matches L:

| New problem about... | Try reducing from... |
|---|---|
| Propositional formulas | SAT, 3-SAT |
| Sets of integers | SUBSET-SUM |
| Graphs | VERTEX-COVER, CLIQUE, INDEPENDENT-SET, 3-COL, HAM-PATH |
| Other | Be creative; 3-SAT is a good default |

3-SAT has constrained, regular structure (every clause has exactly 3 literals) that makes gadgets clean. If your first attempt stalls, switch to a different problem.

**3. Function Design**: Start by mapping *solutions to solutions*.
- 3-SAT solution = truth values to variables.
- 3-COL solution = colors to vertices.
- ⇒ map variables to vertices, truth values to colors.
- Then build **gadgets** that translate each constraint of the source problem into the target problem's structure (e.g., "this clause must have a true literal" becomes "this clause-gadget must be 3-colorable").

**4. Check Your Work**: After defining f, verify both directions of x ∈ L₁ ⟺ f(x) ∈ L₂, and verify f runs in poly time.

## Final Exam Logistics

- Tuesday May 5, 10:30 AM – 12:30 PM, in classroom
- Cumulative
- 2 pages of exam aids permitted
- 6 problems; pick 1 to drop (it will not be graded — student selects)
- Structure: 1 T/F (~10 parts), 1 NP-completeness, 4 from earlier exams' material
- Earlier-exam material can include topics in scope but not previously asked
- Review sheet on NP and sample exam to be posted

## Cross-References

- Builds on: [[Lecture 28 — NP-Completeness]] (Cook-Levin, definitions)
- Continues into: [[Lecture 31 — Approximation Algorithms]] (what to do once NP-hardness is established)
- Practice: [[Practice — NP-Hardness]] (5 problems applying these techniques)
- Worked example: [[NP-Hardness Scribbles]] (a kCol reduction worked out in handwriting)

## See Also

- [[NP Completeness]]
- [[Karp Reductions]]
- [[Lecture 28 — NP-Completeness]]
- [[Lecture 31 — Approximation Algorithms]]
- [[Practice — NP-Hardness]]
- [[NP-Hardness Scribbles]]
- [[CSCE 411]]
