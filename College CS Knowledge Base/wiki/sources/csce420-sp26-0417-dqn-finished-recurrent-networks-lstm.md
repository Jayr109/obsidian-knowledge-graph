---
title: "CSCE 420 Spring 2026 — 04-17 DQN Finished, Recurrent Networks and LSTM"
type: source
tags: [csce420, lecture-recording, spring-2026, dqn, target-value, recurrent-neural-networks, unrolling, backprop-through-time, vanishing-memory, lstm, gates, input-gate, forget-gate, output-gate, cell-state]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-04-17
deck: slide07
exam: final
updated: 2026-09-17
---

Spring 2026 lecture, 27 min (short Friday). Closes DQN with the target formula and results, then deep recurrent networks: why feed-forward nets forget order, unrolling an RNN into a feed-forward graph, why memory fades, and the LSTM unit's three gates and equations. Slides 07:62–75.

## DQN — The Target, Stated

**y = r + max_a′ Q̂(s′, a′)** — the **observed** reward plus the stale copy's estimate of the best next Q. *"This is the more accurate information, because this is observed, and this is estimated."* (The slides include a discount factor γ on the max term; he did not dwell on it.)

Results recap: DQN beat human scores on many Atari games **but not all**; game states that look different but are strategically similar land **near each other** in the hidden representation; the value function rises with urgency (e.g. "move up now" has a high Q); games that need **long-term memory** across screens were the hard cases. See [[Deep Q-Network]].

## Feed-Forward Nets Forget Order

Present input₁, input₂, input₃ → output₃ depends only on input₃. Swap the first two and output₃ is identical. In a recurrent net the **collective input** at step 3 = immediate input + the hidden activation copied from step 2, and that copy differs when the order differs — *"hence you have a different output."* RNNs *"care about how the input sequence is arranged."*

## Unrolling

Backprop assumed **no cycles**. An RNN has one, but *"if you limit to a finite number of iterations through the loop"* you can **unroll** it: draw the hidden layer once per time step with the recurrent edge going to the next copy, and the result *"is just a feed-forward neural network."* Supply targets at each step and train as usual (backprop through time).

**The problem**: by the time you reach a late step, early inputs have passed through many weight layers and *"kind of average out"* under interference from more recent inputs. *"It can't really remember too far in the past."* This *"seriously degraded the utility of RNNs"* until Hochreiter & Schmidhuber's **LSTM**.

## The LSTM Unit

Replaces a single sigmoid hidden unit with a structure that has **three gates** and a **memory cell C_t**.

| Input gate | Forget gate | Output gate | Behaviour |
|---|---|---|---|
| open | open | — | new input is **captured** into memory |
| closed | open | closed | current state **persists** across steps, nothing emitted |
| — | — | open | **release** the memory as output, keep the state |
| closed | closed | closed | memory **erased** |
| open | closed | open | acts like a **vanilla** unit |

**Only three kinds of input arrive**, despite the tangle of lines: (1) the immediate input **x_t**, which feeds every gate and the candidate node; (2) the previous output **y_{t−1}** (= h_{t−1}), likewise to every gate; (3) the previous memory **C_{t−1}**, into the input and forget gates and into the C_t update. He added the missing C_{t−1} lines to the slide by hand — *"this is actually very critical."* Output: **y_t**.

**Equations** (each line has its own weights and bias):
- i_t = σ(W_ix x_t + W_ic C_{t−1} + W_iy y_{t−1} + b_i) — the input gate is *"just the weighted sum of the three input influences."*
- f_t, o_t: same form.
- **C_t = f_t · C_{t−1} + i_t · tanh(W_cx x_t + W_cy y_{t−1} + b_c)** — forget gate 0 **overwrites** the old value; input gate 1 lets the new tanh candidate in. (He first mistook f for a weight, then corrected: *"these are the gates."*)
- **y_t = o_t · tanh(C_t)**.

**The fascinating part**: *"When should I turn on the input gate? When should I turn off the forget gate? You can't imagine how to specify that."* You don't — in the unrolled graph everything flows forward, so **all gate weights are trained by the same backprop**, from the error at the outputs. *"Amazingly, these hold on to something appropriate for the task."* Because C_t can be carried unchanged (f ≈ 1, i ≈ 0), the unit *"can remember things from very far back."* See [[Recurrent Neural Networks]].

## See Also

- [[CSCE 420 Spring 2026 — 04-15 Final Review Posted, CNN Representations, Deep RL, DQN]]
- [[CSCE 420 Spring 2026 — 04-20 LSTM Applications, Attention, Transformers]]
- [[Recurrent Neural Networks]]
- [[Deep Q-Network]]
- [[CSCE 420 Lecture 7 — Deep Learning]]
- [[CSCE 420]]
