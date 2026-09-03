---
title: "Normal Forms"
type: concept
tags: [csce420, cnf, dnf, clauses, literals, normal-forms]
sources: [csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

Normal forms are canonical shapes for logical formulas. **Conjunctive Normal Form (CNF)** is the one that matters, because [[Resolution]] requires its input as a list of clauses.

## The Building Blocks

| Term | Definition |
|---|---|
| **Literal** | an atom, or a negated atom |
| **Clause** | a **disjunction** of one or more literals |
| **Term** | a **conjunction** of one or more literals |

## The Two Forms

- **CNF** — a *conjunction of clauses*: $C_1 \land C_2 \land C_3 \dots$
  e.g. $(\neg F \lor G \lor H) \land (\neg G) \land (K \lor L)$
- **DNF** — a *disjunction of terms*: $T_1 \lor T_2 \lor T_3 \dots$
  e.g. $(\neg F \land G \land H) \lor (\neg G) \lor (K \land L)$

> **Exercise from the slides**: $P \lor Q$ is in *both* CNF and DNF. Why? Because it is simultaneously a conjunction of one clause and a disjunction of two single-literal terms — with one connective, the two definitions coincide.

## Conversion Procedure

Any formula can be transformed into a normal form by applying, in order:

1. **Eliminate $\rightarrow$ and $\leftrightarrow$** using
   $F \leftrightarrow G = (F \rightarrow G) \land (G \rightarrow F)$ and $F \rightarrow G = \neg F \lor G$
2. **Push negations inward** to sit immediately before atoms, using double negation and **De Morgan's laws**
3. **Distribute** using $F \lor (G \land H) = (F \lor G) \land (F \lor H)$ and its dual, plus other laws as needed

### Worked Example

Convert $(P \lor \neg Q) \rightarrow R$ to DNF:

$$(P \lor \neg Q) \rightarrow R = \neg(P \lor \neg Q) \lor R = (\neg P \land \neg(\neg Q)) \lor R = (\neg P \land Q) \lor R$$

(remove $\rightarrow$; De Morgan; remove double negation)

## Distribution Runs Both Ways

A point the lecture makes with a deliberately awkward example — convert $(P \land Q) \lor (P \land R)$ to CNF:

- **Forward distribution**: $((P \land Q) \lor P) \land ((P \land Q) \lor R) \;\dots\; (P \lor P) \land (P \lor Q) \land (P \lor R) \land (Q \lor R)$
- **Backward distribution**: $P \land (Q \lor R)$

Both are valid CNF; the second is dramatically simpler. Mechanically applying the rules forward produces correct but bloated output — worth knowing when clause count drives [[Resolution]] cost.

## See Also

- [[Propositional Logic]]
- [[Horn Clauses]]
- [[Resolution]]
- [[Prenex Normal Form]]
- [[CSCE 420]]
