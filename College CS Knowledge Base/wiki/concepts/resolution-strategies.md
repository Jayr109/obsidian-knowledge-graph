---
title: "Resolution Strategies"
type: concept
tags: [csce420, level-saturation, deletion-strategy, subsumption, set-of-support]
sources: [csce420-lecture-03-logic]
course: CSCE 420
updated: 2026-09-01
---

Naive [[Resolution]] generates enormous numbers of irrelevant clauses. These strategies control the explosion — and matter because resolution's completeness guarantee says only that a proof will be found *eventually*.

## Level Saturation (Two-Pointer Method)

Generate all possible resolvents in levels:

$$S_0 = S \text{ (original clauses)}, \qquad S_n = \{\text{all resolvents of } C_1 \in (S_0 \cup \dots \cup S_{n-1}),\; C_2 \in S_{n-1}\}$$

This is **breadth-first search** over proofs, and is **extremely inefficient except for small problems**. The stated diagnosis: *in generating an $n$-step proof, we also generate all possible derivations of $n-1$ steps.*

## Deletion Strategy

Delete clauses wherever possible. Three kinds are safe to discard:

1. **Tautologies** — e.g. $P(a) \lor \neg P(a) \lor Q(x)$, true regardless, so useless
2. **Duplicates** of an existing clause
3. **Subsumed clauses**

### Subsumption

Clause $C$ **subsumes** clause $D$ iff there is a substitution $\sigma$ with $C\sigma \subseteq D$ (treating clauses as sets of literals). $D$ is the *subsumed clause* and may be deleted.

**Example.** $C = P(x)$, $D = P(a) \lor Q(a)$. With $\sigma = \{x/a\}$: $C\sigma = \{P(a)\} \subseteq \{P(a), Q(a)\} = D$. So $C$ subsumes $D$, and $D$ goes.

The intuition: $C$ is *more general and shorter*, so anything $D$ could contribute, $C$ contributes more broadly. Deletion is complete when paired with certain resolution algorithms such as level saturation.

## Speed-Up Strategies

| Strategy | Rule |
|---|---|
| **Unit preference** | Resolve with clauses having the fewest literals |
| **Set of support** | Begin with set $T$ = clauses from the **negated conclusion**; every step must involve a member of $T$, and results join $T$ |
| **Linear resolution** | Each step must involve the clause produced by the previous step (depth-first) |

**Unit preference** works because resolving with a short clause yields a short resolvent, and the target — the empty clause **False** — is the shortest of all.

**Set of support** encodes the observation that a proof must actually *use* the negated goal. Restricting to clauses descending from it eliminates derivations that reason about the axioms pointlessly — a direct answer to level saturation's irrelevance problem.

## See Also

- [[Resolution]]
- [[Resolvents and Factors]]
- [[Answer Extraction]]
- [[CSCE 420]]
