---
title: "Reinforcement Learning"
type: concept
tags: [csce420, reinforcement-learning, q-learning, reward, mdp]
sources: [csce420-final-practice, csce420-lecture-01-introduction, csce420-lecture-06-machine-learning]
course: CSCE 420
updated: 2026-09-01
---

Reinforcement learning is the paradigm where an agent learns to act by interacting with an environment and receiving a scalar **reward**, rather than from labeled examples. There is no supervisor telling it the correct action — only a signal saying how well things went, often long after the decisive action was taken.

## Setting

At each step the agent observes a state $s$, chooses an action $a$, receives reward $r$, and transitions to a new state $s'$. The goal is to maximize expected cumulative discounted future reward:

$$R_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k}$$

with discount factor $0 \le \gamma < 1$.

## The Q-Function

The action-value function $Q(s,a)$ is the expected return from taking action $a$ in state $s$ and behaving optimally thereafter. Given $Q$, acting optimally is trivial:

$$a^* = \arg\max_a Q(s,a)$$

Q-learning updates $Q$ toward the Bellman target using observed transitions:

$$Q(s,a) \leftarrow Q(s,a) + \alpha\big[r + \gamma \max_{a'} Q(s',a') - Q(s,a)\big]$$

The **credit assignment problem** is what makes this hard: a reward arriving now may be due to an action many steps back. The $\gamma \max_{a'} Q(s',a')$ term is what propagates value backward through time.

## Why Tables Fail

Tabular Q-learning needs one entry per state-action pair. For an Atari game whose state is a raw video sequence, the state space is effectively the space of images — far too large to enumerate, and offering no generalization between similar frames. Replacing the table with a neural function approximator is [[Deep Q-Network]], and it is what put RL in the [[Deep Learning]] era.

## In the Course

Lecture 1 lists deep reinforcement learning among the mid-2010s advances — "behave based on perception and learn from reward" — with AlphaGo and AlphaStar as the headline results and Atari, VizDoom, Minecraft, and simulated robot locomotion as the illustrations. Final Practice Problem 9 assigns deep RL the application area **(B) robotics / autonomous driving**, reflecting that RL is the framework for *control*, where the output is an action rather than a label.

## From the Lecture

### The Formalism

$$s_0 \xrightarrow{a_0, r_0} s_1 \xrightarrow{a_1, r_1} s_2 \xrightarrow{a_2, r_2} \dots$$

with $s_{t+1} = \delta(s_t, a_t)$ and $r_{t+1} = \rho(s_t, a_t)$ — an agent exchanging actions for states and rewards with an environment.

The deck characterizes the three paradigms by **feedback density**: supervised learning has *dense* feedback, unsupervised has *none*, and reinforcement learning has **sparse feedback that alters the environment**. That last clause is what makes RL genuinely different — the agent's actions change the distribution of data it subsequently sees.

**Applications**: multi-agent control, robot control, game playing, scheduling.

### Two Technique Families

- **Value function-based**: Q-learning, Temporal Difference (TD) learning
- **Direct policy search**: neuroevolution, [[Genetic Algorithms|genetic algorithms]], policy gradient

### The Classical Limitations

- **Discrete states and actions were the norm**
- **Scalability** was an issue
- **Unrealistic assumptions** for theoretical guarantees — notably that every state-action pair is *visited infinitely often*
- Open problems: online learning, safety, transfer, imitation

> **Deep reinforcement learning disrupted a lot of these traditional assumptions and limitations.**

See [[Deep Reinforcement Learning]] for what replaced them.

## See Also

- [[Deep Q-Network]]
- [[Deep Learning]]
- [[Machine Learning Paradigms]]
- [[History of AI]]
