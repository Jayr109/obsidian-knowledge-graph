---
title: "CSCE 420 Homework 2 — Game Playing, Logic"
type: source
tags: [csce420, homework, hw2, minimax, alpha-beta, resolution, cnf, prenex, skolemization, unification, fall-2026]
sources: []
course: CSCE 420
semester: Fall 2026
exam: midterm
updated: 2026-11-04
---

Homework 2 of the user's **Fall 2026** section. 100 points, 12 problems — 11 written, 1 programming — spanning game playing ([[CSCE 420 Lecture 2 — Search and Game Playing]]) and logic ([[CSCE 420 Lecture 3 — Logic and Automated Theorem Proving]]). Archived as `raw/CSCE420_HW2_Fall2026.pdf` (**corrected version**), alongside the pre-correction sheet `raw/CSCE420_HW2_Fall2026_original-4-cuts.pdf`, with the starter notebook `raw/CSCE420_HW2_Fall2026_minmax.ipynb` and the instructor's annotated correction slip `raw/CSCE420_HW2_Fall2026_correction.png`.

> **Past due; the instructor's key has been released.** Recorded here: what is asked, and the rules and worked conventions the sheet supplies — which are the same rules the midterm grades against. The official answers are at [[CSCE 420 Homework 2 Solutions — Fall 2026]], and they confirm the **five**-cut correction.

## Part 1 — Game Playing (Problems 1–3, 34 pts)

One game tree, used twice. MAX nodes are △, MIN nodes ▽; successors explored **left to right**.

| # | Asked |
|---|---|
| 1 | [[Minimax]]: assign a utility to every internal node; mark the optimal path from the root MAX node |
| 2 | [[Alpha-Beta Pruning]] on the *same* tree: (a) utilities and optimal path, (b) **final α and β at every node** — root starts at α = −∞, β = ∞, (c) draw a line through each pruned subtree. *Hint: there are **5** cuts* (corrected — see below) |
| 3 | Programming: implement alpha-beta starting from `minmax.ipynb` (walked through in class — see [[CSCE 420 Fall 2026 — 09-18 minmax.ipynb Walkthrough]]); test on the tree, then on a **variant where one or more cuts no longer happen** |

**How cuts are counted** (Figure 3 on the sheet): pruning a subtree that removes several leaves at once is **one** cut, not one per leaf. The cut-count hint uses that convention.

> **Correction, now confirmed against the corrected PDF.** The originally distributed Fall 2026 sheet said *4 places*; the corrected sheet says **5 places**. The Canvas announcement ("Homework 2 correction", Yoonsuck Choe) carried an annotated screenshot with *5 places* circled in red — archived as `raw/CSCE420_HW2_Fall2026_correction.png`. Anyone working from a pre-correction download has the wrong hint. This also removes the apparent Spring-vs-Fall difference noted earlier: both semesters' hints are 5.

> **Second change in the corrected sheet**, easy to miss because the announcement only circled the cut count — Problem 2 gained a note: *"When there is a cut, the final αβ values may or may not be updated. Either way does not affect the final outcome."* So part (b) will not be marked wrong over whether you updated α/β on the pruned branch.

The Spring 2026 instructor's line applies directly: *"Always use the algorithm. If you start to reason about it in your head, you'll make errors."* Problem 2(b) — recording α, β per node — is only doable by running the Max-Value/Min-Value procedure literally.

## Part 2 — Propositional Logic (Problems 4–7, 28 pts)

Atoms P, Q, R, S, T, U, V, W. **Every derivation step must name the law used** — distributive, by definition, De Morgan, etc.

| # | Asked |
|---|---|
| 4 | Prove the [[Inference Rules\|resolution rule]] valid by truth table: `((P ∨ ¬S) ∧ (S ∨ Q)) → (P ∨ Q)` is true under all 8 interpretations. Table skeleton supplied |
| 5 | (1) `P ∨ (Q ∧ ¬R) ∨ (Q ∧ S)` → CNF. (2) `(P → Q) → (R ∨ S)` → DNF. See [[Normal Forms]] |
| 6 | Convert four premises to clauses, **negate the conclusion `Q ∨ W`**, list as C1, C2, … |
| 7 | Derive **False** by [[Resolution]] alone. *"Show every step. DO NOT USE any other inference rule."* |

The premises for 6–7: `¬(P ∨ W) → ¬S`, `S ∨ R`, `R → Q`, `R ∨ (¬P ∧ S)`.

Two traps the sheet spells out:
- One premise can yield **multiple clauses**. Their example: `¬((P ∧ ¬R) ∨ S)` becomes `(¬P ∨ R) ∧ ¬S` — two clauses, listed separately.
- The negated conclusion can yield multiple clauses too. `¬(Q ∨ W) = ¬Q ∧ ¬W` — **two** goal clauses. This is the exact tip from lecture slide 44.

## Part 3 — First-Order Logic Basics (Problems 8–12, 38 pts)

Variables w, x, y, z; constants A, B, C, D; functions f, g, h; predicates P, Q, R.

| # | Asked |
|---|---|
| 8 | Three formulas → [[Prenex Normal Form]]. The corrected sheet moves the **show-every-step-and-name-the-law** requirement into this problem explicitly (it previously sat only in the propositional section) |
| 9 | Five formulas → [[Skolemization\|skolemize]] (1 pt each) |
| 10 | Full canonical form: prenex → CNF → skolemize, for `∀x (Q(x) → ∃y (P(x,y) ∧ R(y)))` |
| 11 | Apply three [[Substitution\|substitutions]] to `P(x,y) ∨ Q(x)` |
| 12 | Four pairs: find the [[Unification\|unifier]] and the unified expression, or say *not unifiable*. **Show the disagreement set D_k and σ_k at each iteration** |

### The substitution rules the sheet lays down — memorize these

*"You can only replace a variable with something else."* With D the disagreement set and θ the substitution:

| D | Verdict |
|---|---|
| `{x, A}` | θ = {x/A} okay. **{A/x} not possible** — cannot replace a constant |
| `{f(B), A}` | no substitution — two non-variables |
| `{B, A}` | no substitution — two constants |
| `{f(x), A}` | no substitution — function vs constant |
| `{f(x), y}` | θ = {y/f(x)} okay. {f(x)/y} not possible |
| `{x, y}` | {x/y} okay **and** {y/x} okay |
| `{f(x), f(B)}` | **Your disagreement set is wrong** — go one level deeper: D = {x, B} |

The last row is the one people miss: the disagreement set is found at the *first differing symbol*, descending into matching function symbols.

### The composition rule

*The final unifier is a series of compositions.* If θ₁ = {x/y} and θ₂ = {y/A}, the correct unifier is **σ = (θ₁ ∘ θ₂) ∪ θ₂ = {x/A, y/A}**. Writing σ = {x/y, y/A} is **incorrect** — the compose step θ₁ ∘ θ₂ = {x/y} ∘ {y/A} = {x/A} was skipped. See [[Substitution]] for the composition definition, and the [[CSCE 420 Fall 2025 — Midterm Review Recording]] for the same thing checked live in Prolog.

## What It Tells You About the Midterm

All of it is midterm scope — [[CSCE 420 Midterm Review]] stops at unification, and so does this sheet. In Spring 2026 the instructor walked through the HW2 solutions in class two days before the exam and said he *"almost gave out the answers."* The written problems here — an alpha-beta trace with α/β bookkeeping, a CNF conversion with named laws, a resolution refutation, and unification with disagreement sets — are the shape of the exam.

## See Also

- [[CSCE 420 Homework 2 Solutions — Fall 2026]]
- [[CSCE 420 Fall 2026 — 09-18 minmax.ipynb Walkthrough]]
- [[CSCE 420 Midterm Review]]
- [[CSCE 420 Homework 1 — Search]]
- [[Alpha-Beta Pruning]]
- [[Resolution]]
- [[Unification]]
- [[CSCE 420]]
