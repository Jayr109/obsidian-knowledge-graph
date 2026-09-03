---
title: "Maximum Likelihood Estimation"
type: concept
tags: [csce421, maximum-likelihood, likelihood, cross-entropy, probabilistic-modeling]
sources: [csce421-t02-logistic-regression]
course: CSCE 421
updated: 2026-08-25
---

Maximum likelihood estimation picks the parameters under which the observed data would have been most probable. In [[CSCE 421]] it is the justification for [[Cross-Entropy Loss]] — the loss is *derived* from the probabilistic model rather than chosen for convenience.

## The Likelihood

Given a model $h$ with $P(y\mid\mathbf{x})$ and independently generated samples $(\mathbf{x}_1,y_1),\dots,(\mathbf{x}_N,y_N)$, the likelihood is the probability of observing the labels we actually observed:

$$P(y_1,\dots,y_N \mid \mathbf{x}_1,\dots,\mathbf{x}_N) = \prod_{n=1}^{N}P(y_n\mid\mathbf{x}_n)$$

Independence is what turns the joint probability into a product — and the product into a sum once we take logarithms.

> The likelihood measures the probability that the data were generated if $f$ were $h$.

The logic runs backwards from usual: rather than asking how probable the parameters are, we ask how probable the *data* is under each candidate, and prefer whichever makes the observations least surprising.

## From Likelihood to Loss

The chain from maximizing likelihood to minimizing cross-entropy, as given for [[Logistic Regression]]:

$$\max \prod_{n=1}^{N}P(y_n\mid\mathbf{x}_n) \;\Leftrightarrow\; \max \ln\!\left(\prod_{n=1}^{N}P(y_n\mid\mathbf{x}_n)\right) \;\equiv\; \max \sum_{n=1}^{N}\ln P(y_n\mid\mathbf{x}_n)$$

$$\Leftrightarrow\; \min\, -\frac{1}{N}\sum_{n=1}^{N}\ln P(y_n\mid\mathbf{x}_n) \;\equiv\; \min\, \frac{1}{N}\sum_{n=1}^{N}\ln\frac{1}{P(y_n\mid\mathbf{x}_n)}$$

Each step is worth naming:

| Step | Justification |
|---|---|
| Product $\to$ log | $\ln$ is monotonic, so the maximizer is unchanged; products become sums |
| Max $\to$ min | Negate |
| Divide by $N$ | Scaling by a positive constant does not move the argmin |

So far this is model-independent. **Specializing to the model** happens in one step — substituting $P(y_n\mid\mathbf{x}_n) = \theta(y_n\mathbf{w}^T\mathbf{x}_n)$:

$$\min \frac{1}{N}\sum_{n=1}^{N}\ln\frac{1}{\theta(y_n\mathbf{w}^T\mathbf{x}_n)} \;\equiv\; \min \frac{1}{N}\sum_{n=1}^{N}\ln\left(1+e^{-y_n\mathbf{w}^T\mathbf{x}_n}\right)$$

which is exactly the cross-entropy error $E_{in}(\mathbf{w})$.

## Why This Matters

The lecture introduces cross-entropy first as an unmotivated formula that "looks complicated and ugly," then earns it. Two payoffs:

- **The loss is not arbitrary.** Any other error measure would implicitly assume a different probabilistic model.
- **The compact form is load-bearing.** The derivation only works because $\theta(-s) = 1-\theta(s)$ lets both label cases fold into $\theta(y\,\mathbf{w}^T\mathbf{x})$ — see [[Sigmoid Function]].

The same argument generalizes to $K$ classes, where the negative log-likelihood of the correct class is the multi-class cross-entropy of [[Softmax Regression]].

## See Also

- [[Cross-Entropy Loss]]
- [[Logistic Regression]]
- [[Sigmoid Function]]
- [[Softmax Regression]]
- [[CSCE 421]]
