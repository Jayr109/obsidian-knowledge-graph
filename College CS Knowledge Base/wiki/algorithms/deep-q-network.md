---
title: "Deep Q-Network"
type: algorithm
tags: [csce420, reinforcement-learning, dqn, atari, q-learning, deep-learning]
sources: [csce420-final-practice, csce420-lecture-07-deep-learning]
course: CSCE 420
updated: 2026-09-01
---

A Deep Q-Network (DQN) replaces the Q-table of tabular Q-learning with a neural network that approximates $Q(s,a)$. This makes [[Reinforcement Learning]] workable in state spaces too large to enumerate — most famously raw video frames from Atari 2600 games, where the state $s$ is a video sequence and the action $a$ is a joystick control (stick plus button).

## What the Network Outputs (Final Practice, Problem 10)

The question asks what values the DQN computes given the input video sequence $s$.

**Answer: one estimated Q-value per possible action** — that is, $Q(s, a_1), Q(s, a_2), \dots, Q(s, a_n)$ for the $n$ legal joystick controls, all produced in a single forward pass. Each output is an estimate of the **expected cumulative discounted future reward** obtained by taking that action in state $s$ and playing optimally thereafter — in Atari terms, the expected final game score.

The network does **not** output the action itself, and it does **not** output a probability distribution over actions. The agent gets its action by taking the argmax over the output units:

$$a^* = \arg\max_a Q(s,a)$$

usually with $\varepsilon$-greedy exploration during training.

## Why One Output Per Action

The alternative design — feed in $(s, a)$ together and output a single scalar — would need $n$ separate forward passes to choose a move, since the argmax requires every action's value. Emitting all $n$ values from a shared network computes them in one pass and lets the convolutional layers share perceptual features across actions. This is a design detail, but it is the one that makes real-time play feasible.

## Architecture Sketch

| Stage | Role |
|---|---|
| Input | Stack of recent frames (a sequence, so that velocity is observable) |
| Convolutional layers | Extract visual features — see [[Deep Learning]] |
| Fully connected layers | Map features to values |
| Output layer | One unit per action, holding $Q(s,a)$ |

Stacking frames matters: a single frame cannot reveal which way the ball is moving, so a single-frame state would not satisfy the Markov property the Q-function assumes.

> Worked here from the problem statement; the practice exam ships without an answer key.

## From the Lecture

Google DeepMind (Mnih et al., *Nature* 2015). **One of the earliest deep learning methods applied to a reinforcement learning domain** — the Q of DQN is the Q of Q-learning — demonstrated on **Atari 2600** game playing.

### The Mapping

| Element | Realization |
|---|---|
| **Input** | Video frames |
| **Output** | $Q(s,a)$ — the action-value function |
| **Reward** | Game score |

$Q(s,a)$ is the **value of taking action $a$ in state $s$**. The deck stresses: **the whole network implements $Q$** — it is not a lookup table with a network attached, the network *is* the value function.

That substitution is what breaks the classical scalability limit in [[Reinforcement Learning]]: a tabular $Q$ needs an entry per state, which is impossible for raw pixels, while a network generalizes across states it has never seen.

### Where It Sits

DQN is the **value-based** branch of [[Deep Reinforcement Learning]]: fit $Q(s_t,a_t)$, then construct a policy from it (e.g. $\epsilon$-greedy). The alternatives are policy gradient, actor-critic, and model-based.

**Experience replay** — a replay buffer of past transitions — is listed among the innovations that made this workable.

### End-to-End Learning

The deck's summary calls DQN **end-to-end machine learning with super-human performance**: raw pixels to action values with no hand-designed features, no game-specific engineering, and reward as the only supervision.

## See Also

- [[Reinforcement Learning]]
- [[Deep Learning]]
- [[Neural Networks]]
