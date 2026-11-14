---
title: "CSCE 420 Homework 4 — Probability, Learning, Deep Learning"
type: source
tags: [csce420, homework, hw4, belief-networks, intercausal-inference, information-gain, perceptron, xor, gradient-descent, cnn, lenet, fall-2026]
sources: []
course: CSCE 420
semester: Fall 2026
exam: final
updated: 2026-11-04
---

Homework 4 of the user's **Fall 2026** section, dated October 25, 2026. 100 points, 10 problems: 7 written and 3 programming. Archived as `raw/CSCE420_HW4_Fall2026.pdf` with the starter notebook `raw/CSCE420_HW4_Fall2026_ml.ipynb`. The sheet gives no due date, so check Canvas.

> **This is a live assignment.** This page records what is *asked*, the data the sheet supplies, and the errors in the sheet itself. It does not contain solutions.

> **Exam scope: `final`.** Decks 5, 6 and 7 all fall after the midterm cutoff. See [[CSCE 420 Final Review]].

| # | Type | Pts | Topic |
|---|---|---|---|
| 1 | Written | 5 | Joint probability from a belief network |
| 2 | Written | 5 | Intercausal inference |
| 3 | Written | 5 | Node ordering |
| 4 | Written | 6 | Depth-one decision trees |
| 5 | Written | 7 | Information gain by hand |
| 6 | Programming | 12 | Information gain in Python |
| 7 | Programming | 30 | Perceptron on AND, OR, XOR |
| 8 | Written | 5 | XOR from three perceptron units |
| 9 | Written | 5 | Gradient descent rule |
| 10 | Programming | 20 | LeNet variant on MNIST, in Colab |

## Part 1 — Uncertainty (Problems 1–3)

**P1.** Calculate P(JohnCalls, ¬MaryCalls, ¬Alarm, Earthquake, ¬Burglary) on the burglary network: Burglary and Earthquake point to Alarm, and Alarm points to JohnCalls and MaryCalls.

| Table | Values |
|---|---|
| P(B) | .001 |
| P(E) | .002 |
| P(A \| B, E) | T,T .95; T,F .94; F,T .29; F,F .001 |
| P(J \| A) | T .90; F .05 |
| P(M \| A) | T .70; F .01 |

The factorization and a worked example on this same network are in [[CSCE 420 Spring 2026 — 03-16 Belief Network Inference]].

**P2.** A camper's scenario: WildFire has two causes, Smoking and Lightening (the sheet's spelling). Give an example of intercausal inference by placing the three variables in the blanks of **P( _ | _ ) >> P( _ | _ , _ )**.

**P3.** Same scenario: what node ordering is appropriate for building the belief network? See [[Bayesian Networks]].

## Part 2 — Learning (Problems 4–9)

### Decision tree data (Table 1)

| Ex | A | B | C | D | E | Target |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 0 | 0 | N |
| 2 | 1 | 1 | 0 | 1 | 1 | N |
| 3 | 1 | 0 | 1 | 1 | 1 | N |
| 4 | 1 | 0 | 1 | 1 | 0 | N |
| 5 | 1 | 1 | 0 | 1 | 1 | N |
| 6 | 0 | 0 | 1 | 1 | 1 | Y |
| 7 | 0 | 0 | 1 | 0 | 0 | Y |
| 8 | 1 | 0 | 1 | 0 | 1 | Y |
| 9 | 1 | 1 | 1 | 1 | 0 | N |
| 10 | 0 | 0 | 1 | 0 | 0 | Y |
| 11 | 0 | 1 | 1 | 1 | 1 | Y |
| 12 | 1 | 0 | 0 | 1 | 1 | N |
| 13 | 0 | 1 | 0 | 0 | 0 | Y |
| 14 | 1 | 1 | 0 | 1 | 0 | N |

**P4.** For attributes **A, C and D**, draw a depth-one tree with that attribute at the root (three trees, 2 pts each). All attributes are binary, so each tree has two branches. Use the style of the sheet's Patrons figure: the root lists its + and − examples, and each branch lists the examples that reach it.

**P5.** (1) By hand, using the P4 trees, compute the information gain for A, C and D (2 pts each). (2) Say which attribute you would test first (1 pt). See [[Decision Tree Learning]].

**P6.** Write `infogain` in Python and use it on A, C and D. Example call: `infogain([6, 6], [[0, 2], [4, 0], [2, 4]])`, the Patrons split. **log2(0) must be checked for and treated as 0.**

### Neural networks

**P7.** (1) Write a perceptron in Python (*"roughly less than 20 lines"* for the core), test it on AND, OR and XOR, and plot the decision boundary [18]. Training rules:
- For each sample, compute δw and **update immediately** (online, not batch).
- Track the average error per epoch. Stop when it reaches 0, or after a fixed cap such as 1,000 epochs.

(2) For each function, run several sessions from different random initial weights and report where the final boundary landed [3 each]. *"XOR would not terminate, so stop it after a few steps."*

(3) For AND and OR, can the perceptron reach zero error **without training**, given random initial weights? Explain why or why not [3].

The data matrix can be defined in code, with no file loading. See [[Perceptron]].

**P8.** Show how to implement XOR by linking **three perceptron units**. No code. Draw (1) the network topology and (2) each unit's decision boundary in the input space, colour-coded to match its unit. A TensorFlow Playground screenshot of the right configuration is allowed. **Count units, not layers:** the sheet's example of 1 hidden layer with 3 units plus 1 output unit is 4 units in 2 layers, so that figure is not the answer shape. Input nodes do not count.

**P9.** Given **E(w) = ¼ w(w − 3)(w − 1)(w + 4)**, derive the rule Δw = −α dE/dw. See [[Gradient Descent]].

## Part 3 — Deep Learning (Problem 10)

Everything runs in Colab, and results go **at the end of the provided ipynb**.

**AI rules for this problem:**
- Show all prompts as a comment at the top of the code, plus the ChatGPT share link, added once the code works.
- **Do not paste the homework text as the prompt.** Write your own.
- Part (2) must be your own words: *"Do not use ChatGPT for this."*
- Per the syllabus, this is the only place AI tools are allowed, so P1–P9 are excluded.

| Part | Ask |
|---|---|
| (1) | First cell: generate a LeNet variant and train on MNIST. **2 conv layers, 5×5 receptive field, 25 channels per conv layer.** Experiment with epochs, batch size and so on. Target: **above 99% accuracy** |
| (2) | In your own words, comment what each layer does: `Sequential`, `Conv2D(25, (5,5), activation='relu', input_shape=(w,h,ch))`, `MaxPooling2D(2,2)`, `Flatten`, `Dense(84, relu)`, `Dense(10, softmax)`. The same applies if your code came out in PyTorch |
| (3) | Second cell: plot the first conv layer's kernels, `gray` colormap, 5×5 arrangement |
| (4) | Third cell: plot the first conv layer's feature maps for an input in category **3**, `gray` colormap, 5×5 arrangement |

See [[Convolutional Neural Networks]].

## The Starter Notebook

`ml_420_26fall.ipynb` has two working sections:

- **Infogain:** skeletons for `my_log`, `entropy` and `infogain`. `my_log` currently crashes on 0, and `entropy` and `infogain` do not return anything until you finish them.
- **Perceptron:** `plot_decision_boundary` is complete. `perceptron(inp, tgt, alpha=0.01, err_target=0.001)` shuffles the samples each epoch and leaves steps 1.1 to 1.4 to you (activate with the step function, compute the error, adjust the weights, sum the error).

Two things in the skeleton will bite if left alone:
- The line `error = 0.00001` forcefully ends training after one epoch. It has to be replaced with the real epoch error.
- The `while` loop has **no epoch cap**, so XOR runs forever until you add the cap the sheet asks for.

## Errors and Mismatches in the Sheet

These were found while ingesting. None has been confirmed by the instructor, so check Canvas for a correction, as happened with HW2's cut count.

| Where | What it says | Issue |
|---|---|---|
| P9 worked example | −0.1 × 2.6 = −2.6 | Arithmetic slip: it is **−0.26**. The method is unaffected |
| P6 | Patrons figure *"above in problem 3"* | The figure is in **Problem 4** |
| P10 (3), (4) | 25 channels in a 5×5 arrangement | The example figures are labelled 0–35, a 6×6 grid from a 36-channel run. Follow the text |
| Title | "CPSC 420" | The course is CSCE 420 |
| Notebook header | *"four sections below"* | Only two exist. Spring's version also had scikit-learn and gradient-descent code; neither is asked for this semester |
| Notebook comment | bias *"fixed value of 1.0"* | The code sets `BIAS = -1.0` |
| Notebook comment | *"white = 1, black = 0"* | `imshow` uses the default colormap, so expect yellow for 1 and purple for 0 |

## How It Differs From Spring

[[CSCE 420 Spring 2026 — 04-08 HW4 Walkthrough, Genetic Algorithms, Neuroevolution]] walks through the Spring version, and its problem numbers do **not** match this sheet. Fall drops the scikit-learn decision-tree problem and the gradient-descent programming problem, so gradient descent is written only (P9) and the perceptron becomes P7 at 30 points. The walkthrough's explanations of `infogain` and the perceptron skeleton still apply.

## See Also

- [[CSCE 420 Homework 3 — FOL, Resolution Prover, Prolog]]
- [[CSCE 420 Spring 2026 — 04-08 HW4 Walkthrough, Genetic Algorithms, Neuroevolution]]
- [[CSCE 420 Spring 2026 — 03-16 Belief Network Inference]]
- [[CSCE 420 Final Review]]
- [[Decision Tree Learning]]
- [[Perceptron]]
- [[Gradient Descent]]
- [[Convolutional Neural Networks]]
- [[CSCE 420]]
