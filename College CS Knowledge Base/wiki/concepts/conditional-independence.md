---
title: "Conditional Independence"
type: concept
tags: [csce420, conditional-independence, bayesian-updating, normalization]
sources: [csce420-lecture-05-probabilistic-reasoning]
course: CSCE 420
updated: 2026-09-01
---

$X$ and $Y$ are **conditionally independent given $Z$** iff

$$P(X|Y,Z) = P(X|Z)$$

— once $Z$ is known, $Y$ tells you nothing more about $X$. This is the assumption that makes probabilistic reasoning tractable, and the structural content of a [[Bayesian Networks|belief network]].

## The Problem It Solves

Suppose we know $P(Cavity|Toothache)$ and $P(Cavity|Catch)$. What is $P(Cavity | Toothache \land Catch)$?

Two unattractive options:

- **Look up the joint probability table** — not practical, often impossible ($2^n$ entries)
- **Compute directly**: $P(Cav|Ache \land Catch) = \frac{P(Ache \land Catch|Cav)P(Cav)}{P(Ache \land Catch)}$ — but the new conditional and the normalization factor are painful

## Bayesian Updating

The alternative: **work the evidence in gradually**, reformulating so that conditionals on *combined* evidence are never needed, and using domain knowledge to replace complex conditionals with simpler known ones.

Using the extended Bayes rule:

$$P(Cav|Ache \land Catch) = \underbrace{P(Cav)\frac{P(Ache|Cav)}{P(Ache)}}_{\text{old}} \cdot \underbrace{\frac{P(Catch|Ache \land Cav)}{P(Catch|Ache)}}_{\text{new}}$$

$P(Catch|Ache \land Cav)$ is still awkward — so assume **conditional independence of Ache and Catch given Cav**:

$$P(Catch|Cav \land Ache) = P(Catch|Cav), \qquad P(Ache|Cav \land Catch) = P(Ache|Cav)$$

The remaining $P(Ache)P(Catch|Ache) = P(Catch \land Ache)$ does not depend on the query variable, so it is absorbed into a **normalization constant**:

$$P(Cav|Ache \land Catch) = \alpha\, \underbrace{P(Cav)P(Ache|Cav)}_{\text{old}} \underbrace{P(Catch|Cav)}_{\text{new}}$$

## The General Form

$$P(Z|X,Y) = \alpha\, P(Z)P(X|Z)P(Y|Z)$$

where $\alpha$ makes the distribution sum to 1.

**Each new piece of evidence contributes one independent factor.** Adding evidence becomes multiplication rather than a fresh joint-table lookup — which is why Bayesian updating makes combining multiple evidence efficient.

## Why the Assumption Is Reasonable Here

A toothache and a dental probe catching are both *caused by* the cavity. They are correlated in the population, but once you know whether the cavity is present, learning about one tells you nothing new about the other. This causal pattern — **common cause screens off its effects** — is exactly what a belief network encodes structurally.

## See Also

- [[Bayes Rule]]
- [[Bayesian Networks]]
- [[Belief Network Construction]]
- [[Probability Basics]]
- [[CSCE 420]]
