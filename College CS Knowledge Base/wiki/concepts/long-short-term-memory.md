---
title: "Long Short-Term Memory"
type: concept
tags: [csce420, lstm, rnn, gates, sequence-learning]
sources: [csce420-lecture-07-deep-learning]
course: CSCE 420
updated: 2026-09-01
---

LSTM (Hochreiter and Schmidhuber, 1997) fixes the central failure of plain [[Recurrent Neural Networks]]: they **cannot remember far into the past**.

## The Problem

RNNs are trained by **backprop through time** — unfold the recurrent loop into a feedforward network and apply the ordinary [[Backpropagation]] algorithm. The good news is that past input affects present output; the bad news, stated twice in the deck, is that the network **cannot remember too far into the past**.

## The Solution: Gates

LSTM adds a **built-in recurrent memory** that can be:

| Gate | Function |
|---|---|
| **Input gate** | Written |
| **Forget gate** | Reset |
| **Output gate** | Outputted |

Because the memory cell is written and cleared under *learned* control rather than overwritten every step, information can persist for many time steps — **long-term retention becomes possible**.

Training is unchanged: **unfold in time and use backprop as usual.** LSTM is an architectural fix, not a new learning rule — the same pattern as [[Convolutional Neural Networks]].

## Applications

- **Sequence classification**
- **Sequence prediction**
- **Sequence translation**

Google's production machine translation was LSTM-based (Wu et al., 2016).

## Superseded

The deck is candid that [[Transformers]] have since surpassed LSTMs, chiefly because attention parallelizes and recurrence does not.

## See Also

- [[Recurrent Neural Networks]]
- [[Transformers]]
- [[Backpropagation]]
- [[Deep Learning]]
- [[CSCE 420]]
