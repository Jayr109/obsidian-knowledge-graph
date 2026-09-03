---
title: "Machine Learning Paradigms"
type: concept
tags: [csce420, machine-learning, supervised, unsupervised, reinforcement-learning]
sources: [csce420-lecture-01-introduction, csce420-final-practice, csce421-t01-linear-regression]
course: CSCE 420, CSCE 421
updated: 2026-08-25
---

Machine learning algorithms are classified by what kind of feedback the learner receives. The distinction is exam-relevant because you can usually read the paradigm straight off the **learning equation**: look for what supervisory signal appears in it.

## The Three Paradigms

| Paradigm | Training data | Signal in the update rule | Examples |
|---|---|---|---|
| **Supervised** | $(x, y)$ pairs — input and label | An error against a target $y$ | [[Decision Tree Learning]], perceptron, CNN classifiers |
| **Unsupervised** | $x$ only — no labels | Structure in the input itself | [[Self-Organizing Map]], clustering |
| **Reinforcement** | States, actions, and a scalar reward | Reward, often delayed | Q-learning, [[Deep Q-Network]] |

## Machine Learning Primer (Lecture 1)

The lecture's primer slide states the supervised case plainly: **learn from data pairs of the form $(x = \text{PATTERN},\ y = \text{LABEL})$, so that the system can recognize novel input $x$ not seen during training.** It gives two illustrative datasets — a logic operation over binary $x_1, x_2$, and an animal-recognition set mapping images to Dog/Cat labels — and notes that *deep learning is a form of machine learning*, not a separate thing.

Generalization to unseen input is the actual goal; fitting the training data is only the means.

## Identifying the Paradigm From an Update Rule (Final Practice, Problem 8)

The problem gives the [[Self-Organizing Map]] learning equation

$$\mathbf{w}_j \leftarrow \mathbf{w}_j + \alpha \Lambda(i(\mathbf{x}), j)(\mathbf{x} - \mathbf{w}_j)$$

and asks which paradigm SOM belongs to. **Answer: (2) Unsupervised Learning.**

The equation is the evidence. Every term on the right is either a weight ($\mathbf{w}_j$), a hyperparameter ($\alpha$), a function of the network's own geometry ($\Lambda$, the neighborhood function, and $i(\mathbf{x})$, the index of the best matching unit), or the input itself ($\mathbf{x}$). **There is no target value and no reward anywhere in it.** The error term $(\mathbf{x} - \mathbf{w}_j)$ measures distance from the *input*, not from a label — so the map organizes itself around the structure of the input distribution.

> Worked here from the problem statement; the practice exam ships without an answer key.

## The CSCE 421 Framing

[[CSCE 421]] states the same three paradigms with a sharper split inside the supervised case:

| Paradigm | Mapping | Sub-types |
|---|---|---|
| **Supervised** | $x 	o y$ | *Classification* — $y$ discrete (binary or multi-class); *Regression* — $y$ continuous |
| **Unsupervised** | $x$ | Clustering, density estimation |
| **Reinforcement** | Sequential decision making | Noted as useful in training LLMs |

The classification/regression split is what organizes that course's opening arc: [[Linear Regression]] is the regression case, [[Logistic Regression]] the binary classification case, and [[Softmax Regression]] the multi-class case — all three built on the same [[Linear Models|linear signal]].

The course also motivates supervision by contrast: a large arithmetic computation needs no intelligence, while *"is there a tree in the photo?"* cannot be written as a rule and must be learned from labeled examples.

## See Also

- [[Linear Models]]
- [[Self-Organizing Map]]
- [[Decision Tree Learning]]
- [[Neural Networks]]
- [[Reinforcement Learning]]
- [[Deep Learning]]
- [[CSCE 421]]
