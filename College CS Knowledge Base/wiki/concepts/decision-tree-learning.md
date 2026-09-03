---
title: "Decision Tree Learning"
type: concept
tags: [csce420, machine-learning, entropy, information-gain, id3, supervised]
sources: [csce420-final-practice, csce420-lecture-06-machine-learning]
course: CSCE 420
updated: 2026-09-01
---

Decision tree learning builds a classifier by recursively splitting the training set on attributes, choosing at each node the attribute that best separates the classes. "Best" is measured by **information gain** — the reduction in entropy achieved by the split. This is the ID3 family of algorithms.

## Entropy

For a set $E$ with a fraction $p_+$ of positive and $p_-$ of negative examples:

$$H(E) = -p_+ \log_2 p_+ - p_- \log_2 p_-$$

Useful values to recognize on sight, since exams are built around them:

| Composition | Entropy |
|---|---|
| All one class (pure) | $0$ |
| 50/50 split | $1$ |
| Any other | strictly between 0 and 1 |

## Information Gain

The expected entropy remaining after splitting $E$ on attribute $A$, subtracted from the entropy before:

$$Gain(E, A) = H(E) - \sum_{v \in values(A)} \frac{|E_v|}{|E|} H(E_v)$$

Choose the attribute with the largest gain. Because the weights $|E_v|/|E|$ sum to 1, gain is maximized by splits that produce **pure** subsets.

## Worked Example (Final Practice, Problem 5)

| Example | Attr 1 | Attr 2 | Class |
|---|---|---|---|
| X1 | a | y | + |
| X2 | b | n | + |
| X3 | b | n | + |
| X4 | a | y | − |
| X5 | c | n | − |
| X6 | c | n | − |

$E$ has 3 positive and 3 negative examples, so $H(E) = 1$.

**Split on Attr 1** (three values):

| Value | Examples | Class counts | Entropy |
|---|---|---|---|
| a | X1, X4 | 1+, 1− | $1$ |
| b | X2, X3 | 2+, 0− | $0$ (pure) |
| c | X5, X6 | 0+, 2− | $0$ (pure) |

$$Gain(E, Attr1) = 1 - \left[\tfrac{2}{6}(1) + \tfrac{2}{6}(0) + \tfrac{2}{6}(0)\right] = 1 - \tfrac{1}{3} = \tfrac{2}{3} \approx 0.667$$

**Split on Attr 2** (two values):

| Value | Examples | Class counts | Entropy |
|---|---|---|---|
| y | X1, X4 | 1+, 1− | $1$ |
| n | X2, X3, X5, X6 | 2+, 2− | $1$ |

$$Gain(E, Attr2) = 1 - \left[\tfrac{2}{6}(1) + \tfrac{4}{6}(1)\right] = 1 - 1 = 0$$

**Attr 1 should be tested first.** Attr 2 is worthless here — both of its branches are still exactly 50/50, so the split conveys no information about the class at all, and its gain is exactly zero. Attr 1 immediately resolves four of the six examples into pure leaves.

The problem's hint that "many of the entropy values give trivial values (0 or 1)" is the tell: every subset above is either pure or evenly split, so no logarithms actually need computing.

> Worked here from the problem statement; the practice exam ships without an answer key.

## From the Lecture

### The Restaurant Example

The running dataset: 12 examples $X_1 \dots X_{12}$ with ten attributes — Alternate, Bar, Fri/Sat, Hungry, **Patrons**, Price, Raining, Reservation, Type, Estimated wait — and the goal predicate **WillWait**.

The task: given positive and negative training examples, construct a decision tree describing a **concise** decision path, then classify new instances. **We want to test a small number of attributes, not the whole set.**

### What a Decision Tree Represents

The learned tree corresponds to:

```
(Patrons = Some)
∨ (Patrons = Full ∧ Hungry = Yes ∧ Type = French)
∨ (Patrons = Full ∧ Hungry = Yes ∧ Type = Thai ∧ Fri/Sat = Yes)
∨ (Patrons = Full ∧ Hungry = Yes ∧ Type = Burger)
```

**Decision trees represent a disjunction of conjunctions.** Each Yes-leaf contributes one conjunctive term; No-leaves contribute nothing.

### The Algorithm

```
function DECISION-TREE-LEARNING(examples, attributes, default) returns a tree
  if examples is empty then return default
  else if all examples have the same classification then return the classification
  else if attributes is empty then return MAJORITY-VALUE(examples)
  else
    best <- CHOOSE-ATTRIBUTE(attributes, examples)
    tree <- a new decision tree with root test best
    for each value v_i of best do
      examples_i <- elements of examples with best = v_i
      subtree <- DECISION-TREE-LEARNING(examples_i,
                                        attributes - best,
                                        MAJORITY-VALUE(examples))
      add a branch to tree with label v_i and subtree
    return tree
```

The three base cases are each doing distinct work: empty examples → fall back to the parent's majority; uniform classification → done; **out of attributes but examples still mixed** → the data is noisy or the attributes insufficient, so take the majority.

### Choosing the Attribute

`CHOOSE-ATTRIBUTE` maximizes **information gain**, using Shannon's information theory — see [[Entropy and Information Gain]]. Entropy measures average *surprisal*: a 50/50 split is high entropy, a 0/100 split is low. In the restaurant data the initial set and the "Full" subset are high entropy, while "None" and "Some" are low — those branches nearly settle the answer alone.

### Ockham's Razor as the Inductive Bias

> **The most likely hypothesis is the simplest one that is consistent with all observations.**

Memorizing all cases is possible but not useful; we want a pattern describing many cases concisely, i.e. **as few tests as possible before a decision** — a shallow tree. Information gain is how that preference is made executable. See [[Inductive Bias]].

### Reading the Result

- **Some attributes are never tested at all** — the greedy gain criterion simply never finds them worth splitting on
- **Odd paths can be generated** (the Thai food branch)
- **The tree can be incorrect for new examples** — exceptional cases

### Evaluating Accuracy

Divide examples into **training and test sets**, train on the former, measure accuracy on the latter. The learning curve plots percentage correct on the test set against training set size.

### Known Issues

- **Noise and overfitting**
- **Missing attribute values**
- **Multi-valued attributes** with many possible values
- **Continuous-valued attributes**

## See Also

- [[Machine Learning Paradigms]]
- [[Bayesian Networks]]
- [[Neural Networks]]
- [[CSCE 420]]
