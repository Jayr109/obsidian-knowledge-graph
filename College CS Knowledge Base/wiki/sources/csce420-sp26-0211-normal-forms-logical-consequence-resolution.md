---
title: "CSCE 420 Spring 2026 — 02-11 Normal Forms, Logical Consequence, Resolution"
type: source
tags: [csce420, lecture-recording, spring-2026, horn-clauses, cnf, absorption, logical-consequence, forward-chaining, backward-chaining, resolution, unicorn]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-02-11
deck: slide03
exam: midterm
updated: 2026-09-17
---

Spring 2026 lecture, 50 min. Horn clauses, CNF conversion including the absorption shortcut, logical consequence and the refutation theorem, the three theorem-proving methods, and the unicorn example done by resolution and then by hand. Slides 03:19–48.

## Horn Clauses — The Edge Cases

*"One or fewer positive literals."* So a single positive literal **G** is a Horn clause, and a single negative literal **¬H** is too (zero positive literals qualifies). Horn Normal Form is a conjunction of Horn clauses, hence **every Horn normal form is also CNF** — CNF with a stricter clause type. The restriction is what makes the implication reading clean: with only one positive literal, it becomes the conclusion and *"the left part of the implication is a conjunction of only positive literals."* See [[Horn Clauses]].

He repeated: *"Don't confuse the formula F with the constant False. I always write False explicitly."*

## CNF Conversion — Absorption Saves Work

Converting (P ∧ Q) ∨ (P ∧ R) by distributing *forward* gives four clauses, (P ∨ P) ∧ (P ∨ Q) ∧ (P ∨ R) ∧ (Q ∨ R). Distributing *backward* gives **P ∧ (Q ∨ R)** directly. Both are correct CNF; the second is simpler. He showed they are equivalent using **absorption**: P ∧ (P ∨ Q) = P, argued by cases — *"regardless of Q, this has the value of P."*

**Grading note**: *"If you wrote that [four clauses], I would say okay, that's good. If you wrote that [two clauses], of course that's good — a little bit less elegant."* Either form earns credit; both are logically equivalent. See [[Normal Forms]].

## Logical Consequence and Refutation

G is a logical consequence of F₁…Fₙ iff (F₁ ∧ … ∧ Fₙ) → G is **valid** — a **theorem**, with **axioms/premises** and a **conclusion**. Modus ponens is the template: with F₁ = F and F₂ = F → G, the theorem (F₁ ∧ F₂) → G is valid.

Then the pivot: **H valid ⟺ ¬H inconsistent**, worked on P ∨ ¬P (valid on both rows; its negation false on both). Applied to the theorem, ¬H = F₁ ∧ … ∧ Fₙ ∧ **¬G**. *"That's kind of trivial, but this is a very important thing — turning the first definition into the second makes it very easy to do automated theorem proving."*

**False premises prove anything**: *"If any formula on the premise side is false, False → G is True regardless of what you have in the conclusion."* A KB must be consistent. See [[Logical Consequence]].

## Three Ways to Prove — With Their Weaknesses

**Forward chaining** on the A, B, D / A∧B→C / C∧D→E example. Why C must be true: if A∧B is true and C false, the rule True → False is False, *"which would invalidate your knowledge base."* The weakness: with many rules, *"the order of generating new facts — your performance depends on that"*, and *"you'll generate many new facts that are not used toward your final generation of E."*

**Backward chaining**: check whether E is a fact; if not, find rules with E on the right-hand side; recursively check their preconditions. Less waste — but *"this assumed you had only one positive literal on the right-hand side. These are all Horn clauses."* He then said the key sentence: **"In general we don't want to limit our representational power. That's when resolution comes in."** See [[Forward and Backward Chaining]].

## Resolution — Mechanics and the One Rule People Break

Negate the conclusion and add it to the clauses. **A negated conclusion can produce several clauses**: negating P ∨ ¬Q gives ¬P ∧ Q — *two lines*, ¬P and Q. **"If you have any conjunction in any of these lines, you're doing something wrong."** This is the tip repeated in HW2 Problem 6.

**Why the method is sound**: each resolvent is a logical consequence of two existing clauses, so *"the truth value of the original set is the same as the truth value with the new clause added."* Derive False, and the whole conjunction — premises ∧ ¬G — is False, i.e. inconsistent, i.e. G follows. The caveat again: C₁ ∧ C₂ ∧ H = C₁ ∧ C₂, but **not** C₁ ∧ C₂ = H.

**Clauses are reusable.** In the unicorn proof clause 5 (¬H) resolves against both 3a and 3b. *"Even though I crossed it out, you can reuse it as need be."*

## The Unicorn — Translation Decisions

Propositions: M mythical, I immortal, L mammal, H horned, G magical. Two decisions worth noticing: **"mortal" is ¬I, not a new atom**; and *"the unicorn is magical if it is horned"* must be read with word order reversed — **H → G**, not G → H. Premise 2, ¬M → (¬I ∧ L), becomes two clauses (M ∨ ¬I), (M ∨ L); premise 3 becomes (¬I ∨ H), (¬L ∨ H). Proof: 3a+5 → ¬I; 3b+5 → ¬L; 2b+7 → M; 1+6 → ¬M; 8+9 → **False**.

## Why He Then Did It Again by Hand

*"It all looks nice and neat, but we don't get any human-level intuition from it."* The alternative proof: contrapositive of M → I, transitivity with premise 2 to get ¬I → (¬I ∧ L), distribute and simplify to I ∨ L, then **modus ponens** with (I ∨ L) → H. *"This is a little bit easier for us to understand — but it's not easy to see the underlying logic [in resolution]. That's one issue with resolution."* Recorded on [[Resolution]] as the readability disadvantage.

## See Also

- [[CSCE 420 Spring 2026 — 02-09 Knowledge Bases, Propositional Logic]]
- [[CSCE 420 Spring 2026 — 02-13 HW2 Walkthrough, First-Order Logic]]
- [[Resolution]]
- [[Logical Consequence]]
- [[CSCE 420]]
