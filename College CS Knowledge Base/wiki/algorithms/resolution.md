---
title: "Resolution"
type: algorithm
tags: [csce420, logic, refutation, cnf, theorem-proving]
sources: [csce420-midterm-practice, csce420-final-practice, csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

Resolution is a single inference rule that is **refutation-complete**: if a set of clauses is unsatisfiable, repeated resolution will derive the empty clause (False). To prove $KB \models \alpha$, you negate the conclusion, add it to the KB, convert everything to clauses, and derive False.

## The Rule

From two clauses containing complementary literals, infer their combination with those literals removed:

$$\frac{C \lor \ell \qquad D \lor \neg \ell}{C \lor D}$$

In [[First-Order Logic]], the literals need not be syntactically identical — they need only [[Unification|unify]], and the resulting substitution is applied to the resolvent.

## Procedure

1. Convert every KB sentence to clause form ([[First-Order Logic]] lists the seven steps).
2. **Negate the conclusion** and convert it to clauses too.
3. Repeatedly resolve pairs, adding each resolvent to the set.
4. Stop when the empty clause (False) appears.

Two failure modes dominate on exams: forgetting to negate the conclusion, and leaving an $\land$ inside a "clause" instead of splitting it into two.

## Worked Example 1 — Propositional (Midterm Practice, Problem 10)

Given (1) $Q \to \neg R$, (2) $S \lor \neg((R \lor W) \to P)$, (3) $W \to P$, show $\neg Q \lor S$ is a logical consequence.

**Clausify.** Sentence (2) is the one the "no $\land$ in a clause" caution is aimed at:

$$(R \lor W) \to P \;\equiv\; \neg(R \lor W) \lor P$$
$$\neg\big((R \lor W) \to P\big) \;\equiv\; (R \lor W) \land \neg P$$
$$S \lor \big((R \lor W) \land \neg P\big) \;\equiv\; (S \lor R \lor W) \land (S \lor \neg P)$$

so (2) yields **two** clauses. The negated conclusion $\neg(\neg Q \lor S) \equiv Q \land \neg S$ yields two more.

| # | Clause | Origin |
|---|--------|--------|
| 1 | $\neg Q \lor \neg R$ | given (1) |
| 2 | $S \lor R \lor W$ | given (2), first conjunct |
| 3 | $S \lor \neg P$ | given (2), second conjunct |
| 4 | $\neg W \lor P$ | given (3) |
| 5 | $Q$ | negated conclusion |
| 6 | $\neg S$ | negated conclusion |

**Derivation.**

| # | Resolvent | From | On literal |
|---|---|---|---|
| 7 | $\neg R$ | 1, 5 | $Q$ |
| 8 | $R \lor W$ | 2, 6 | $S$ |
| 9 | $W$ | 7, 8 | $R$ |
| 10 | $P$ | 4, 9 | $W$ |
| 11 | $\neg P$ | 3, 6 | $S$ |
| 12 | **False** | 10, 11 | $P$ |

## Worked Example 2 — First-Order (Final Practice, Problem 1)

Given
1. $\forall x\, (P(x) \to Q(x))$
2. $\forall y\, ((Q(y) \land R(y)) \to S(y))$
3. $\exists z\, (P(z) \land \neg S(z))$

show $\exists w\, \neg R(w)$ is a logical consequence.

**Clausify.** Sentence 3 is existential and outermost, so skolemize $z$ to a fresh **constant** $C$, then split on the $\land$. The conclusion is existential, so its negation $\neg\exists w\, \neg R(w) \equiv \forall w\, R(w)$ is universal — giving a clause with a free (universally quantified) variable.

| # | Clause | Origin |
|---|--------|--------|
| 1 | $\neg P(x) \lor Q(x)$ | given 1 |
| 2 | $\neg Q(y) \lor \neg R(y) \lor S(y)$ | given 2 |
| 3 | $P(C)$ | given 3, skolemized |
| 4 | $\neg S(C)$ | given 3, skolemized |
| 5 | $R(w)$ | negated conclusion |

**Derivation.**

| # | Resolvent | From | Substitution |
|---|---|---|---|
| 6 | $Q(C)$ | 1, 3 | $\{x/C\}$ |
| 7 | $\neg R(C) \lor S(C)$ | 2, 6 | $\{y/C\}$ |
| 8 | $\neg R(C)$ | 7, 4 | — |
| 9 | **False** | 8, 5 | $\{w/C\}$ |

Both skolemizations matter. Clause 3 must be a *constant* $C$, not a variable — otherwise steps 6–8 would prove the property for all objects rather than for the one witness that exists. And the negated conclusion must be a *variable* $w$, so that step 9 can instantiate it to $C$.

> Both examples worked here; the practice exams ship without answer keys.

## From the Lecture

### Why Resolution Works

Resolution proves $G$ follows from $F_1 \land \dots \land F_n$ by showing $F_1 \land \dots \land F_n \land \neg G$ is **inconsistent** — see [[Logical Consequence]] for the theorem licensing this.

The justification for *adding* derived clauses to the list: if $H$ is a logical consequence of $F_1 \land \dots \land F_n$, then

$$F_1 \land \dots \land F_n \;=\; F_1 \land \dots \land F_n \land H$$

because when the premises are **True**, $H$ must also be true; and when they are **False**, both sides are false so $H$ does not matter. Hence any logical consequence can be added without changing the value — which is exactly what each resolution step does.

### What Resolution Is *Not*

A distinction the lecture flags explicitly. If $C_1 \land C_2 \rightarrow H$, then

- $C_1 \land C_2 \land H = C_1 \land C_2$ &nbsp;&nbsp;✔
- $C_1 \land C_2 = H$ &nbsp;&nbsp;✘

Formally: $(C_1 \land C_2 \rightarrow H) \rightarrow ((C_1 \land C_2 \land H) \leftrightarrow (C_1 \land C_2))$, but $(C_1 \land C_2 \rightarrow H) \nrightarrow ((C_1 \land C_2) \leftrightarrow H)$. The resolvent is *implied by* the parents, not *equivalent to* them — it is weaker, having dropped the complementary literals.

### The Algorithm

1. Convert premises to [[Normal Forms|CNF]]; list the resulting clauses.
2. **Negate the conclusion**, convert to CNF, add to the list.
3. **Resolution step**: pick two clauses with *exactly one* complementary literal — any other literals appearing in both must have the **same sign**. Form the disjunction without the complementary pair; add it.
   $$(P \lor C_i),\; (\neg P \lor C_j) \;\Longrightarrow\; (C_i \lor C_j)$$
4. If **False** was added, stop — theorem proved. Otherwise go to 3.

### Tip: Negating a Disjunctive Conclusion

If the conclusion is $P \lor R$, negating gives $\neg P \land \neg R$ — which is **two clauses, not one**. Both must be added as separate lines. A common source of failed proofs.

### Worked Example

Premises $A$; $B$; $D$; $\neg A \lor \neg B \lor C$; $\neg C \lor \neg D \lor E$. Prove $E$ by adding $\neg E$:

```
(1,4)  ¬B ∨ C        (7)
(2,7)  C             (8)
(5,6)  ¬C ∨ ¬D       (9)
(8,9)  ¬D            (10)
(3,10) False         (11)
```

### First-Order Properties

- **Complete**: if a set of clauses $S$ is unsatisfiable, resolution will *eventually* derive False — everything true can be proved.
- **Sound**: if False is derived, $S$ really is unsatisfiable — everything proved is true.

"Eventually" is doing real work; see [[Resolution Strategies]] for the control needed in practice.

### Weakness

Resolution derives *Axioms $\land\ \neg$Theorem = False*. So: **is there already a False in the axioms?** If so the formula is unsatisfiable regardless and anything is provable. Can we tell whether the axioms alone derive False? Generally, no.

### Advantages and Disadvantages

**Advantages**: universally applicable to anything expressible in first-order logic; the proving engine is decoupled from any particular domain.

**Disadvantages**: (1) too inefficient to be generally applicable; (2) **purely syntactic** — it does not consider what the predicates *mean*, so domain-dependent heuristics are impossible; (3) a contradiction in the axioms allows anything to be proved; (4) resolution proofs are difficult for humans to follow.

Point (2) is the deep one, and it is the same domain-independence that [[Logical Inference]] identifies as both the strength and the limitation of the approach.

For first-order resolution mechanics see [[Resolvents and Factors]]; for the question-answering application see [[Answer Extraction]].

## See Also

- [[Unification]]
- [[First-Order Logic]]
- [[Logical Inference]]
- [[Symbolic AI]]
