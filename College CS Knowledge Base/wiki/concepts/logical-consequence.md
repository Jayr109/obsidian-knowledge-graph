---
title: "Logical Consequence"
type: concept
tags: [csce420, entailment, theorem, axioms, validity, refutation]
sources: [csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

$G$ is a **logical consequence** of $F_1, \dots, F_n$ iff, for any interpretation in which $F_1 \land \dots \land F_n$ is true, $G$ is also true — equivalently, iff $(F_1 \land \dots \land F_n) \rightarrow G$ is **valid**.

## Vocabulary

- $(F_1 \land \dots \land F_n) \rightarrow G$ is called a **theorem**
- $F_1, \dots, F_n$ are the **axioms** (postulates, premises)
- $G$ is the **conclusion**

## The Refutation Theorem

The result that makes automated theorem proving possible:

> **$G$ is a logical consequence of $F_1, \dots, F_n$ iff $F_1 \land \dots \land F_n \land \neg G$ is inconsistent.**

**Proof.** $G$ is a logical consequence iff $H = (F_1 \land \dots \land F_n) \rightarrow G$ is valid. $H$ is valid iff $\neg H$ is inconsistent. And

$$\neg\big((F_1 \land \dots \land F_n) \rightarrow G\big) = \neg\big(\neg(F_1 \land \dots \land F_n) \lor G\big) = (F_1 \land \dots \land F_n) \land \neg G$$

so $H$ is valid iff $F_1 \land \dots \land F_n \land \neg G$ is inconsistent. $\blacksquare$

This converts "prove $G$ follows" into "derive a contradiction from the premises plus the *negated* goal" — precisely what [[Resolution]] does.

## The Caveat: Anything Follows From False

$$F \rightarrow G = \text{False} \rightarrow G = \neg\text{False} \lor G = \text{True} \lor G = \text{True}$$

**Anything is a logical consequence of False.** So for a theorem's result to be meaningful, **the premises must be consistent.** This is not a technicality — it reappears as a stated weakness of [[Resolution]]: a contradiction hidden in the axiom set lets the prover "prove" everything, and detecting that is generally not possible.

## Three Ways to Prove It

1. **Truth table** — $G$ must be true whenever the premises are
2. **Prove $(F_1 \land \dots \land F_n) \rightarrow G$ is valid** — by truth table, or by algebraically reducing to True
3. **Prove $F_1 \land \dots \land F_n \land \neg G$ is inconsistent** — by truth table, or by algebraically reducing to False

Method 3 is the resolution route. Methods 1 and 2 are **model checking**; they are exponential in the number of atoms ($2^n$ rows) and do not generalize to [[First-Order Logic]], where the domain may be infinite.

## See Also

- [[Propositional Logic]]
- [[Resolution]]
- [[Inference Rules]]
- [[Forward and Backward Chaining]]
- [[CSCE 420]]
