---
title: "Probabilistic Inference"
type: concept
tags: [csce420, inference, explaining-away, diagnostic, causal, intercausal]
sources: [csce420-lecture-05-probabilistic-reasoning]
course: CSCE 420
updated: 2026-09-01
---

The kinds of query a [[Bayesian Networks|belief network]] can answer, classified by the direction information flows relative to the causal structure.

## Four Types

| Type | Form | Direction |
|---|---|---|
| **Diagnostic** | $P(Cause \mid Effect)$ | Effect → cause |
| **Causal** | $P(Effect \mid Cause)$ | Cause → effect |
| **Intercausal** | Causes of a common effect | Between sibling causes |
| **Mixed** | $P(A \mid CauseOfA \land EffectOfA)$ | Both at once |

That a single network answers all four — rather than needing a separate model per query direction — is the payoff of representing the joint distribution rather than a fixed set of rules.

## Explaining Away

The most interesting case, and the one with no counterpart in logical inference:

$$P(Cause|Effect) \gg P(Cause|Effect \land OtherCause)$$

Learning that **another** cause is present *reduces* belief in the first. The alarm went off, so a burglary is likely — but on learning there was an earthquake, the burglary hypothesis loses most of its support. The earthquake **explains away** the alarm.

Note what this implies structurally: `Burglary` and `Earthquake` are **independent** a priori, but become **dependent once `Alarm` is observed**. Conditioning on a common effect *creates* a dependency between its causes. This is why [[Conditional Independence]] must be stated relative to what is known, and why it cannot simply be read off which nodes are connected.

## Answering Queries

Given evidence $E$, find $P(X|E)$ for query $X$:

- Recursively determine the **causal support** $E^+_X$ for $X$ — evidence from above (its ancestors)
- Recursively determine the **evidential support** $E^-_X$ for $X$ — evidence from below (its descendants)

> **This applies only when the graph is singly connected.** Multiply-connected networks require heavier machinery, which the deck does not develop.

## Using the Results

Beyond answering a single query, a belief network supports:

- **Making decisions** from the derived probabilities plus a utility function — see [[Decision Theory]]
- **Deciding which additional variables** to include in the model
- **Sensitivity analysis** — finding which node matters most and therefore should be estimated most accurately
- **Explaining** the results of reasoning

The last is worth noting against [[Resolution]]'s acknowledged weakness that its proofs are hard for humans to follow. A causal belief network is comparatively legible.

## See Also

- [[Bayesian Networks]]
- [[Belief Network Construction]]
- [[Conditional Independence]]
- [[Decision Theory]]
- [[CSCE 420]]
