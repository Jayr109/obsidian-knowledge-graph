---
title: "Wumpus World"
type: concept
tags: [csce420, wumpus-world, entailment, knowledge-base, agents]
sources: [csce420-lecture-04-planning]
course: CSCE 420
updated: 2026-09-01
---

Wumpus World is the example domain used to make [[Logical Inference|logical inference]] concrete: a grid world where an agent must reach gold while avoiding pits and a monster, reasoning from *indirect* sensory evidence.

## The Domain

- **Goal**: get to the gold and grab it
- **Hazards**: pits, and the wumpus
- **Clues**: a **breeze** near pits, a **stench** near the wumpus
- **Other sensors**: bump (wall), glitter (gold), scream (kill)
- **Actions**: move, grab, shoot

### Performance Measure

| Event | Score |
|---|---|
| Picking up gold | +1000 |
| Falling in a pit, or being eaten | −1000 |
| Each action taken | −1 |
| Each arrow used | −10 |

The scoring matters: the −1 per action means a *correct but slow* plan still loses points, so the agent must reason efficiently, not merely soundly.

## The Inference Walkthrough

The deck traces knowledge accumulating square by square, and it is a clean illustration of **entailment doing real work**:

1. From [1,1] move to [2,1]. A breeze is felt, so [2,2] and [3,1] are marked as possible pits (P?). **[1,1] need not be marked** — the agent came from there and already knows it is safe.
2. Move back to [1,1] and then to [1,2]. A **stench** is perceived, so the wumpus could be in [1,1], [2,2], or [1,3].
   - [1,1] is ruled out — the agent has been there.
   - [2,2] is ruled out — the agent was at [2,1] and detected **no stench**.
   - **Therefore the wumpus is in [1,3].**
3. Also, **no breeze at [1,2]**, so [2,2] is safe after all — it was previously P?.
4. Move to [2,2], then [2,3], where glitter reveals the gold.

Step 2 is the point of the example: the conclusion follows from the **absence** of a percept, which is exactly the kind of inference a knowledge base gives you and a reactive agent cannot make.

## Entailment, Precisely

With the KB holding the basic rules plus [1,1] and [2,1] explored, pits could lie in three unvisited squares — $2^3 = 8$ possible cases. Consider:

- $\alpha_1$ = "There is no pit in [1,2]"
- $\alpha_2$ = "There is no pit in [2,2]"

**Only $\alpha_1$ follows from the KB**: every model of the KB satisfies $\alpha_1$, so $KB \models \alpha_1$. But $KB \not\models \alpha_2$ — some models of the KB have a pit in [2,2].

This is the definition of entailment made operational: enumerate the models consistent with what is known, and check whether the query holds in *all* of them.

## See Also

- [[Planning]]
- [[Situation Calculus]]
- [[Logical Inference]]
- [[Propositional Logic]]
- [[CSCE 420]]
