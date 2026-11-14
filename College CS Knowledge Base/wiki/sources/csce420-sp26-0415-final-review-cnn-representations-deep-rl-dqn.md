---
title: "CSCE 420 Spring 2026 — 04-15 Final Review Posted, CNN Representations, Deep RL, DQN"
type: source
tags: [csce420, lecture-recording, spring-2026, final-review, exam-scope, cnn-representations, hidden-vector, t-sne, imagenet-visualization, vgg, resnet, skip-connections, spectrogram, vision-transformers, deep-reinforcement-learning, q-function, value-function, policy, model-free, model-based, dqn, target-network, experience-replay, epsilon-greedy]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-04-15
deck: slide07
exam: final
updated: 2026-09-17
---

Spring 2026 lecture, 50 min. The **final exam review page** was posted and its scope stated; then what a CNN's hidden vector "means," Karpathy's t-SNE map of ImageNet, the post-AlexNet architecture race, CNNs on spectrograms, and the first half of deep reinforcement learning — Q/value/policy functions, the algorithm taxonomy, and DQN's target-network trick. Slides 07:45–62.

> **Final scope, restated.** One question on **propositional-logic theorem proving**; questions on **planning**, **uncertainty and probability**, **machine learning** — **Self-Organizing Maps will NOT be on the exam** — and **deep learning**. **AI Ethics will not be on the exam.** Final exam May 5. HW4 due the following Tuesday. See [[CSCE 420 Final Review]].

## What a CNN's Hidden Vector Encodes

Feed a reference image; take its **4,096-d hidden representation**; scan all 1.2 M ImageNet images for the 6 whose hidden vectors are closest. Results: the same pink flower under different lighting and backgrounds; elephants in varied poses — *"pixel-wise different images have a similar representation."*

**The two-tone dog row** is the cautionary case: the reference is one dog with two colour patches; one match is **a solid-white dog and a solid-black dog standing together**. *"To the CNN, this dog with a mixed pattern is basically the same as two dogs of solid colour."* Lesson: the network may be learning **superficial patterns**, not what a human brain represents.

## Karpathy's t-SNE Map of ImageNet

Each image is a point in a very-high-dimensional space; **t-SNE** projects to 2-D so nearby images sit together. Regions: bluish (ocean, ships, fish), greenish (vegetation), reddish-orange (fruit, food), insects transitioning into flowers, electrical gadgets, black-top objects, round things (spiral staircase, pot lids). *"Not perfect"* — yachts sit next to **solar panels**. *"All of this is based on the appearance, not the function of the objects."* A 6000×6000 version is linked.

## The Architecture Race After AlexNet

ImageNet = **ILSVRC**; 2012 was its **third** year (he corrected himself). AlexNet: 8 layers. **VGG** (2014): nearly the same architecture, **more layers**, better error. **ResNet**: **152 layers**, error greatly reduced. Then people realized flat stacks are not enough — **architectural modules**: GoogLeNet's bottleneck, ResNet's **skip connections**, DenseNet's dense skips. *"From this point on, people started paying attention to the architecture."*

The bubble chart: x = compute, y = **top-1 accuracy**, bubble size = parameters (~10 M to ~125 M). AlexNet ≈ 55% top-1; the same architecture scaled up gained ~15 points; lean models like **Inception** hold accuracy at a fraction of the compute.

**CNNs beyond vision**: turn a WAV into a **spectrogram** (x = time, y = frequency, brightness = power) — a standard-size image — and classify words with a CNN. *"Nowadays no one uses CNNs for speech; everything is transformer-based"* — and even in vision, **vision transformers** are replacing CNNs.

## Deep Reinforcement Learning — Vocabulary

**Deep** = a deep network processes complex sensory input; **RL** = learn from **rewards** to choose actions. Deep RL has *"overtaken all the traditional RL work"* by replacing RL components with networks: a CNN front-end for high-dimensional input, a back-end network for the **value** or **policy** function.

| Function | Signature | Meaning |
|---|---|---|
| **Q(s, a)** | state × action → value | how good is taking a in s, long-term. Q(s,a₁)=0.9, Q(s,a₂)=0.7, Q(s,a₃)=1.1 → pick a₃ |
| **V(s)** | state → value | how good is being in s; useful if you know where each action leads |
| **π(s)** | state → action | the **policy**; an optimal π hands you the best action directly |

### A student asked: is the value a probability?

**No.** *"It's related to the reward. If the reward is on the order of 1,000, the value might be a thousand or two thousand."*

Active research themes: **experience replay** (store (s, a, r, s′) tuples in a buffer, sample from it), multitask, transfer, meta-, imitation learning.

## Taxonomy

- **Model-based**: learn or are given δ(s, a) (state transition) and ρ(s, a) (reward) — e.g. board games where the rules are explicit.
- **Model-free**: *"I don't care about the model — I just observe"* the resulting state and reward the environment hands back.
  - **Policy optimization**: policy gradient, A2C/A3C, PPO, TRPO.
  - **Q-learning** (value-based): **DQN** — covered in detail.
  - Hybrids with both policy and value networks: DDPG.

Pointer: the UC Berkeley deep RL course and its YouTube lectures.

## DQN — Structure

Input: **not one frame but 4–7 recent frames** for temporal context; conv layers; fully-connected layers; output layer of **18 units** = 8 joystick directions, 8 directions with the button, button only, do nothing. **The outputs are Q-values, not actions** — *"this is very important."* Which action to take is delegated to whatever selection rule you use (ε-greedy below). See [[Deep Q-Network]].

## DQN — How Do You Train It Without True Q-Values?

Supervised learning needs a target; the true Q\* is unknown. The only hint is the **reward** — the score went up 1,000, or didn't, or your unit died. *"Reward is the currency of the Q function."*

**Target-network trick** (his best attempt at the algorithm):
1. Start with network Q; **copy its weights to Q̂**.
2. In state s, compute Q(s, a) for all a; execute one action; observe s′ and reward r.
3. Build a **surrogate target y = r + (Q̂'s estimate at s′)** — *"the observed reward combined with the old estimate — slightly better than Q."*
4. Loss = (y − Q(s, a))²; gradient step on Q's parameters ζ.
5. Keep using the **stale Q̂** for several steps, then **refresh** it from the now-more-accurate Q — the *"delayed periodic update."*

**Terminal case**: if the episode ended, there is no future reward, so **y = r exactly** — equal to Q\* for that transition.

**Input preprocessing** φ(s_t) of the frame stack; transitions (φ_t, a_t, r_t, φ_{t+1}) go into **replay memory D** of capacity N; updates use a **random mini-batch** from D, not the latest step.

**ε-greedy** (he double-checked the direction live): with probability **ε take a random action**; with probability **1 − ε take the greedy action** argmax_a Q(s, a). High ε → mostly random; low ε → mostly greedy.

**Algorithm skeleton**: init D; init Q with random ζ; Q̂ ← Q. For each of M episodes (start of game to end): init frame sequence; each step: ε-greedy action → emulator → (r, next frame) → store transition → sample mini-batch → compute y (r if terminal, else r + Q̂ term) → gradient step. Ran out of time at the y formula; continues 04-17.

## See Also

- [[CSCE 420 Spring 2026 — 04-13 Final Practice Walkthrough, Deep CNNs, AlexNet]]
- [[CSCE 420 Spring 2026 — 04-17 DQN Finished, Recurrent Networks and LSTM]]
- [[CSCE 420 Final Review]]
- [[Deep Q-Network]]
- [[Deep Reinforcement Learning]]
- [[CSCE 420 Lecture 7 — Deep Learning]]
- [[CSCE 420]]
