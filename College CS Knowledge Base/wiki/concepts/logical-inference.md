---
title: "Logical Inference"
type: concept
tags: [csce420, logic, inference-engine, knowledge-base, soundness, completeness]
sources: [csce420-midterm-practice, csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

A knowledge-based agent separates **what it knows** (the knowledge base, a set of logical sentences) from **how it reasons** (the inference engine, a set of domain-independent inference rules). The inference engine derives new sentences from the KB without knowing what the symbols mean. This separation is the defining architectural commitment of [[Symbolic AI]], and it cuts both ways.

## Core Definitions

- **Entailment** ($KB \models \alpha$) — $\alpha$ is true in every model where $KB$ is true.
- **Sound** — the engine derives only entailed sentences. It never lies.
- **Complete** — the engine can derive every entailed sentence. It never misses.
- **Logical consequence** — the exam phrasing for entailment. To show $KB \models \alpha$ by [[Resolution]], prove $KB \land \neg\alpha$ is unsatisfiable.

## Domain Independence: Good and Bad (Midterm Practice, Problem 7)

The problem asks why domain independence of the inference engine is *both* good and bad, in terms of (1) efficiency of search — noting that generating clauses from the KB is a search process — and (2) applicability across domains.

**(1) Efficiency — Bad.** The engine treats every clause as an equally plausible next step because it has no idea what any symbol means. Every resolvable pair is a legal move, so the branching factor of the clause-generation search is enormous and grows as derived clauses are added back to the KB. A domain expert would know that resolving on some particular literal is pointless; the engine cannot know that, so it explores those branches anyway. This is why general resolution theorem provers are slow, and why the 1970s–80s built domain-specific expert systems instead of general reasoners.

**(2) Applicability — Good.** The same engine works on medical diagnosis, circuit verification, and map coloring with no code changes. Only the KB changes. Knowledge is declarative and reusable, new facts can be added without touching the reasoning machinery, and correctness of the engine is proved once for all domains.

The trade-off is the general one between generality and performance: a mechanism that assumes nothing about its input can be applied anywhere and exploits nothing anywhere.

> Worked here from the problem statement; the practice exam ships without an answer key.

## From the Lecture

### The Architecture

A knowledge-based system separates **domain-independent algorithms** (the inference engine) from **domain-specific content** (the knowledge base). See [[Knowledge Base Systems]] for the full treatment, including the ontological/epistemological table comparing propositional, first-order, temporal, probabilistic, and fuzzy logics.

### Soundness and Completeness

| Property | Definition | Slogan |
|---|---|---|
| **Sound** | No false sentences can be derived from the KB | Everything proved is true |
| **Complete** | All true conclusions can be derived from the premises | Everything true can be proved |

[[Resolution]] is proved to be **both** for first-order logic — though its completeness is only "eventually", which is why [[Resolution Strategies]] matter in practice.

### Three Routes to a Conclusion

The deck presents [[Forward and Backward Chaining|forward chaining, backward chaining]], and [[Resolution]] as the three ways to prove a theorem from facts and rules. Forward chaining is data-driven, backward is goal-driven, and resolution is refutation-based — the only one of the three that mechanizes cleanly for full first-order logic.

## See Also

- [[Resolution]]
- [[Unification]]
- [[First-Order Logic]]
- [[Symbolic AI]]
