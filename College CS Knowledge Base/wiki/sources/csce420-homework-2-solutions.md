---
title: "CSCE 420 Homework 2 Solutions — Fall 2026"
type: source
tags: [csce420, homework, hw2, solutions, answer-key, minimax, alpha-beta, resolution, cnf, prenex, skolemization, unification, fall-2026]
sources: []
course: CSCE 420
semester: Fall 2026
exam: midterm
updated: 2026-11-04
---

The **instructor's official released answer key** for Fall 2026 Homework 2, posted after the due date. Archived as `raw/CSCE420_HW2_Fall2026_solutions.docx`. The assignment itself — asks, conventions, and the 4→5 cut correction — is at [[CSCE 420 Homework 2 — Game Playing, Logic]].

> **This is the released key, not derived work.** Where it differs from your own working, the key is what the midterm grades against. It also **settles the cut-count correction**: the key lists **five** cuts explicitly, confirming the corrected sheet.

## Game Playing (Problems 1–3)

**P1 — minimax.** Values propagate from the leaves: MAX takes the largest child, MIN the smallest. **Root value 4**, optimal path *root → left MIN → left MAX → leaf 4*. Internal values from the key's figure, left to right:

| Level | Values |
|---|---|
| Root (MAX) | 4 |
| MIN | 4, 3 |
| MAX | 4, 7, 8, 3, 8 |
| Lower MIN | MIN[2,8] = 2; MIN[5,7,1] = 1; MIN[3,7] = 3; MIN[3,6,4] = 3; MIN[8,1,9] = 1; MIN[3,4] = 3 |

**P2 — alpha-beta.** Root starts α = −∞, β = +∞. The minimax value is still **4**; pruning skips five subtrees or leaf groups. **The five cuts, in left-to-right search order** (node ids as marked on the key's figure):

| # | Where | Trigger | Pruned |
|---|---|---|---|
| 1 | MIN[2, 8] (node 7) | saw 2 with **α = 3** | remaining leaf 8 |
| 2 | MAX node containing 3 (node 5) | got 7 with **β = 4** | the whole MIN[5, 7, 1] subtree |
| 3 | MAX[8, MIN[3,7]] (node 15) | saw 8 with **β = 4** | MIN[3, 7] |
| 4 | MIN[3, 6, 4] (node 22) | saw 3 with **α = 4** | leaves 6 and 4 |
| 5 | right MIN child of root | left MAX child (node 21) returned 3 while **α = 4** | the entire remaining right MAX subtree |

Cuts 1 and 4 prune *leaves*; 2, 3 and 5 prune *subtrees* — but under the sheet's counting convention each is **one** cut regardless of how many leaves it removes. Optimal path unchanged from P1.

**Final α and β at every visited node**, from the key's figure. Ids are the key's pre-order numbering. Pruned and never visited: 9; 11–14; 17–19; 24–25; 27–35.

| Id | Node | α | β | Returns |
|---|---|---|---|---|
| 0 | root MAX | 4 | +∞ | 4 |
| 1 | MIN | −∞ | 4 | 4 |
| 2 | MAX | 4 | +∞ | 4 |
| 3 | leaf 1 | −∞ | +∞ | 1 |
| 4 | leaf 4 | 1 | +∞ | 4 |
| 5 | MAX | 3 | 4 | 7 |
| 6 | leaf 3 | −∞ | 4 | 3 |
| 7 | MIN | 3 | 4 | 2 |
| 8 | leaf 2 | 3 | 4 | 2 |
| 10 | leaf 7 | 3 | 4 | 7 |
| 15 | MAX | −∞ | 4 | 8 |
| 16 | leaf 8 | −∞ | 4 | 8 |
| 20 | MIN | 4 | +∞ | 3 |
| 21 | MAX | 4 | +∞ | 3 |
| 22 | MIN | 4 | +∞ | 3 |
| 23 | leaf 3 | 4 | +∞ | 3 |
| 26 | leaf 2 | 4 | +∞ | 2 |

The key does **not** update α or β at a node on the step that causes its cut: node 5 returns 7 but keeps α = 3, and node 20 returns 3 but keeps β = +∞. The corrected sheet says either way is acceptable. See [[Alpha-Beta Pruning]].

**P3 — programming, and the required variation.** *"Any correct implementation."* The key's own variation and the reasoning behind it:

| Test | Change | Root value | Cuts |
|---|---|---|---|
| Original Figure 1 | none | 4 | **5** |
| Variation | replace MIN[3, 6, 4] with **MIN[5, 6, 4]** | 4 | **4** |

Why it works: in the original, MIN[3,6,4] arrives with α = 4 and cuts immediately on seeing 3. With MIN[5,6,4] the node must examine all three children before its value reaches 4, **so no child remains to prune**. *"Any reasonable alternatives are acceptable."*

## Propositional Logic (Problems 4–7)

**P4 — resolution rule validity.** The 8-row truth table for `((P ∨ ¬S) ∧ (S ∨ Q)) → (P ∨ Q)` has the implication column **true in every row** — valid. The rows that could break it are the two where P ∨ Q is false (P = F, Q = F, with S either way). In both, the antecedent is false, so the implication holds.

**P5 — normal forms, with named laws.**

```
P ∨ (Q ∧ ¬R) ∨ (Q ∧ S)
= P ∨ [Q ∧ (¬R ∨ S)]              distributive law
= (P ∨ Q) ∧ (P ∨ ¬R ∨ S)          distributive law; associative law
```
```
(P → Q) → (R ∨ S)
= ¬(P → Q) ∨ R ∨ S                implication
= ¬(¬P ∨ Q) ∨ R ∨ S               implication
= (P ∧ ¬Q) ∨ R ∨ S                De Morgan's law
```

**P6 — clause set.** Premise 1 `¬(P ∨ W) → ¬S` becomes `P ∨ W ∨ ¬S`; premise 4 `R ∨ (¬P ∧ S)` distributes into **two** clauses; the negated conclusion `¬(Q ∨ W) = ¬Q ∧ ¬W` gives **two more**:

| | |
|---|---|
| C1 | `P ∨ W ∨ ¬S` |
| C2 | `S ∨ R` |
| C3 | `¬R ∨ Q` |
| C4 | `R ∨ ¬P` |
| C5 | `R ∨ S` |
| C6 | `¬Q` |
| C7 | `¬W` |

**P7 — refutation, resolution only.**

| New | Step | Result |
|---|---|---|
| C8 | C3 + C6 on Q | `¬R` |
| C9 | C2 + C8 on R | `S` |
| C10 | C1 + C9 on S | `P ∨ W` |
| C11 | C10 + C7 on W | `P` |
| C12 | C4 + C11 on P | `R` |
| C13 | C8 + C12 on R | **⊥** |

The empty clause is derived, so `Q ∨ W` is a logical consequence. Note C5 is never used — a clause set can carry clauses the proof does not need. See [[Resolution]].

## First-Order Logic (Problems 8–12)

**P8 — prenex normal form.**

| # | Result |
|---|---|
| 1 | `∃x∀y (P(x) ∧ Q(x,y))` |
| 2 | `∀x∀y (¬P(x,y) ∨ Q(x))` |
| 3 | `∃x∀y (Q(x,y) ∧ P(x))` |

Laws named at each step: **quantifier negation**, **De Morgan's**, `¬(A → B) ≡ A ∧ ¬B`, then **move quantifier outward**.

**P9 — skolemization.** *"Any fresh Skolem constants or function names are equivalent."*

| # | Input | Skolemized |
|---|---|---|
| 1 | `∀x∃y∃z (P(x,y) ∧ Q(y,z))` | `∀x (P(x,f(x)) ∧ Q(f(x),g(x)))` |
| 2 | `∀x∃y P(x,y)` | `∀x P(x,f(x))` |
| 3 | `∀x∀y∃z (P(x,y) ∧ Q(y,z))` | `∀x∀y (P(x,y) ∧ Q(y,f(x,y)))` |
| 4 | `∃x P(x)` | `P(A)` |
| 5 | `∃x∃y∀z (P(x,y) ∧ Q(y,z))` | `∀z (P(A,B) ∧ Q(B,z))` |

The rule the table encodes: an existential **inside** universals becomes a **function of those universals** (#1, #2, #3); an existential with **no** universal to its left becomes a **constant** (#4, #5). See [[Skolemization]].

**P10 — full canonical form** of `∀x (Q(x) → ∃y(P(x,y) ∧ R(y)))`: eliminate implication → prenex `∀x∃y (¬Q(x) ∨ (P(x,y) ∧ R(y)))` → distribute → skolemize `y = f(x)`:

`∀x [(¬Q(x) ∨ P(x,f(x))) ∧ (¬Q(x) ∨ R(f(x)))]`, i.e. clauses `{ ¬Q(x) ∨ P(x,f(x)),  ¬Q(x) ∨ R(f(x)) }`.

**P11 — substitutions** applied to `P(x,y) ∨ Q(x)`: `{x/A, y/f(z)}` → `P(A,f(z)) ∨ Q(A)`; `{x/f(A)}` → `P(f(A),y) ∨ Q(f(A))`; `{x/f(z), y/B}` → `P(f(z),B) ∨ Q(f(z))`.

**P12 — unification, showing D_k and σ_k.**

1. `P(x,f(y),y)` / `P(A,f(g(w)),g(A))`: D₁ = {x, A}, D₂ = {y, g(w)}, D₃ = {w, A} → **σ = {x/A, y/g(A), w/A}**, unified `P(A,f(g(A)),g(A))`. Note σ₂ held `y/g(w)` but the final σ shows **`y/g(A)`** — the composition step propagating `w/A` back through, which is exactly the compose rule the sheet warns about.
2. `P(A,f(y),y,A)` / `P(x,f(g(x)),g(B),w)`: D₁ = {x, A}, D₂ = {y, g(A)}, then **D₃ = {A, B}** — two distinct constants, no substitution possible → **not unifiable**.
3. `P(x,f(B))` / `P(A,f(y))`: D₁ = {x, A}, D₂ = {y, B} → σ = {x/A, y/B}, unified `P(A,f(B))`.
4. `P(x,f(A))` / `P(y,y)`: D₁ = {x, y}, θ₁ = {x/y} (the key notes {y/x} is also possible). D₂ = {y, f(A)}, θ₂ = {y/f(A)}. **σ₂ = (σ₁ ∘ θ₂) ∪ θ₂ = {x/f(A), y/f(A)}**, unified `P(f(A),f(A))`. This is the compose rule from the sheet, applied in full.

See [[Unification]].

## See Also

- [[CSCE 420 Homework 2 — Game Playing, Logic]]
- [[CSCE 420 Homework 1 Solutions — Fall 2026]]
- [[CSCE 420 Midterm Review]]
- [[Alpha-Beta Pruning]]
- [[Resolution]]
- [[Unification]]
- [[CSCE 420]]
