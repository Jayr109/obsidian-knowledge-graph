---
title: "CSCE 421 HW1 Solutions — Linear Models for Handwritten Digits"
type: source
tags: [homework, solutions, csce421, logistic-regression, softmax-regression, cross-entropy, gradient-descent, features]
sources: []
course: CSCE 421
updated: 2026-10-20
---

Instructor-released solution key for Homework 1 of [[CSCE 421]], Fall 2026 — *"Linear Models for Handwritten Digits Classification."* 4 pages, 100 points across five questions. This is the **released answer key**, not a live assignment, so the answers are recorded here; coding answers are given as *"write your own code"* in the key itself and are summarized rather than reproduced.

The homework is the practical counterpart to [[CSCE 421 T02 — Logistic Regression for Binary Classification|T02]] and [[CSCE 421 T03 — Logistic Regression: From Binary to Multi-Class|T03]], run on the same 16×16 digit data those decks use.

## Q1 — Data Preprocessing (15 pts)

**(a) What does `train_valid_split` do and why is it needed?**

> Splits the original training set into training and validation sets. The validation set is used to **monitor generalization and help avoid overfitting**.

Exactly the role [[Model Selection]] gives the validation split.

**(b) Before testing, is it correct to retrain on the full original training set?**

> **Yes.** Using more training data can improve the fitted model. Because the validation set was taken from the original training set, it **can be included again after model selection**, while the **test set remains unseen**.

The distinction that matters: the validation set has already done its job once hyperparameters are chosen, so folding it back in is legitimate. The test set never is.

**(c) The two hand-crafted features.**

```
F_symmetry  = -(1/256) * sum_pixels | x - flip(x) |
F_intensity =  (1/256) * sum_pixels   x
```

These are the *intensity and symmetry* features named on [[CSCE 421 T02 — Logistic Regression for Binary Classification|T02]] slide 7, now with explicit formulas. Note symmetry is **negated** — a perfectly symmetric digit gives 0, and asymmetry drives the value down.

**(d) Why is the third feature always 1?**

> It supplies the **bias (intercept) term**, allowing the corresponding weight vector to have dimension `n + 1`.

The `x_0 = 1` augmented coordinate from [[Linear Models]].

**(e)** Convert classes 1 and 2 to labels `+1` and `-1`. **(f)** Visualize features without plotting the constant one — a scatter in symmetry–intensity space.

## Q2 — Cross-Entropy Loss (25 pts)

**(a) Loss for one sample**, `y in {-1,+1}`:

```
E(w) = ln( 1 + e^(-y w^T x) )
```

**(b) The gradient** — two equivalent forms, both given:

```
grad_w E(w) = - e^(-y w^T x) * y x / (1 + e^(-y w^T x))
            = - y x / (1 + e^(y w^T x))
```

The second form follows by multiplying numerator and denominator by `e^(y w^T x)`, and is the one to use in code — it avoids computing the same exponential twice. This matches the gradient derived from [[CSCE 421 T02 — Logistic Regression for Binary Classification|T02]] and drives the SGD update on its slide 28.

**(c) Why is evaluating the sigmoid unnecessary at a 0.5 threshold?**

> The prediction rule `y_hat = +1 if theta(w^T x) >= 0.5` is **equivalent to the linear test** `y_hat = +1 if w^T x >= 0`. Use the sigmoid when a **probability estimate** is required.

**(d) Does a threshold of 0.9 still give a linear boundary?**

> **Yes.** `theta(z) >= 0.9 <=> z >= ln(0.9/0.1) = ln 9 ≈ 2.197`, therefore `y_hat = +1 if w^T x >= ln 9`.

The boundary moves but stays a hyperplane — it is `w^T x = ln 9` instead of `w^T x = 0`.

**(e) Which property of logistic regression makes the boundary linear?**

> The sigmoid is **monotonic and bounded** on R. In particular, its **strict monotonicity** allows a constant probability threshold to be converted into a linear threshold on `w^T x`.

This is property 3 from [[Sigmoid Function]], and (d) is the generalization of the `theta(s)=0.5 <=> s=0` argument to any threshold.

## Q3 — Sigmoid Logistic Regression (25 pts)

Implementation of `_gradient` (from Q2b), `fit_BGD` / `fit_SGD` / `fit_miniBGD`, `predict` / `score` / `predict_proba`, and a decision-boundary plot.

```
w <- w - lr * grad E(w)_batch
```

> For **BGD**, the batch contains all training samples; for **mini-BGD**, a roughly equal-sized subset; for **SGD**, a single sample.

The three-way split from [[CSCE 421 T02 — Logistic Regression for Binary Classification|T02]] slide 29, now as code.

**(e) Reported result:** *"Test accuracy of around **94%** is achievable. The testing labels must also be converted to +1 and -1."*

## Q4 — Softmax Logistic Regression (25 pts)

**(a) The gradient**, as given in the key:

```
dL/dW = x [ p_1 - y_1   p_2 - y_2   ...   p_k - y_k ]

where x = [x_0, x_1, ..., x_n]^T
```

This is the **predicted minus true** result derived in the [[CSCE 421 T03 Notes — Softmax Regression Derivations|T03 notes]] — an outer product of the input with `(p - y)`, structurally identical to the `x^(l-1) (delta^(l))^T` form in [[Backpropagation]].

**(b)** mini-batch GD, **(c)** `predict` (via `np.argmax`) and `score`, **(d)** plot classes 0, 1, 2 with multi-class boundaries.

**(e) Reported result:** *"Test accuracy of around **86%** is achievable."*

Lower than the binary 94% — three classes is a harder problem on the same two features.

## Q5 — Softmax vs Sigmoid (10 pts)

Train both on classes 1 and 2 until convergence and compare.

> Both the softmax and sigmoid logistic classifiers can **converge to the same accuracy**. If `W1, W2` are the two softmax weight vectors and `W` is the sigmoid weight vector, the original solution observes the approximate relationship
>
> ```
> W2 - W1 ≈ W
> ```
>
> This illustrates the **equivalence of binary sigmoid logistic regression and the two-class case of softmax regression** (up to the class-label convention).

**This question is the empirical version of the T03 slide-14 proof.** That proof concludes `h_w(x) = [theta(w_hat^T x), 1 - theta(w_hat^T x)]` with `w_hat = w_1 - w_2`; here the observed relation is `W2 - W1 ≈ W`. The sign difference is the *"up to the class-label convention"* caveat the key itself flags — which of the two classes is designated `+1` flips the direction of the difference. See [[Softmax Regression]].

## See Also

- [[Logistic Regression]]
- [[Softmax Regression]]
- [[Sigmoid Function]]
- [[Cross-Entropy Loss]]
- [[Gradient Descent]]
- [[Model Selection]]
- [[CSCE 421]]
