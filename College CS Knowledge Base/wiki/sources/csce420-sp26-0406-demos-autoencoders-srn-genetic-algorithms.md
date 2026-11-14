---
title: "CSCE 420 Spring 2026 — 04-06 Demos, Autoencoders, SRN, Genetic Algorithms"
type: source
tags: [csce420, lecture-recording, spring-2026, nettalk, alvinn, waymo, autoencoder, embeddings, momentum, stochastic-gradient-descent, self-organizing-maps, recurrent-neural-networks, simple-recurrent-network, elman, genetic-algorithms, crossover]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-04-06
deck: slide06
exam: final
updated: 2026-09-17
---

Spring 2026 lecture, 50 min. Audio/video demos of NETtalk and ALVINN, the autoencoder-as-compression pipeline finished, momentum and SGD, a skipped SOM section, recurrent networks with the Elman SRN worked on a sequence dataset, and genetic algorithms applied to network weights. Slides 06:110–135.

> **Exam-scope note.** He explicitly **skipped the Self-Organizing Maps section**: *"we'll skip this for now — let me mark that."* It is also excluded from the Fall 2025 final scope; see [[CSCE 420 Final Review]].

## Demos

**NETtalk (1986).** The dataset (linked on the course resources page as *NetTalk*) is a dictionary: word, phoneme string, stress marks. Same letter → different phonemes: the *a* in *aardvark* vs. *able*. The network outputs only the **phoneme**; a synthesizer produces sound. Early-training audio is babble; trained audio reads a word list (friend, sent, around, nut, read, soon, doubt, key, attention, lost — *attention* was mis-stressed) and a child's sentence about staying up until 9. *"Almost exactly 40 years ago… not some massive dataset, just a dictionary."*

**CMU NavLab / ALVINN.** History Channel clip: NavLab 1 needed a separate engine to power four workstations plus a supercomputer and ran at walking speed; NavLab 2 (Army Humvee) carried **ALVINN**, a neural net that *"learns to drive"* by watching a person drive for about 5 minutes. His own Waymo ride in Atlanta: LiDAR tracks every pedestrian and vehicle, changes lanes, no one in the driver's seat — *"unlike Tesla, which just depends on vision."*

## Autoencoders, Finished

Flatten a 10×10 image to a 100-vector; input = target. Pipeline: **100 → 10 hidden → 100**. Encode with the first weight layer, transmit or store the **10 numbers** (a tenfold reduction), decode with the second layer. *"Whatever representation is learned has very nice properties — it distills the features in the input. These are called **embeddings**."* See [[Autoencoders]].

## Momentum and Incremental Update

**Momentum**: add a fraction of ΔW(t−1) to ΔW(t) — the toy-car-rolling-over-a-small-hill analogy. The fraction *"could be pretty high too, depending on the dataset."*

**Batch vs. incremental** changes the error function itself: batch E(W) = Σ_{samples} Σ_{outputs} (t − o)²; incremental drops the outer sum, so each sample descends a **different** surface — this is **stochastic gradient descent**, and the noise helps escape local minima. Other tricks: add input noise; allow occasional **uphill** moves with small probability (cf. [[Simulated Annealing]]).

His own `bp.cc`: tanh activation; AND and OR converge fast (linearly separable); **XOR takes a while** to reach near-zero error.

## Self-Organizing Maps — Skipped

One-slide summary only: an unsupervised algorithm that lays out input vectors on a 2-D map so **map location encodes similarity** — dog near fox and wolf, lion near tiger and cat, birds clustered. His MS thesis applied it to MNIST: regions for each digit, and **transition regions** 1→7→9→4 for visually similar shapes.

## Recurrent Neural Networks

A **recurrent** network has a loop — self-loop, 2-hop, 3-hop, not necessarily at the same level. Hopfield networks (Hopfield, physicist) and Boltzmann machines (Hinton) — the 2024 Physics Nobel. *"Our brain is basically a huge recurrent neural network."*

**The big deal — memory.** A feed-forward net given input₁, input₂, input₃ produces output₃ from input₃ alone; swap the order of the first two and output₃ is **identical**. *"It's ignorant of any past input."* In an RNN the same input₃ gives a **different** output because the **context** differs.

**Simple Recurrent Network (Elman).** The hidden activation from step t−1 is **copied** into a context layer and fed in alongside input t. *"So the output₂ is not purely based on input₂, but partly on hidden₁, which encodes the input₁ signal."* The copy link has **no weights**; only the input→hidden and hidden→output connections learn — *"you can just use the same backpropagation algorithm."*

**Sequence-detection dataset**, worked: inputs 1,0,1,0,1,1,… with target 1 only after certain history. Students guessed 0-1-1; the answer is **"1 1" — output 1 whenever the current and previous inputs are both 1.** 0-1-1 *"is close"* — it matches some rows but misses others. See [[Recurrent Neural Networks]].

## Genetic Algorithms

More general than neural nets — any **parameterized solution** encoded as a **genome**. Loop: random population → evaluate **fitness** → rank → **selection** → **crossover** (pick a crossover point; take the prefix from parent 1, the suffix from parent 2) → random **mutation** → new generation. *"No computation of a gradient or anything."* Works best when the task is **decomposable** so that mixing partial solutions gives something usable.

### A student asked: the genome values are numbers, not an algorithm?

Yes — for a network with 8 weights the genome is just **(W₁…W₈)**. Crossover after position 3 gives a **hybrid network** with W₁–W₃ from parent 1 and W₄–W₈ from parent 2. He drew the resulting network, caught a mistake, and redrew. Continues 04-08. See [[Genetic Algorithms]].

## See Also

- [[CSCE 420 Spring 2026 — 03-31 Backprop II, Recorded Lecture]]
- [[CSCE 420 Spring 2026 — 04-08 HW4 Walkthrough, Genetic Algorithms, Neuroevolution]]
- [[Neural Networks]]
- [[Recurrent Neural Networks]]
- [[CSCE 420 Lecture 6 — Machine Learning]]
- [[CSCE 420]]
