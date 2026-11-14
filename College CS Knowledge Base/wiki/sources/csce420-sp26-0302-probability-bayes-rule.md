---
title: "CSCE 420 Spring 2026 — 03-02 Probability, Bayes Rule"
type: source
tags: [csce420, lecture-recording, spring-2026, decision-theory, expected-utility, probability-axioms, joint-distribution, marginalization, bayes-rule, rare-disease, causal-diagnostic]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-03-02
deck: slide05
exam: final
updated: 2026-09-17
---

Spring 2026 lecture, 48 min. Decision theory and maximum expected utility, probability basics through the joint distribution, Bayes rule derived and extended, and the rare-disease example worked to its counterintuitive answer. Slides 05:8–30. Post-midterm material; midterm was that Friday.

## Decision Theory = Probability + Utility

Blackjack: keep track of the cards seen to calibrate whether the next card is likely high or low. **Utility theory** handles preferences — *"someone might prefer A over B; someone else with a different preference goes for B."* **Decision theory** combines it with probability: an agent is rational iff it chooses the action with the **highest expected utility** — the principle of maximum expected utility. A [[Expectimax|minimax tree with probabilistic levels]] is the game-playing case.

**The worked example**: three actions from one state.
- Action 1: utility 10 at p = 0.2, else 0 → EU = **2**
- Action 2: utility ~1,000 at p = 0.001, else 0 → EU ≈ **1** (the slide had a typo in the payoff; he corrected it live)
- Action 3: a modest payoff at high probability → **highest EU**

*"If you just looked at this without the probability, you'd pick action 2 because of the very high payoff. But that payoff has very low probability."* The lowest payoff with the highest probability won.

The **decision-theoretic agent**: persistent belief state and action; on each percept, update beliefs, compute outcome probabilities per action, select the action maximizing expected utility.

## Probability Basics — Points of Emphasis

- Bold **P(X)** is the whole **distribution**, not one value.
- Conditional probability by the Venn picture: P(A|B) = P(A∧B)/P(B) — the intersection over the B region. The **product rule** both ways: P(A∧B) = P(A|B)P(B) = P(B|A)P(A), *"because it's commutative."*
- From the axioms: P(A ∨ ¬A) = P(A) + P(¬A) − P(A ∧ ¬A) → 1 = P(A) + P(¬A) − 0 → **P(¬A) = 1 − P(A)**.
- **Joint distribution**: n Boolean variables → 2ⁿ atomic events summing to 1. *"Describing this can be very inefficient — exponential in the number of variables."*

### The cavity/toothache table

| | Toothache | ¬Toothache |
|---|---|---|
| **Cavity** | 0.04 | 0.06 |
| **¬Cavity** | 0.01 | 0.89 |

**Marginalize** by summing a row or column: P(toothache) = 0.05; P(cavity) = 0.10. Then **P(cavity | toothache) = 0.04/0.05 = 0.8** but **P(toothache | cavity) = 0.04/0.10 = 0.5**.

The asymmetry, made real: *"How many times have you gone to the dentist with no symptoms and they told you you have a cavity? Pretty common. So it's not easy to self-diagnose. But when you have toothache, it's almost certain you have a cavity."*

## Bayes Rule

Derived from the two definitions of conditional probability: equate the two expressions for P(A∧B), divide by P(A):

**P(B|A) = P(A|B) P(B) / P(A)**

**Extended Bayes rule** with extra evidence E — his memory trick: *"Start with the original Bayes rule and add E on the conditioning side of every term."* P(Y|X,E) = P(X|Y,E) P(Y|E) / P(X|E). Derived by repeatedly applying *the trick*: rewrite any conditional as joint/marginal, reorder the joint, factor again. Note the grouping: P(A|B,C) is A given (B and C), not (A|B) and C.

## The Rare Disease — Bad News, Good News

Test positive for a serious disease. Bad news: the test is **99% accurate**. Good news: the disease is **rare — 1 in 10,000**. *"Would you take that as good news?"*

The trap: 99% accuracy means **P(T|D) = 0.99**. What you care about is **P(D|T)** — *"our instinct is to guess this is similar to 0.99."*

Known: P(T|D) = 0.99; P(¬T|¬D) = 0.99, hence P(T|¬D) = 0.01; P(D) = 0.0001; P(¬D) = 0.9999.

P(T) = P(T|D)P(D) + P(T|¬D)P(¬D) = 0.99·0.0001 + 0.01·0.9999 = **0.010098**.

**P(D|T) = 0.99 · 0.0001 / 0.010098 ≈ 0.0098 — under 1%.**

*"So 0.99 was the bad news. 0.0098 is the good news."* If the disease were 1 in 100 instead, the two would nearly cancel and P(D|T) ≈ 0.99. Follow-up he posed: *"How accurate must the test be for P(D|T) > 0.95? Pretty accurate."*

**Total probability in population terms**: only a subpopulation is *tested*; among them some positive, some negative. P(T∧D) are the true positives, P(T∧¬D) the **false positives** — and with a rare disease the false positives swamp the true ones. Generalizes to any exhaustive variable: P(T) = Σᵢ P(T | X=xᵢ) P(X=xᵢ).

## Why Bayes Rule Matters in Practice

**P(T|D) is easy to estimate**: go to a hospital, find 100 known patients, run the test. **P(D|T) is hard**: you would have to test ~10,000 people on the street to find ~100 positives *before* you could check who is actually sick. Bayes rule lets you compute the hard one from the easy one.

**The prior P(D)** is *"a double-edged sword"*: it lets you proceed even when P(D) is not directly measurable — *"guess it given reasonable assumptions"* — but *"people might say it's subjective."* It also **changes over time** (seasonal disease), whereas **P(T|D) is fixed — it's the mechanics.**

## Causal vs. Diagnostic Knowledge

P(symptom | disease) is **causal** — disease causes symptom, relatively fixed. P(disease | symptom) is **diagnostic** — going backward from cough or fever to cold, COVID, or something serious — and it shifts whenever the disease prevalence shifts. Continued 03-04. See [[Uncertainty]].

## See Also

- [[CSCE 420 Spring 2026 — 02-27 Exam Rules, Practice Exam Walkthrough, Frame Problem, Uncertainty]]
- [[CSCE 420 Spring 2026 — 03-04 Midterm Review, Bayesian Updating, Belief Networks]]
- [[CSCE 420 Lecture 5 — Uncertainty and Probabilistic Reasoning]]
- [[Bayesian Networks]]
- [[CSCE 420]]
