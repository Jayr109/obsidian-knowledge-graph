---
title: "CSCE 420 Lecture 3 — Logic and Automated Theorem Proving"
type: source
tags: [lecture, csce420, logic, propositional, first-order, resolution, theorem-proving]
sources: []
course: CSCE 420
updated: 2026-09-01
---

Slide deck 3 of [[CSCE 420]], by [[Yoonsuck Choe]]. 145 slides — the second-largest deck. Covers knowledge representation, propositional logic, first-order logic, and automated theorem proving by resolution. The predicate-calculus treatment follows Chang & Lee, *Symbolic Logic and Mechanical Theorem Proving* (1973); substitution notation follows Russell & Norvig.

## Structure

| Slides | Section |
|---|---|
| 1–10 | Knowledge representation; KB systems; types of logic |
| 11–18 | Propositional logic: wffs, semantics, laws, inference rules |
| 19–27 | Normal forms: CNF, DNF, Horn clauses, conversion |
| 28–32 | Logical consequence; the refutation theorem |
| 33–44 | Theorem proving: forward/backward chaining, resolution algorithm |
| 45–49 | Worked example (the unicorn); limits of propositional logic |
| 50–66 | First-order logic: terms, predicates, quantifiers |
| 67–76 | Domain, interpretation, semantics, bound/free variables |
| 77–89 | Standard form: prenex, CNF matrix, skolemization |
| 90–93 | Proof example |
| 94–109 | Substitution and unification |
| 110–127 | Factors, resolvents, properties of resolution |
| 128–132 | Implementation: level saturation, deletion, speed-ups |
| 133–139 | Pros and cons; question answering; answer extraction |
| 140–145 | Prolog tutorial and prover demo |

## The Organizing Idea

The deck is one continuous argument for **why resolution is the right mechanism**, built on a chain of reductions:

1. **Validity reduces to inconsistency** — $G$ is valid iff $\neg G$ is inconsistent ([[Propositional Logic]]).
2. **Entailment reduces to refutation** — $G$ follows from $F_1 \dots F_n$ iff $F_1 \land \dots \land F_n \land \neg G$ is inconsistent ([[Logical Consequence]]). This is proved on the slides, not asserted.
3. **Any formula reduces to CNF** ([[Normal Forms]]), and any first-order formula to universally-quantified CNF via [[Prenex Normal Form]] and [[Skolemization]].
4. **All inference reduces to one rule** — resolution subsumes modus ponens and unit resolution ([[Inference Rules]]).

So a general theorem prover needs one normal form and one rule. Everything after slide 94 is making that work for first-order terms: [[Substitution]], [[Unification]], and [[Resolvents and Factors]].

## Why Propositional Logic Is Not Enough

The pivot of the deck, stated as a challenge on slide 49:

- $P$: All men are mortal &nbsp;&nbsp; $Q$: Socrates is a man &nbsp;&nbsp; $R$: Socrates is mortal
- **Can you prove $(P \land Q) \rightarrow R$?**

No — the atoms are unrelated, and nothing inside $P$ connects "men" to "Socrates". Propositional logic cannot reason with general rules. This single failure motivates the entire second half.

## Results Worth Extracting

- **The refutation theorem** and its proof — the licence for proof by contradiction.
- **Anything follows from False**, so premises must be **consistent** for a theorem to mean anything. This returns as a stated weakness of resolution: a contradiction hidden in the axioms lets the prover prove everything, and detecting it is generally impossible.
- **Quantifier pairing**: $\forall$ goes with $\rightarrow$, $\exists$ goes with $\land$. The two wrong forms are given explicitly with what they actually mean.
- **$\forall x \exists y \neq \exists y \forall x$**, made mechanical by [[Skolemization]]: a Skolem *constant* versus a Skolem *function*.
- **Undecidability**: infinite domains mean infinitely many interpretations, so validity, satisfiability and consistency are **not decidable in general** for predicate calculus. Truth tables do not generalize.
- **Resolution is sound and complete** for first-order logic — but complete only "eventually", which is what [[Resolution Strategies]] address.
- **Negating a disjunctive conclusion yields multiple clauses** — negating $P \lor R$ gives two lines, not one.

## Worked Examples in the Deck

- **The unicorn** (slides 46–48) — mythical/immortal/mammal/horned/magical, proved two ways: by resolution, and by direct algebraic manipulation ending in modus ponens. Source: the AIMA exercise collection.
- **Howling hounds** (slides 63–64) — a five-sentence English-to-FOL translation exercise.
- **Kinship domain** (slide 69) — mother, husband, parent, grandparent, sibling axioms.
- **Bob/Carol/Ted/Alice** (slides 73–74) — evaluating $\forall x (Man(x) \rightarrow \exists y (Woman(y) \land Loves(x,y)))$ case by case over a four-element domain.
- **Used-car dealers** (slides 84–85, 91) — the proof that motivates skolemization, done informally first ("there must be an $x$, which we shall arbitrarily call $a$") and then mechanically.
- **Greek genealogy** (slides 136–138) — "Who is a grandparent of Harmonia?", the [[Answer Extraction]] example.

## Visual-Only Slides

Slide 82 is a figure of quantifier-equivalence Venn diagrams whose content is not in the text layer (it extracts as a long run of box-drawing artifacts). Slides 141–145, the [[Prolog]] tutorial and resolution-prover demo, are screenshots of code and interpreter sessions and carry no extractable text beyond their titles.

## Pages Created

**New (15)**: [[Knowledge Representation]], [[Knowledge Base Systems]], [[Propositional Logic]], [[Normal Forms]], [[Horn Clauses]], [[Inference Rules]], [[Logical Consequence]], [[Forward and Backward Chaining]], [[Prenex Normal Form]], [[Skolemization]], [[Substitution]], [[Resolvents and Factors]], [[Resolution Strategies]], [[Answer Extraction]], [[Prolog]]

**Reconciled (4)**: [[Resolution]], [[Unification]], [[First-Order Logic]], [[Logical Inference]]

## See Also

- [[CSCE 420]]
- [[Yoonsuck Choe]]
- [[Resolution]]
- [[First-Order Logic]]
- [[CSCE 420 Midterm Practice]]
