---
title: "CSCE 420 Spring 2026 — 02-13 HW2 Walkthrough, First-Order Logic"
type: source
tags: [csce420, lecture-recording, spring-2026, hw2, minmax-ipynb, first-order-logic, predicates, functions, quantifiers, howling-hounds, interpretation, scope]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-02-13
deck: slide03
exam: midterm
updated: 2026-09-17
---

Spring 2026 lecture, 51 min. A walkthrough of the HW2 sheet and starter notebook, the limits of propositional logic, and first-order logic through domain, interpretation, and the Bob/Carol/Ted/Alice evaluation. Slides 03:49–76.

## HW2 Walkthrough (Spring 2026 version)

**Notebook `minmax.ipynb`**: the game tree is a nested list; ±∞ are `9999` / `-9999`; the provided `minmax` is correct and can be used to check Problem 1. It prints with an **indent string** that grows two characters per recursive call, so the call sequence is readable. Task: *"write two functions, the max-value function and the min-value function."*

**Written problems**: Problem 4 is a plain truth table to show the resolution rule is valid. Problem 6 — *"don't forget to negate the conclusion before adding it to the clauses."* When a negated premise yields (¬P ∨ R) ∧ ¬S, that is **two clauses on two lines**. **Associative law**: P ∨ (Q ∨ R) is one clause regardless of parentheses — drop them. **Reuse clauses**: ¬P can resolve with both (P ∨ Q) and (P ∨ R); *"crossing it out doesn't completely get rid of it."*

Spring's tree had **5 cuts**; the Fall 2026 sheet says 4. See [[CSCE 420 Homework 2 — Game Playing, Logic]].

## The Limit of Propositional Logic

All men are mortal (P), Socrates is a man (Q), Socrates is mortal (R) — each true, but *"there's nothing that would link them. We cannot decompose any of these."* (P ∧ Q) → R is unprovable. First-order logic *"lets you break it down."* The predicate-calculus treatment follows a textbook he *"read in my graduate student days as part of an AI course"* — Chang & Lee.

## "Term" Means Two Different Things

Stated explicitly, and worth memorizing because the collision is real:

| Context | "Term" means |
|---|---|
| [[Normal Forms]] | a **conjunction of literals** (P ∧ ¬Q ∧ R) — has a truth value |
| [[First-Order Logic]] | an **object** in the domain — a constant, variable, or function application — has **no** truth value |

*"This term is not the same as this. In first-order logic, terms are objects in the domain. It doesn't tell you anything about true or false."*

## Predicates vs. Functions — The Practical Test

Predicates take terms and return **True/False**; functions take terms and return **a term**. For an ambiguous name like Brother(x, y): *"If it appears standalone, it's a predicate, because it has to be true or false. If it's used as an argument in a function or predicate, it's a function, because it's a term."*

**Socrates, proved**: ∀x Man(x) → Mortal(x) holds for every x in the domain, so instantiate x = Socrates to get Man(Socrates) → Mortal(Socrates); modus ponens with Man(Socrates) gives Mortal(Socrates). The universal quantifier is what licenses the instantiation.

## Quantifier Mistakes, With a Domain Drawing

Domain: himself, the students, Mr. and Ms. Skunk, Snoopy.

- **∀x Skunk(x) ∧ Stinky(x)** — *"This says I'm a skunk and I'm stinky. You are a skunk and you're stinky. Snoopy is a skunk and stinky. This is incorrect."* Correct: ∀x Skunk(x) → Stinky(x).
- **∃x Cat(x) → White(x)** — a student asked why this is wrong. Plug in himself: Cat(me) is false, and *"False implies anything is True"* — so the sentence is true because of a non-cat. Correct: ∃x Cat(x) ∧ White(x), made true by Snowy the white cat.

**∀y ∃x vs. ∃x ∀y**, with a people diagram: ∃x ∀y Loves(x, y) — one person x₃ who loves everyone, *"and actually you have to love yourself."* ∀y ∃x Loves(x, y) — go through every y and check someone loves them, possibly themselves; fails if any y is loved by nobody. **Very different meanings.**

**Quantifier negation**: double-negate, move one negation inward, and **flip the quantifier** as it passes: ∀x Likes(x, Coffee) = ¬∃x ¬Likes(x, Coffee).

## Howling Hounds — Common Sense First

Before translating, he reasoned it in English: John is a light sleeper → has nothing that howls → hounds howl → no hound → but he has a cat or a hound → so a cat → cat-owners have no mice → **no mice**. Then the FOL translation, with the point that **variables link predicates**: the Y that John has is *the same* Y that is a cat; *"we are able to link multiple different predicates using the variables."* He does not have the full resolution proof for this one on the slides.

## Standard Form Preview

Three steps: prenex normal form (quantifiers to the front), CNF on the **matrix** (the quantifier-free part), [[Skolemization]] to remove existentials. Result: all remaining variables universally quantified.

## Domain, Interpretation, Scope

- The **domain** is the set of constants. In the kinship axioms, Mother(c) = m is a **function**; Female(m), Parent(m, c) are predicates.
- **Interpretation**: constants → elements of D, n-ary functions → Dⁿ → D, n-ary predicates → Dⁿ → {T, F}. ∀x G true iff G holds for all x in D; ∃x G iff for some x.
- **Scope and bound variables**: *"these are the only concepts you need to remember from this slide."* Free variables *"we won't discuss, because we're not going to use it."*

## Bob, Carol, Ted, Alice

Bob loves Carol, Ted loves Alice, Carol loves Ted — *"it's getting bad"* — Bob and Ted are brothers, Alice is Carol's boss. Evaluate ∀x (Man(x) → ∃y (Woman(y) ∧ Loves(x, y))): Bob → Carol ✓, Ted → Alice ✓; for Alice and Carol, Man(x) is false so the implication is **vacuously true**. All four hold → the formula is **true** under this interpretation. The vacuous case is the same False → anything = True rule as above.

## See Also

- [[CSCE 420 Spring 2026 — 02-11 Normal Forms, Logical Consequence, Resolution]]
- [[CSCE 420 Spring 2026 — 02-16 Standard Form, Skolemization]]
- [[First-Order Logic]]
- [[CSCE 420 Homework 2 — Game Playing, Logic]]
- [[CSCE 420]]
