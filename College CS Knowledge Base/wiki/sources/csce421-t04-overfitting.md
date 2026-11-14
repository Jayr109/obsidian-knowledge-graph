---
title: "CSCE 421 T04 — Overfitting and Regularization"
type: source
tags: [lecture, csce421, overfitting, regularization, model-selection, cross-validation, polynomial-regression]
sources: []
course: CSCE 421
updated: 2026-09-22
---

Topic deck 4 of [[CSCE 421]], by [[Shuiwang Ji]]. 14 slides. The first deck that is **not** about building a new model — it is about the failure mode that appears once a model is flexible enough to fit anything. Introduces [[Overfitting]], [[Regularization]], and [[Model Selection]].

> **Extraction note:** this deck is unusually image-heavy — the polynomial fits, RMS curves, coefficient tables, and cross-validation diagrams are all figures with no extractable text. The prose below is complete; the numeric figures are not reproduced. Consult the PDF (`raw/CSCE421_T04-overfitting.pdf`) for the plots.

## Case Study: Polynomial Curve Fitting

The running example departs from the credit/digits examples of T01–T03 and follows Bishop's setup: observe a real-valued input $x$ and predict a real-valued target $t$ with a **polynomial function** of order $M$.

The coefficients are fit by minimizing the **sum-of-squares error function**, which *"measures the misfit between the function $y(x, \mathbf{w})$, for any given value of $\mathbf{w}$, and the training set data points."* This is the same squared error as [[Linear Regression]] — note that a polynomial in $x$ is still **linear in $\mathbf{w}$**, which is why the machinery carries over unchanged.

## How to Choose the Order $M$?

Four fits are shown: $M = 0$, $M = 1$, $M = 3$, $M = 9$. The deck's own observations:

- $M = 0$ (constant) and $M = 1$ (first order) give **rather poor fits**.
- $M = 3$ **seems to give the best fit**.
- $M = 9$ gives an **excellent fit to the training data** — but *"the fitted curve oscillates wildly and gives a very poor representation. This leads to over-fitting."*

The $M=9$ case is the point of the deck: perfect in-sample performance and useless out-of-sample performance are not in tension, they routinely coexist. See [[In-Sample and Out-of-Sample Error]].

## Over-fitting

Diagnosed by plotting **Root-Mean-Square (RMS) error** on training and test sets against $M$. Training RMS falls monotonically; test RMS falls then turns sharply upward. The deck labels the result **poor generalization**.

A separate slide shows the **polynomial coefficients** at each $M$. The coefficients of the $M=9$ fit are enormous in magnitude — the wild oscillation is achieved by large positive and negative terms nearly cancelling. This observation is what motivates the fix.

## Regularization

> One technique that is often used to control the over-fitting phenomenon in such cases is that of regularization, which involves **adding a penalty term to the error function in order to discourage the coefficients from reaching large values**.

> The coefficient $\lambda$ governs the **relative importance of the regularization term** compared with the sum-of-squares error term.

Two slides then show the **effect of the regularization parameter** and the resulting **polynomial coefficients**, which are visibly shrunk relative to the unregularized $M=9$ fit. Full treatment on [[Regularization]].

## Model Selection

The deck closes on the question $\lambda$ creates: *"Model selection: estimation of the optimal value of the regularization parameter."* Choosing $M$ and choosing $\lambda$ are the same kind of decision — a **hyperparameter** that cannot be fit by minimizing training error, because training error always prefers the more flexible option.

> In practice, **cross validation** is commonly applied for model selection.

Three closing slides cover model selection for machine learning (scikit-learn's cross-validation documentation), for deep learning (the train/validation/test split), and a final summary figure. See [[Model Selection]].

## See Also

- [[Overfitting]]
- [[Regularization]]
- [[Model Selection]]
- [[In-Sample and Out-of-Sample Error]]
- [[Linear Regression]]
- [[CSCE 421]]
- [[Shuiwang Ji]]
