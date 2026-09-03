---
title: "Frame Problem"
type: concept
tags: [csce420, frame-problem, successor-state-axioms, fluents, situation-calculus]
sources: [csce420-lecture-04-planning]
course: CSCE 420
updated: 2026-09-01
---

The **frame problem** is the difficulty of representing what does **not** change when an action is taken. Effect axioms say only what an action *changes*; without further machinery, nothing rules out the possibility that everything else changed too.

## The Failure

In [[Situation Calculus]] with only possibility and effect axioms, this cannot be proven:

$$At(G_1, [1,1], Result([Go([1,1],[1,2]),\, Grab(G_1),\, Go([1,2],[1,1])], S_0))$$

The agent picked up the gold and carried it home — but the axioms never said the gold *stays* where it was when the agent moves. **The gold may have moved when the agent moved**, for all the logic knows.

## First Attempt: Frame Axioms

Write axioms stating what stays put:

$$At(o,x,s) \land (o \neq Agent) \land \neg Holding(o,s) \;\rightarrow\; At(o,x,Result(Go(y,z),s))$$

"Moving does not affect the gold when it is not held."

**The problem**: you need $O(AF)$ such axioms — one for every (action, fluent) pair, where $A$ is the number of actions and $F$ the number of fluent predicates. The knowledge base is swamped by statements about things not happening.

## Two Frame Problems

| Problem | What it concerns |
|---|---|
| **Representational** | How many axioms must be *written* — the $O(AF)$ blow-up above |
| **Inferential** | How much work it takes to *project* a $t$-step plan |

For the inferential version, the target is $O(Et)$ where $E$ is the number of effects — typically far smaller than $F$ — rather than $O(Ft)$ or $O(AEt)$.

## Solving the Representational Problem: Successor-State Axioms

Instead of writing one axiom per (action, fluent) pair, describe **how each fluent evolves**:

> Action is possible → (Fluent is true in the result state ↔ (1) the action's effect made it true, **or** (2) it was true before and the action left it alone).

$$Poss(a,s) \rightarrow \big(At(Agent,y,Result(a,s)) \leftrightarrow a = Go(x,y) \lor (At(Agent,y,s) \land a \neq Go(y,z))\big)$$

One axiom per **fluent** rather than per (action, fluent) pair. The biconditional is what does the work: it states the *complete* set of circumstances under which the fluent holds afterward, so "nothing else changed" becomes a consequence rather than something to assert.

### The Ramification Problem

A remaining issue: **implicit effects**. Moving while holding something moves that thing too. This is the *ramification problem*, addressable with a more general successor-state axiom.

## Solving the Inferential Problem

A typical frame axiom has several actions making a fluent true and several making it false:

$$Poss(a,s) \rightarrow [F_i(Result(a,s)) \leftrightarrow \{(a = A_1 \lor a = A_2 \dots) \lor (F_i(s) \land a \neq A_3 \land a \neq A_4 \dots)\}]$$

Formalize the two groups as predicates:

$$Poss(a,s) \rightarrow [F_i(Result(a,s)) \leftrightarrow \{PosEffect(a,F_i) \lor (F_i(s) \land \neg NegEffect(a,F_i))\}]$$

with facts $PosEffect(A_1,F_i)$, $NegEffect(A_3,F_i)$, and so on. Now projection is efficient: **take the current action, fetch its effects, update only those fluents** — $O(Et)$.

The alternative offered: use **fluent calculus** rather than situation calculus.

## See Also

- [[Situation Calculus]]
- [[Planning]]
- [[Wumpus World]]
- [[First-Order Logic]]
- [[CSCE 420]]
