---
title: "Bayes Rule"
type: concept
tags: [csce420, bayes-rule, diagnostic, causal, base-rate, priors]
sources: [csce420-lecture-05-probabilistic-reasoning]
course: CSCE 420
updated: 2026-09-01
---

Bayes' rule inverts a conditional probability, letting an agent compute the hard direction from the easy one.

## Derivation

From $P(A|B) = \frac{P(A \land B)}{P(B)}$ and $P(B|A) = \frac{P(A \land B)}{P(A)}$ we get $P(A|B)P(B) = P(B|A)P(A)$, hence

$$P(B|A) = \frac{P(A|B)P(B)}{P(A)}$$

## Extended Form (Conditioned on Background Evidence)

$$P(Y|X,E) = \frac{P(X|Y,E)\,P(Y|E)}{P(X|E)}$$

Every term simply gains "$, E$" — the rule holds inside any fixed context.

## Computing the Denominator

Usually $P(A)$ is not given, and is recovered by **conditioning**:

$$P(T) = P(T \land D) + P(T \land \neg D) = P(T|D)P(D) + P(T|\neg D)P(\neg D)$$

Generally, for disjoint exhaustive $X = x_1 \dots x_n$: $P(T) = \sum_x P(T|X=x)P(X=x)$.

> A subtlety the deck flags: $\{D\} \cup \{\neg D\}$ covers the whole population, but $\{T\} \cup \{\neg T\}$ does **not** — because you did not test everyone.

## The Disease Example

You test positive for a serious disease. The test is 99% accurate. The disease strikes 1 in 10,000. **What are the chances you have it?**

Given: $P(T|D) = 0.99$, $P(\neg T|\neg D) = 0.99$, $P(D) = 0.0001$. Derived: $P(T|\neg D) = 0.01$, $P(\neg D) = 0.9999$.

$$P(T) = 0.99 \times 0.0001 + 0.01 \times 0.9999 = 0.010098$$

$$P(D|T) = \frac{0.99 \times 0.0001}{0.010098} = 0.0098 \approx \mathbf{1\%}$$

**Slightly less than 1%** — despite a 99% accurate test. This is the base-rate effect: the disease is so rare that the 1% false-positive rate applied to the 9,999 healthy people produces far more positives than the disease does.

Concretely: test 10,000 people and you get about **100 false positives and one true positive.** That ratio *is* the answer.

> Exercise from the slides: how accurate must the test be for $P(D|T) > 0.95$?

The same calculation appears in [[CSCE 465]] with an intrusion in place of the disease and an alarm in place of the positive test; see [[Base-Rate Fallacy]].

## Why Bayes' Rule Is Worth the Trouble

- $P(T|D)$ is **easy to obtain** — run the test on a small pool of known patients.
- $P(D|T)$ is **hard to obtain directly** — you would need to test ~10,000 people to collect 100 positives.
- $P(D)$ serves as the **prior**. Where it is not directly measurable, the prior represents the *subjective belief* of whoever is calculating.

## Diagnostic vs. Causal Knowledge

| Direction | Form | Stability |
|---|---|---|
| **Causal** | $P(Symptom \mid Disease)$ | Relatively **fixed** |
| Prior | $P(Disease)$ | Somewhat variable |
| **Diagnostic** | $P(Disease \mid Symptom)$ | **Fluctuates** as $P(Disease)$ changes |

This is the practical argument for the rule. A directly-measured $P(Disease|Symptom)$ **goes stale** when prevalence changes — during an epidemic, say — whereas the causal term stays put, so recomputing through Bayes' rule is **far more robust**.

## Comparing Two Hypotheses Without the Denominator

When either $C_1$ or $C_2$ could cause effect $E$, the shared $P(E)$ cancels:

$$\frac{P(C_1|E)}{P(C_2|E)} = \frac{P(E|C_1)P(C_1)}{P(E|C_2)P(C_2)}$$

**No need to compute $P(E)$ at all** — usually the most awkward term.

### Object Recognition

Given an image on the retina, is the cause a 2D hexagon or a transparent 3D cube?

$$\frac{P(Hexagon|Image)}{P(Cube|Image)} = \frac{P(Image|Hexagon)P(Hexagon)}{P(Image|Cube)P(Cube)} = \frac{a}{b}$$

If $a/b > 1$ a hexagon most likely generated the image; if $< 1$, a cube.

**Why is $P(Image|Object)$ easier than $P(Object|Image)$?** Because the forward direction is **one-to-one — that is computer graphics**; the backward direction is **one-to-many — that is computer vision**. Rendering a known object is deterministic; inverting a rendering is ambiguous. Bayes' rule lets vision be done by running graphics forward and comparing.

## See Also

- [[Probability Basics]]
- [[Conditional Independence]]
- [[Bayesian Networks]]
- [[Uncertainty]]
- [[Base-Rate Fallacy]]
- [[CSCE 420]]
