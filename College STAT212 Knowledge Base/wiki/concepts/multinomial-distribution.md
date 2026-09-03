---
title: "Multinomial Distribution"
type: concept
tags: [multinomial, binomial, categorical-data, probability]
sources: [lecture-06-categorical-data]
course: STAT 212
updated: 2026-07-04
---

The multinomial distribution is the fundamental model for categorical (count) data — it generalizes the binomial from 2 outcomes to $r \ge 2$ outcomes per trial. It underlies the [[Chi-Square Goodness-of-Fit Test]] and [[Contingency Tables and Chi-Square]].

## From binomial to multinomial

A **binomial** experiment: `n` independent trials, each a success/failure with $P(S)=p$; the number of successes $N$ has $P(N=x)=\binom{n}{x}p^x(1-p)^{n-x}$.

A **multinomial** experiment is the same but with `r` possible outcomes per trial, $P(\text{category } i) = p_i$, $\sum_{i=1}^r p_i = 1$. Let $N_i$ = number of trials in category `i` (so $\sum_i N_i = n$).

## The distribution

For nonnegative integers $n_1,\dots,n_r$ summing to `n`:

$$P(N_1=n_1,\dots,N_r=n_r) = \frac{n!}{n_1!\,n_2!\cdots n_r!}\, p_1^{n_1}\cdots p_r^{n_r},$$

and 0 otherwise. When $r=2$ this reduces to the binomial.

## Moments

$$E(N_i) = np_i, \qquad \mathrm{Var}(N_i) = np_i(1-p_i).$$

The $E(N_i) = np_i$ formula gives the **expected counts** used in every chi-square test.

## Sampling note

Randomly selecting `n` individuals *without replacement* from a large population is, to a good approximation, a multinomial experiment (exact only with replacement). Since populations are usually large/infinite, any `n` is fine. The $p_i$ are typically population proportions.

## See Also
- [[Chi-Square Goodness-of-Fit Test]]
- [[Contingency Tables and Chi-Square]]
