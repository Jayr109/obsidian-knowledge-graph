---
title: "Genetic Algorithms"
type: algorithm
tags: [csce420, genetic-algorithms, evolution, fitness, neuroevolution]
sources: [csce420-lecture-06-machine-learning]
course: CSCE 420
updated: 2026-09-01
---

Genetic algorithms use **evolution as a problem-solving strategy**: maintain a population of candidate solutions, select by fitness, recombine, and mutate.

## The Loop

1. **Population of chromosomes**, each encoding one solution
2. **Selection** based on a fitness function — survival of the fittest
3. **Mating (cross-over)** and reproduction
4. **Random mutation**
5. → New generation

## Properties

- Each chromosome encodes a solution
- **Similar to hill-climbing search** — but as a **parallel** search over many points at once
- Works for both **immediate and delayed** reward

The relation to [[Hill Climbing]] is the useful framing: a GA is roughly a population of hill-climbers that exchange information, which is why it resists local optima better than a single climber and why the remedies overlap (see [[Beam Search]]'s role as a parallel alternative).

## Four Design Questions

- What is the **fitness function**?
- How is a chromosome **represented**, and what does it represent?
- How are individuals **selected**?
- How do individuals **reproduce**?

## Diversity

The central practical problem:

- Letting **only** successful individuals reproduce **seriously reduces the gene pool** — an "epidemic" can wipe out the population, and the solution will not generalize to new and unexpected conditions.
- A **converged population** is often found at a **local minimum**, not the global optimum.

Diversity is to a GA what temperature is to [[Simulated Annealing]]: the mechanism that keeps exploration alive against a purely greedy pull.

## Further Issues

- **Cross-over strategy** — success depends heavily on how genes are encoded
- **Not much theoretical understanding** of why it works so well
- **Crevices in the fitness landscape** — analogous to spikes in hill climbing
- How to **combine learning with evolution**; how to use **cultural leverage**

## GA as a Learning Algorithm

An individual chromosome does not appear to learn — but **the population over generations adapts**, and that is learning. The point becomes clearer when each chromosome encodes a **function** rather than a bare solution: at each generation the function's parameters are being adapted, and fitness is measured by using that function on the task.

## Neuroevolution

Evolving neural networks: chromosomes encode network **topology and connection weights**; evaluate, select, reproduce.

**Problem**: individual neurons doing good work may get lost when whole networks are the unit of selection. The deck's response is to evolve **individual neurons** and combine them into networks — so that a useful neuron is preserved on its own merit rather than perishing with a mediocre network.

## See Also

- [[Hill Climbing]]
- [[Simulated Annealing]]
- [[Neural Networks]]
- [[Reinforcement Learning]]
- [[Game AI Milestones]]
- [[CSCE 420]]
