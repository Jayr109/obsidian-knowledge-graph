---
title: "Prolog"
type: concept
tags: [csce420, prolog, logic-programming, horn-clauses, backward-chaining]
sources: [csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

**Prolog** is a logic programming language based on a subset of first-order logic — specifically [[Horn Clauses|Horn clauses]], resolved by backward chaining. It is the practical demonstration that the machinery in this unit is a working programming model, not only a proof technique.

## Why the Horn Restriction

Prolog restricts to Horn clauses — at most one positive literal — because that fragment makes inference tractable and gives backward chaining an unambiguous target. See [[Horn Clauses]] and [[Forward and Backward Chaining]].

The cost is expressiveness: genuinely disjunctive conclusions such as $P \lor Q$ have no Horn form, so Prolog cannot state them directly. This is the same tractability-for-expressiveness trade the lecture identifies when introducing the form.

## The Correspondence

| Logic concept | Prolog counterpart |
|---|---|
| [[Horn Clauses\|Horn clause]] $(G \land H) \rightarrow F$ | A rule: `f :- g, h.` |
| Ground literal | A fact |
| Negated goal | A query |
| [[Forward and Backward Chaining\|Backward chaining]] | The execution model |
| [[Unification]] | Parameter passing and pattern matching |
| [[Answer Extraction]] | Returned variable bindings |

The last row is the important one: a Prolog query does not merely succeed or fail, it **returns the bindings** — which is answer extraction built into the language.

## Declarative Programming

Prolog realizes the [[Knowledge Base Systems|declarative]] ideal — state *what* is true and let the engine determine *how* to derive it. The programmer supplies facts and rules; the resolution engine supplies control flow.

> The lecture presents Prolog across five slides plus a live resolution-prover demo. The slides are screenshots of code and interpreter sessions, so their content is not recoverable from the PDF text layer.

## See Also

- [[Horn Clauses]]
- [[Forward and Backward Chaining]]
- [[Resolution]]
- [[Answer Extraction]]
- [[Knowledge Base Systems]]
- [[CSCE 420]]
