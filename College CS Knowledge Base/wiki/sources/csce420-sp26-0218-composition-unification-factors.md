---
title: "CSCE 420 Spring 2026 — 02-18 Composition, Unification, Factors"
type: source
tags: [csce420, lecture-recording, spring-2026, substitution, composition, unification, mgu, disagreement-set, unification-algorithm, factors, binary-resolvent, midterm-boundary]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-02-18
deck: slide03
exam: midterm / final
updated: 2026-09-17
---

Spring 2026 lecture, 46 min. Composition of substitutions with a full worked check, the unification algorithm run to completion, and the first slides past the midterm boundary: factors and binary resolvents. Slides 03:99–118.

> **The midterm boundary is in this lecture.** *"Up to this page — page 99 — would be the range for the midterm exam… this is where the midterm exam ends."* Page 99 is the unification algorithm. Factors and resolvents that follow are **final-exam** material. See [[CSCE 420 Midterm Review]] and [[CSCE 420 Final Review]].

## Composition — When You Need It and How

Unifying P(x, f(x)) against P(f(c)) is one substitution. But when the term part of one substitution contains a variable that a later substitution binds, you need **composition** — one substitution equivalent to applying several in sequence: E θ λ = E (θ∘λ).

**Trivial case**: θ = {x/a}, λ = {y/b} → θ∘λ = {x/a, y/b}, just the union. *"It gets complicated if the term part actually includes y."*

**The rule**: apply λ to every term on θ's right-hand side; then append λ's own pairs; then **delete** any xⱼ/xⱼ (a variable replaced by itself does nothing) and any of λ's pairs whose variable already appears on θ's left (it is already gone from the expression by the time λ would act).

**Worked**: θ = {x/f(y), y/z}, λ = {x/a, y/b, z/y}.
Apply λ to θ's terms: f(y)λ = f(b); zλ = y → {x/f(b), y/y}. Append λ: {x/a, y/b, z/y}. Delete: y/y (self); x/a and y/b (x and y already in θ). **Result: θ∘λ = {x/f(b), z/y}.**

**Checked on E = P(x, y, z)**: E θ = P(f(y), z, z); then λ → P(f(b), y, y). Directly, E (θ∘λ) = P(f(b), y, y). Same. See [[Substitution]].

## Unification

θ is a **unifier** for {E₁…Eₖ} iff applying it to all of them yields a single expression. The **most general unifier** σ is the minimal one: every unifier θ = σ∘λ for some λ.

Examples he ran: P(x, g(x)) vs P(x, y) → {y/g(x)}. P(x, g(x)) vs P(z, g(z)) → **either** {x/z} or {z/x} — *"equally the same unifier."* P(x, g(x)) vs P(g(y), z) → first x/g(y), then z/g(g(y)) — *"this is when you need composition"* → {x/g(y), z/g(g(y))}. P(Socrates, g(Socrates)) vs P(Socrates, f(Socrates)) → **not unifiable**: *"you have f and g, which are functions, non-variable terms. You cannot replace a term with a term."*

### The disagreement set is at the symbol level

Scan left to right to the **first symbol** that differs, and descend into matching function symbols. For P(x, f(g(h(y)))) vs P(x, f(g(z))): the disagreement set is **{h(y), z}**, *not* the whole second arguments. *"It's computed not at the argument boundary but at the symbol boundary."* This is exactly HW2's *"your disagreement set is incorrect — go one level deeper"* rule. *"It's always best to write the expressions down vertically."*

### The algorithm

W₀ = the expressions (rename any shared variable names first); σ₀ = {}. Loop: if Wₖ is a singleton, stop — σₖ is the MGU. Else find Dₖ; pick a **variable vₖ and a term tₖ in which vₖ does not occur**; σₖ₊₁ = σₖ ∘ {vₖ/tₖ}; Wₖ₊₁ = Wₖ{vₖ/tₖ}.

**Terminates** because each pass eliminates one variable and there are finitely many. He corrected himself mid-explanation: *"I was a little bit incorrect — we are not reducing entire expressions into one; you're removing one variable at a time."*

**Worked to the end**: W₀ = {P(x, f(x,z)), P(g(y), f(g(a), y))}.
D₀ = {x, g(y)} → {x/g(y)}; W₁ = {P(g(y), f(g(y), z)), P(g(y), f(g(a), y))}.
D₁ = {y, a} → {y/a}; σ₂ = {x/g(a), y/a} (composition updates x's term); W₂ = {P(g(a), f(g(a), z)), P(g(a), f(g(a), a))}.
D₂ = {z, a} → {z/a}; W₃ singleton. **MGU σ₃ = {x/g(a), y/a, z/a}.** See [[Unification]].

## Past the Boundary: Factors and Resolvents

In FOL the same predicate can appear more than once in a clause *without* the literals being identical: P(x) ∨ P(f(y)) ∨ ¬Q(x). Unify the two P-literals with {x/f(y)} to get the **factor** P(f(y)) ∨ ¬Q(f(y)) — *"you can reduce it to a single predicate, but not directly; there's a step where you need to find a unifier."*

**Binary resolvent**: find L₁ in C₁ and L₂ in C₂ such that L₁ and ¬L₂ unify with σ; apply σ to **both clauses**; drop the now-identical complementary pair; union the rest. For P(x) ∨ Q(x) and ¬P(a) ∨ R(y): σ = {x/a} → Q(a) ∨ R(y). *"It doesn't matter whether you apply the negation to L₁ or L₂."* Clauses as **sets of literals** make the union notation precise. See [[Resolvents and Factors]].

## See Also

- [[CSCE 420 Spring 2026 — 02-16 Standard Form, Skolemization]]
- [[CSCE 420 Spring 2026 — 02-20 FOL Resolution, Strategies]]
- [[Unification]]
- [[Resolvents and Factors]]
- [[CSCE 420 Midterm Review]]
- [[CSCE 420]]
