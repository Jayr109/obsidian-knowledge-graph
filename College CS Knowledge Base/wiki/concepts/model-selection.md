---
title: "Model Selection"
type: concept
tags: [csce421, model-selection, cross-validation, hyperparameters, validation-set, train-test-split]
sources: [csce421-t04-overfitting]
course: CSCE 421
updated: 2026-09-22
---

Model selection is choosing the settings that training cannot choose for you — the polynomial order $M$, the [[Regularization]] strength $\lambda$, the network architecture. These are **hyperparameters**: they are fixed before fitting, and training error is systematically the wrong criterion for picking them.

## Why Training Error Cannot Decide

Training error falls monotonically with model flexibility. Selecting $M$ by training error always names the largest $M$; selecting $\lambda$ by training error always names $\lambda = 0$. **In both cases the answer is the overfitted one**, as the RMS curves in [[Overfitting]] show directly.

Test error has the shape you want — it bottoms out at the right complexity — but the test set cannot be used to choose, or it stops being an honest estimate of [[In-Sample and Out-of-Sample Error|$E_{out}$]]. Once you pick the model that scores best on a set, that score is optimistic for the same reason $E_{in}$ is.

## The Three-Way Split

The resolution used throughout [[Deep Learning]], and shown in the closing slides of [[CSCE 421 T04 — Overfitting and Regularization|T04]]:

| Split | Used for | Touched how often |
|---|---|---|
| **Training set** | fitting the weights | every step |
| **Validation set** | choosing hyperparameters, early stopping | once per candidate model |
| **Test set** | final honest estimate of $E_{out}$ | **once, at the very end** |

The validation set absorbs the selection bias so the test set stays clean. Reusing the test set for selection is the most common way a reported result becomes meaningless.

## Cross-Validation

> In practice, **cross validation** is commonly applied for model selection.

When data is scarce, a single held-out validation set is both wasteful and noisy. **$k$-fold cross-validation** instead splits the training data into $k$ folds, then for each candidate hyperparameter setting:

1. Train on $k-1$ folds, evaluate on the held-out fold.
2. Repeat $k$ times, each fold serving as validation once.
3. Average the $k$ scores.

Every point is used for both training and validation, just never simultaneously. The averaged score is a lower-variance estimate than any single split, and the cost is $k$ trainings per candidate. The deck cites scikit-learn's cross-validation documentation for the mechanics.

## Where This Sits in the Course

T01 through T03 asked *given a model, how do I fit it?* and answered with the closed form and [[Gradient Descent]]. T04 asks the prior question — **which model should I be fitting?** — and the answer is empirical rather than analytic: try candidates, score them on data the fit never saw, pick the winner.

## See Also

- [[Overfitting]]
- [[Regularization]]
- [[In-Sample and Out-of-Sample Error]]
- [[Deep Learning]]
- [[CSCE 421]]
