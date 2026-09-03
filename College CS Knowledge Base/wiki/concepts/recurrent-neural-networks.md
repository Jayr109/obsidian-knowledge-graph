---
title: "Recurrent Neural Networks"
type: concept
tags: [csce420, rnn, elman, hopfield, sequence, memory]
sources: [csce420-lecture-06-machine-learning]
course: CSCE 420
updated: 2026-09-01
---

A recurrent network's connection graph **contains cycles** — reciprocal connections, so it is not strictly feed-forward. The consequence is memory:

| Network | Behavior |
|---|---|
| **Feedforward** | **No memory** of past inputs; output depends only on the present input |
| **Recurrent** | **Past inputs affect the present output** |

## Families

- **Statistical-mechanics based** (associative or content-addressable memory): Hopfield networks, Boltzmann machines
- **Sequence encoding**: Simple Recurrent Network and successors
- **Biologically motivated**: laterally connected self-organizing maps

Elsewhere the deck also names LSTM and GRU among recurrent architectures.

## Simple Recurrent Network (Elman Network)

The concrete architecture given:

- Input, hidden, and output layers, plus a **context** layer
- The **hidden layer activation from the previous time step** is fed back as input via a one-step delay
- **Trained with standard backpropagation** — no new learning algorithm required

The context layer is the memory: it holds a compressed summary of everything seen so far, so the hidden layer's next state is a function of both the new input and the accumulated past.

**Example task**: output 1 when two 1s appear in a row. This cannot be done by a feedforward network on single inputs — the answer depends on what came *before*, which is exactly what recurrence supplies.

## Relation to the Rest of the Course

Recurrence is how a network handles **sequences**, and it is the architectural ancestor of the Transformer mentioned in [[Deep Learning]] as an alternative way of conditioning on context.

## See Also

- [[Neural Networks]]
- [[Backpropagation]]
- [[Deep Learning]]
- [[Self-Organizing Map]]
- [[CSCE 420]]
