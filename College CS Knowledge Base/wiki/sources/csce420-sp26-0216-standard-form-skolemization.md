---
title: "CSCE 420 Spring 2026 — 02-16 Standard Form, Skolemization"
type: source
tags: [csce420, lecture-recording, spring-2026, prenex, quantifier-equivalences, skolemization, skolem-function, used-car-dealer, substitution, closed-world]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-02-16
deck: slide03
exam: midterm
updated: 2026-09-17
---

Spring 2026 lecture, 49 min. Midterm scope announced, closed-world evaluation, prenex normal form with the quantifier equivalences, skolemization motivated by a hand proof, and the start of substitution. Slides 03:73–100.

## Midterm Scope, Stated at the Top

HW2 due Sunday; midterm **Friday March 6**, right before spring break. The practice exam is *"2 pages back and forth, 10 questions"*, and the real one adds **first-order logic basics** — *"right before we go into the full-blown resolution theorem proving"* in FOL. **"Everything that appears on your homework 2 has potential for appearing on the midterm as well."** Full scope on [[CSCE 420 Midterm Review]].

## Closed World: What Is Man(Alice)?

Given only the listed facts (Woman(Carol), Woman(Alice), Man(Bob), Man(Ted), …), a student was asked the truth value of Man(Alice). **False** — *"anything that is not stated evaluates to false."* And note: the Man predicate says nothing about Woman. *"It doesn't directly say that if you're a man you cannot be a woman. Something like that you have to write as a rule"* — e.g. ∀x Man(x) → ¬Woman(x). Two lessons: absence is falsity, and mutual exclusion is never implicit.

Consistency, inconsistency, validity, invalidity are as in propositional logic — but *"many domains are infinite, so you cannot really find the truth value in general. It's not even decidable."*

## Prenex Normal Form — The Equivalences, and Which Connective

- **(Qx F(x)) ∨ G = Qx (F(x) ∨ G)** when G has no x — just widen the scope. Same for ∧.
- **Negation over a quantifier flips it** as it moves inside.
- **∀x F(x) ∧ ∀x G(x) = ∀x (F(x) ∧ G(x))** — *"the connective in the middle is very important. It can only be conjunction to merge universal quantifiers."* Dually, ∃ merges only over **∨**.
- **The safe move**: when the two quantified variables share a name, **rename the second to z** and pull both out: Q₁x Q₂z (F(x) ∨ H(z)). *"The good thing is this works for both disjunction and conjunction. The recommendation is to just use this."*

Why ∀x F(x) ∨ ∀x G(x) ≠ ∀x (F(x) ∨ G(x)): the right side is satisfied by a domain where F holds on one half and G on the other; the left requires one of them to hold everywhere. The board version got tangled — *"you can watch the recording to figure that out."* See [[Prenex Normal Form]].

**Worked**: (∀x P(x)) → (∃y Q(y)) → ¬(∀x P(x)) ∨ ∃y Q(y) → (∃x ¬P(x)) ∨ ∃y Q(y) → **∃x ∃y (¬P(x) ∨ Q(y))**. *"If you don't have any negation outside any quantifier, you can just move everything to the front, however complex."*

## Skolemization — Motivated Before Defined

**Used-car dealers.** Premises ∀x (U(x) → ¬B(x)) and ∃x (B(x) ∧ D(x)); prove ∃x (D(x) ∧ ¬U(x)). *"I don't have anything against this occupation — it's the textbook example."*

First he did it **ignoring the quantifiers** as propositional: ¬U ∨ ¬B, B, D, negated goal ¬D ∨ U → resolve to False in three steps. *"Straightforward. But here you have quantifiers. How do you know that someone exists? We don't know who that is."*

Then the hand proof: the ∃ line says there is *someone* with B and D — *"let's just randomly name this person A."* Now B(A) and D(A) are true. The ∀ line applies to everyone, **including A** — *"even though it's a universal quantifier, we can just retrieve one example"* — so U(A) → ¬B(A). Since B(A) is true, ¬U(A). With D(A): D(A) ∧ ¬U(A), which is the witness the conclusion asks for.

*"What we did effectively is replace this existentially quantified variable with an anonymous constant that supposedly satisfies this. That's called the Skolem constant."*

### The rule and the example

Replace each ∃xᵣ by a **function of all universally quantified variables to its left**; if none, a **constant**. *"Use a different symbol every time."* On ∃x ∀y ∀z ∃u ∀v ∃w P(x,y,z,u,v,w): x → a; u → f(y,z); w → g(y,z,v). See [[Skolemization]].

### Why a function, with the people diagram

∃x ∀y Loves(x,y) skolemizes to Loves(a, y): *"A loves everyone, including himself or herself."* ∀y ∃x Loves(x,y) skolemizes to Loves(f(y), y): for each y, *"someone else, which is a function of y."* On the diagram: who loves y₅? y₂ — so f(y₅) = y₂; f(y₇) might also be y₂. *"You don't need to know the exact detail about this function. Once you claim this is true, there must be some f you don't know about."* Skolemization preserves the meaning **without** requiring the witness to be identified.

**Canonical form**: since every remaining variable is universal, *"you don't need to write ∀x — for any variable it's assumed."* Just the clauses.

## Resolution in FOL Needs Unification

Redoing the used-car proof in canonical form: ¬B(x) and B(A) are **not** complementary — *"the argument is different."* Replace x with A, *"and you have to do that for every other occurrence of x in the same clause,"* then resolve. That replacement is [[Unification]], the last piece before FOL resolution.

## Substitution — What Is and Isn't One

{v₁/t₁, …} — **variable on the left, term on the right**. A term is a constant, variable, or function. So {x/y}, {x/f(y)}, {x/Tom} are substitutions; **{Tom/f(x)} is not** — *"you can't replace a constant with something else. You can only replace a variable."* Applying θ = {x/a, y/f(b), z/c} to P(x,y,z) gives P(a, f(b), c). See [[Substitution]].

## See Also

- [[CSCE 420 Spring 2026 — 02-13 HW2 Walkthrough, First-Order Logic]]
- [[CSCE 420 Spring 2026 — 02-18 Composition, Unification, Factors]]
- [[Skolemization]]
- [[Prenex Normal Form]]
- [[CSCE 420]]
