---
title: "CSCE 420 Lecture 6 — Machine Learning"
type: source
tags: [lecture, csce420, machine-learning, decision-trees, neural-networks, som, genetic-algorithms]
sources: []
course: CSCE 420
exam: final
updated: 2026-09-01
---

Slide deck 6 of [[CSCE 420]], by [[Yoonsuck Choe]]. 124 slides. Covers machine learning fundamentals, decision tree learning, neural networks from perceptrons through backpropagation, self-organizing maps, recurrent networks, and genetic algorithms.

## Structure

| Slides | Section |
|---|---|
| 2–18 | What machine learning is; the three types; issues in each |
| 19–34 | Decision tree learning; entropy and information gain |
| 35–48 | Neural networks: biology, abstraction, classification |
| 49–59 | Perceptrons; linear separability; the XOR limitation |
| 60–85 | Multilayer feed-forward networks; backpropagation derivation |
| 86–111 | Unsupervised learning; self-organizing maps |
| 112–124 | Recurrent networks; genetic algorithms; neuroevolution |

## The Arc

The deck is organized as a historical and logical progression through representational power:

1. **[[Decision Tree Learning]]** — symbolic, interpretable, learns a disjunction of conjunctions
2. **[[Perceptron]]** — a single linear unit, which can compute AND/OR/NOT but **not XOR** (Minsky & Papert, 1969)
3. **[[Backpropagation]]** — multiple layers, which removes the limitation once a training rule exists
4. **[[Self-Organizing Map]]** — drop the teacher entirely
5. **[[Genetic Algorithms]]** — drop gradients entirely

Each step relaxes a constraint the previous one imposed.

## Results Worth Extracting

- **The perceptron geometry**: output 1 iff $x_2 > -\frac{w_1}{w_2}x_1 + \frac{w_0}{w_2}$, so the unit draws a line. **Without a bias the line must pass through the origin** and learning can only adjust its slope.
- **XOR is not linearly separable** — its true cases occupy diagonal corners. See [[Linear Separability]].
- **The sigmoid derivative trick**: $g'(x) = g(x)(1-g(x))$, so $g'(\sum_j W_{ij}a_j) = O_i(1-O_i)$ and the **forward-pass output is reused directly in the backward pass**.
- **Entropy measures average surprisal**; information gain is entropy minus the *weighted average* entropy after splitting. See [[Entropy and Information Gain]].
- **Ockham's razor as an implemented bias** — `CHOOSE-ATTRIBUTE` is how a preference for short trees becomes executable.
- **Curse of dimensionality**: 10 values per dimension needs $10^d$ samples, and a $50\times50$ image is 2,500-dimensional. See [[Curse of Dimensionality]].
- **The brain's energy figure**: $10^{-16}$ J per operation against $10^{-6}$ J in modern computers — ten orders of magnitude.
- **Unsupervised learning requires redundancy** — where input content is less than channel capacity. Without redundancy there is no structure to find.

## The Closing Caution

> **ML is good at solving problems, but not at posing problems** (Choe and Mann, 2012).

The instructor's own note, and it recurs in deck 7's list of fundamental open issues.

## Visual-Only Slides

The example-data scatterplots (8), the high-dimensional image diagram (9), the curse-of-dimensionality figure (12), the inductive-bias curves (13), the decision-tree figures (22–23, 31), the accuracy learning curve (32), all neural-network topology diagrams (36, 48, 61–62), the activation function plots (45–46), the perceptron geometry figures (52–57), the SOM lattice diagrams (88–91), and the GA population figures (116, 119, 122–123) are diagrams whose content is not recoverable from the text layer. The **restaurant dataset table** (slides 20–21, 24, 26–27) extracts as an unstructured column of values; its 12 examples and 10 attributes are captured in prose on [[Decision Tree Learning]].

## Pages Created

**New (11)**: [[Machine Learning]], [[Supervised Learning Issues]], [[Curse of Dimensionality]], [[Inductive Bias]], [[Entropy and Information Gain]], [[Perceptron]], [[Linear Separability]], [[Backpropagation]], [[Unsupervised Learning]], [[Recurrent Neural Networks]], [[Genetic Algorithms]]

**Reconciled (4)**: [[Decision Tree Learning]], [[Neural Networks]], [[Self-Organizing Map]], [[Reinforcement Learning]]

## See Also

- [[CSCE 420]]
- [[Yoonsuck Choe]]
- [[Machine Learning Paradigms]]
- [[Deep Learning]]
- [[SOM Notebook — Self-Organizing Maps (2D Grid)]]
