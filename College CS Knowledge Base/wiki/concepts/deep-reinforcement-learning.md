---
title: "Deep Reinforcement Learning"
type: concept
tags: [csce420, deep-rl, dqn, policy-gradient, actor-critic, experience-replay]
sources: [csce420-lecture-07-deep-learning]
course: CSCE 420
updated: 2026-09-01
---

The deck's one-line definition is the clearest statement of why the combination matters:

> **Deep** = can process complex sensory input.
> **Reinforcement learning** = can choose complex actions.

Neither half suffices alone. Classical [[Reinforcement Learning]] assumed small discrete state spaces; deep networks supply perception, so RL can act from raw pixels.

## What Gets Replaced

Deep RL replaces components of the RL pipeline with neural networks:

- **Convolutional network** for input processing
- **Value function** (e.g. the $Q$ function)
- **Policy function** $\pi(s)$

Plus innovations: **experience replay** (a replay buffer), multitask learning, transfer learning, meta learning, imitation learning.

## Four Variations

| Approach | What is fitted |
|---|---|
| **Value-based** | Fit $Q(s_t, a_t)$, construct $\pi(s_t)$ from it (e.g. $\epsilon$-greedy). **[[Deep Q-Network\|DQN]]** is the example |
| **Policy gradient** | Fit $\pi(s_t)$ **directly** |
| **Actor-critic** | Fit $Q(s_t,a_t)$ and use it to improve the fit of $\pi(s_t)$ |
| **Model-based** | Directly model $p(s_{t+1} \mid s_t, a_t)$, then **plan** |

Model-based RL is the one that reconnects to the first half of the course: having learned a transition model, the agent can [[Planning|plan]] with it rather than only react.

## Why It Disrupted the Field

[[Reinforcement Learning]] lists the classical limitations — discrete states and actions as the norm, scalability problems, and theoretical guarantees resting on the unrealistic assumption that every state-action pair is visited infinitely often. The deck's verdict: **deep reinforcement learning disrupted a lot of those traditional assumptions and limitations.**

## See Also

- [[Deep Q-Network]]
- [[Reinforcement Learning]]
- [[Deep Learning]]
- [[Game AI Milestones]]
- [[CSCE 420]]
