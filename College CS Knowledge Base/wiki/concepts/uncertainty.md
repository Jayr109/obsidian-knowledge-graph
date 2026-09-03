---
title: "Uncertainty"
type: concept
tags: [csce420, uncertainty, degree-of-belief, prior, posterior, evidence]
sources: [csce420-lecture-05-probabilistic-reasoning]
course: CSCE 420
updated: 2026-09-01
---

Agents almost never have full access to the truth about their environment, so they must **act under uncertainty**. This lecture is the pivot from logic to probability: where [[First-Order Logic]] forces every sentence to be True or False, probability lets an agent hold a **degree of belief**.

## Why First-Order Logic Fails in Uncertain Domains

The three reasons, given for medical diagnosis:

| Reason | Meaning |
|---|---|
| **Laziness** | Cannot list the complete set of antecedents and consequents needed for an exceptionless rule — and the resulting rules would be too unwieldy to use |
| **Theoretical ignorance** | Medical science has **no complete theory** |
| **Practical ignorance** | Even with all the rules, running every test is impossible |

The same situation arises in law, business, and dating. The agent's knowledge can at best provide a **degree of belief** — and probability theory is well suited to exactly that.

Note that these are three genuinely different failures: laziness is about *representation cost*, theoretical ignorance about *missing science*, practical ignorance about *unaffordable evidence*. Only the first could in principle be fixed by more effort.

## The Motivating Example

Plan $A_t$: leave home $t$ minutes before departure to catch a flight.

The car can break down, traffic can jam, a natural disaster can strike — and the list does not terminate: out of gas, family emergency, crew strike. The traveller has only an **incomplete understanding**. Playing safe with $A_{1440}$ (24 hours early) guarantees the flight but wastes a day.

**The right thing to do depends on both the relative importance of the goals and the likelihood they will be achieved** — which is precisely [[Decision Theory]].

## Prior and Posterior

Degree of belief changes as the agent acquires new information, called **evidence**:

- **Before** the evidence: **prior** (unconditional) probability
- **After** the evidence: **posterior** (conditional) probability

The lecture draws the analogy explicitly: this is like asking whether a sentence is entailed by a knowledge base, since **the truth value can change when new facts are added**. Probability generalizes entailment rather than replacing it.

In blackjack, as cards are shown, your belief that you need another card changes. The deck poses poker and slot machines as contrasts worth thinking about — poker adds hidden opponent information, a slot machine adds none at all.

## See Also

- [[Decision Theory]]
- [[Probability Basics]]
- [[Bayes Rule]]
- [[Bayesian Networks]]
- [[CSCE 420]]
