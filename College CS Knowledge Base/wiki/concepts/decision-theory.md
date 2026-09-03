---
title: "Decision Theory"
type: concept
tags: [csce420, decision-theory, utility, expected-utility, rationality]
sources: [csce420-lecture-05-probabilistic-reasoning]
course: CSCE 420
updated: 2026-09-01
---

**Decision theory = probability theory + utility theory.** It is the general theory of rational decision under uncertainty, and it supplies the course's definition of rationality.

## Utility and Preference

An agent facing trade-offs must first have **preferences** among outcomes. **Utility theory** deals with these: how useful is a given result to the agent?

## The Principle of Maximum Expected Utility

> An agent is **rational** iff it chooses the action that yields the **highest expected utility**, averaged over all possible outcomes of that action.

This is a definition, not an empirical claim — and it is the same principle that makes chance nodes work in [[Expectimax]], where backgammon is the worked example.

## The Decision-Theoretic Agent

```
function DT-Agent (percept) returns action
  persistent: belief_state  -- probabilistic beliefs about the world
              action        -- the agent's action
  1. Update belief_state based on action and percept
  2. Calculate outcome probabilities for actions, given
     action descriptions and current belief_state
  3. Select the action with highest expected utility,
     given outcome probabilities and utility info
  4. return action
```

## Worked Example

| | Utility of resulting state | Probability |
|---|---|---|
| **Action 1** | 10 or 0 | 0.2, 0.8 |
| **Action 2** | 10000 or 0 | 0.001, 0.999 |
| **Action 3** | 5 or 0 | 0.799, 0.201 |

Expected utilities:

- Action 1: $10 \times 0.2 = 2.0$
- Action 2: $1000 \times 0.001 = 1.0$
- Action 3: $5 \times 0.799 = \mathbf{3.995}$ ← maximum

**Action 3 wins.** The example is constructed to defeat two bad heuristics at once: Action 2 has by far the largest payoff, and Action 1 the largest single-outcome utility among the likely ones — but neither maximizes the *product*. Expected utility is not "biggest prize" nor "most likely win."

> Note: the slide lists Action 2's utility as 10000 in the table but computes with 1000. The ranking is unaffected either way — with 10000 the expected utility would be 10.0 and Action 2 would win, so the arithmetic as shown (1000) is what produces the stated answer.

## See Also

- [[Uncertainty]]
- [[Probability Basics]]
- [[Expectimax]]
- [[Bayesian Networks]]
- [[CSCE 420]]
