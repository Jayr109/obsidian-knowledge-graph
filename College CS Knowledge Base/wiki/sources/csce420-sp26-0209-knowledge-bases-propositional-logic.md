---
title: "CSCE 420 Spring 2026 — 02-09 Knowledge Bases, Propositional Logic"
type: source
tags: [csce420, lecture-recording, spring-2026, knowledge-base, soundness, completeness, propositional-logic, interpretation, validity, inference-rules, normal-forms]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-02-09
deck: slide03
exam: midterm
updated: 2026-09-17
---

Spring 2026 lecture, 50 min. The representation hypothesis, knowledge-based systems, soundness vs. completeness explained with a diagram, the types-of-logic table, and propositional logic from syntax through the definition of clauses and terms. Slides 03:4–21.

## Why Logic Is "Slow" — The Sentence That Explains It

The slide lists slowness as a weakness of logic. His explanation: *"You think of logic as more advanced than search — when you think logically you expect it to be more efficient. But when you implement theorem proving on a computer, it turns into a search problem: which logical expressions to combine to generate something new, and keep doing that until you generate the desired result."* Automated reasoning **is** search over derivations. That is the bridge from slide02 to slide03.

Frames, by contrast: *"very similar to object-oriented programming"* — procedural attachment means *"when a certain value is set, it triggers some action; when there's a need, it pulls values from other entities."* Neural networks are the sub-symbolic alternative: a high-level symbol *"is spread out across multiple neurons as a vector embedding"* — a **distributed** representation. See [[Knowledge Representation]].

## Knowledge-Based Systems

The inference engine is **domain-independent**: *"It could be a medical knowledge base, an engineering knowledge base, or even a military knowledge base — regardless of the application, you don't need to change the inference engine."* The KB is **declarative**: *"Instead of writing line-by-line code telling it how to retrieve something, you just tell it: here are the facts and rules from my domain, and I want something like this."*

**Semantics is narrow here.** In natural language, semantics means meaning at every level; *"in logic we use a very narrow definition — whether a sentence written in the syntax is true or false."* See [[Knowledge Base Systems]].

## Sound vs. Complete — The Diagram

Draw the set of all sentences derivable from a KB, and inside it the true ones.

- **Sound** inference procedure (IP₁): everything it generates is true. It *may miss* some true sentences — that is still sound. *"There's no way it can generate false sentences."*
- **Complete** inference procedure (IP₂): it generates *all* the true sentences. Its blind spot: *"in that process it can generate some false sentences."*

*"Each has pros and cons. In general you want an inference procedure that is both sound and complete"* — generates every true sentence and no false one. [[Resolution]] is both. See [[Logical Inference]].

## Types of Logic — Ontology vs. Epistemology

**Ontology** is the philosophy of what exists — *"is it only material, only mental, or both?"* Here, narrowly: what the logic can represent. **Epistemology** is about knowledge — what can we know about it.

The temporal row got an example: *"I am alive — true right now, but not before my date of birth, and not after I die."* First-order logic cannot express that a fact's truth changes over time; that needs **temporal logic**, which *"becomes very complicated."* Probability theory: facts as random variables with a **degree of belief**. Fuzzy logic: **degree of truth** itself.

## Propositional Logic

- **Atoms** are natural-language statements that are true or false but not both — *"I am alive."*
- **Precedence**: ¬ first; then ∧ and ∨ (equal); then → and ↔ last. *"In most cases I will put explicit parentheses in homeworks and exams so it's not ambiguous."*
- **Interpretation** = one truth assignment; n atoms → 2ⁿ rows of the truth table. Worked: P ∨ ¬Q ∧ R under (T, T, T) is true.
- **Valid**: P ∨ ¬P, checked on both rows. **Inconsistent**: P ∧ ¬P. Then **G valid ⟺ ¬G inconsistent**, shown by De Morgan: ¬(P ∨ ¬P) = ¬P ∧ P. *"This is true for any complex expression, not just one atom."*
- Don't confuse the formula F with the constant **False**.

### Laws, with his asides

- **Distributive law confuses people** because of arithmetic: A·(B+C) = AB + AC is familiar, but **A + B·C = (A+B)(A+C) is false in arithmetic and fine in logic** — *"if you are too fixated on that it's confusing, but this is perfectly fine in logic."*
- Identity and universal bound: verify by plugging in both values of F. F ∧ False is False *"regardless of this value."*
- **Implication**: F → G ≡ ¬F ∨ G, verified by truth table. *"A lot of you have an issue: why is False → True true, and False → False true? I guess you can look it up — this is how it is."*

### Inference rules, derived not stated

- **Modus ponens** two ways. Short: F → G is ¬F ∨ G; F true makes ¬F false; so G must be true *"and that's exactly what we wanted."* Long: negate the whole rule and algebraically reduce to True — *"the hard way,"* and it got longer than he expected on the board.
- **Unit resolution is modus ponens in disguise**: rewrite ¬G ∨ F as G → F and the two rules line up term for term. A **literal** is an atom or its negation *"without any baggage"*; a **complementary pair** is what resolution cancels.
- **Resolution is transitivity of implication**: F ∨ G and ¬G ∨ H become ¬F → G and G → H, yielding ¬F → H. *"A lot of these are equivalent to each other."* See [[Inference Rules]].

**Why normal forms**: with a KB of facts and rules, you generate new sentences until the query appears. *"Complex expressions with implications are not good for that. We want to make it simpler, so we can quickly identify: there's just one pair of complementary literals, get rid of them, generate a new one."* See [[Normal Forms]].

### Clauses and terms — the "one or more" trap

A **clause** is a disjunction of *one or more* literals; a **term** is a conjunction of one or more. So a single literal **P is both a clause and a term**. And **P ∨ Q is both CNF and DNF**: as CNF it is one clause; as DNF it is two single-literal terms joined by ∨. *"The exercise asks why — and I actually just gave you the answer."* It is the *main connective* that decides the form.

## See Also

- [[CSCE 420 Spring 2026 — 02-06 Chance Games, Game AI History, Logic Intro]]
- [[CSCE 420 Spring 2026 — 02-11 Normal Forms, Logical Consequence, Resolution]]
- [[Propositional Logic]]
- [[Knowledge Base Systems]]
- [[CSCE 420]]
