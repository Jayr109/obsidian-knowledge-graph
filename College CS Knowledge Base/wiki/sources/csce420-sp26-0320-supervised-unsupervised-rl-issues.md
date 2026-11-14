---
title: "CSCE 420 Spring 2026 — 03-20 Supervised, Unsupervised, RL Issues"
type: source
tags: [csce420, lecture-recording, spring-2026, dimensionality, generalization, catastrophic-forgetting, curse-of-dimensionality, inductive-bias, clustering, blind-source-separation, t-sne, reinforcement-learning]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-03-20
deck: slide06
exam: final
updated: 2026-09-17
---

Spring 2026 lecture, 51 min. The conceptual half of the ML deck: what dimensionality means, generalization and its research questions, the curse of dimensionality with numbers, inductive bias on a five-point dataset, the unsupervised task families with a live t-SNE demo, and the issues in traditional reinforcement learning. Slides 06:14–36. Post-midterm.

## An Image Is a Point

A 50×50 grayscale image is **2,500 columns** in the dataset — one row, one point in 2,500-dimensional space. *"It's a 2D image, but information-wise it's a 2,500-dimensional data point."* Nearby points are similar images — his own photo from 15 years ago (*"I wore glasses; I took LASIK"*), his childhood, his brother — while a dog is far away. *"This dimensionality is a very serious issue for machine learning, as we'll see."*

## Supervised Learning and Its Open Questions

**Regression** approximates a (usually continuous, possibly vector-valued) function; **classification** is discrete categorization. Techniques listed — neural nets, decision trees, SVMs (*"a minimal version of a neural network"*), RBFs, naive Bayes, k-NN — all available in **scikit-learn**, used in Spring's HW4.

**Generalization**: training accuracy 98%, novel-input accuracy maybe 93%. *"How well does your trained model do on inputs it has not seen? A very important question and metric."* **Sample complexity**: how many training samples to get test error below a threshold. These belong to **computational learning theory**, which has its own conference (COLT).

**Catastrophic forgetting** — *"unresolved even now"*: train on D₁ to 99%; train the same model further on D₂ to 99%; re-test on D₁ and *"the performance will degrade — the new parameters overwrite what you learned."* Online learning (data arriving in batches) makes this unavoidable. Retraining on D₁ ∪ D₂ works but *"cannot be done forever — when D₃ arrives you'd retrain on all three. Not feasible."*

## Curse of Dimensionality — With Numbers

10 samples tile a 1-D range [0, 10] nicely. In 2-D the same 10 points look sparse; in 3-D sparser still. To match 1-D density: **1-D needs 10, 2-D needs 10², 3-D needs 10³** — and 2,500-D needs 10²⁵⁰⁰, *"way beyond the physical limits of the universe. If you just applied computational learning theory, this really should not work at all."* CNNs handle 100×100 = 10,000-D inputs.

**Why it works anyway**: a random 2,500-vector rendered as an image is white noise. *"Recognizable images only occupy a very, very tiny region of the space — human faces here, dog faces there, cars there. That's the structure of the data space, and that actually helps."* Layers reduce dimensionality progressively.

## Inductive Bias — The Five-Point Exercise

Dataset (x, y): (1, 1.5), (2, 2), (3, 2), (4, 4), (5, 3); the true function is unknown. Three models: **ML1** piecewise-linear interpolation, **ML2** a high-degree polynomial through every point, **ML3** a low-degree polynomial that misses some. *"Which one would you choose?"*

A student noted the data might be **noisy** — *"a very good observation"* — in which case the low-degree ML3 is preferable. The choice encodes assumptions: exact fit vs. smooth approximation; continuous vs. not. **Inductive bias** is whatever principle the human brings to that choice. *"It's very important to look at the data — analysis, visualization — before you choose a machine learning algorithm."*

## Unsupervised Learning

- **Clustering**: three Gaussian clouds — three clusters. Zoom out and there may be **three or nine**, depending on scale. *"How many clusters are there is a non-trivial problem."*
- **Feature extraction**: recurring patterns in high-dimensional data.
- **Blind source separation**: two mixed signals (two people speaking; speech plus music) recovered from mixtures without knowing the sources or the mixing — **but you need as many mixtures as sources**, e.g. two microphones. A student asked whether diffusion models do this — *"different; you always need two separate mixtures for two sources."* Works on mixed images too. The classic method is **ICA**.
- **Dimensionality reduction — live t-SNE on MNIST** (he had ChatGPT generate the script): 784-D digit images → 2-D. Same-class digits form near-uniform clusters. Outliers are informative: a **9 lands among the 7s**; **3, 5, 8 sit near each other** — *"similar categories occupy nearby spaces."* Strip the colours and the clusters are still visible — *"if these were an ancient script you could still discover the discrete categories."* t-SNE is the most widely used; ISOMAP and locally linear embedding are alternatives (**manifold learning**); **PCA** is the lightweight traditional one — *"I recommend you try it."* [[Self-Organizing Map]] may be covered *"if we have the time."*

## Reinforcement Learning — Framing and Issues

No dataset; an agent observes a state, acts, receives the new state and a reward from an environment whose mechanism it does not know. **Policy** = function from state to action, chosen to maximize (discounted, accumulated) reward. Preference matters: policy 1 gives steady moderate reward; policy 2 gives low reward for a long time then extremely high. *"If you prefer immediate reward you pick policy 1 — but you get into trouble because you're not looking into the future."*

Issues in traditional RL: **discrete** states and actions, so **no high-dimensional inputs**; a **scalability** wall; theoretical guarantees resting on unrealistic assumptions — *"all state-action pairs visited infinitely often"*; online learning; **safety** for physical robots; sim-to-real transfer; imitation from human demos. **Deep RL** addresses the first two; details under DQN in the DL deck. See [[Reinforcement Learning]].

## See Also

- [[CSCE 420 Spring 2026 — 03-18 HW3 Walkthrough, Machine Learning Intro]]
- [[CSCE 420 Spring 2026 — 03-23 Decision Trees, Entropy]]
- [[CSCE 420 Lecture 6 — Machine Learning]]
- [[Machine Learning Paradigms]]
- [[CSCE 420]]
