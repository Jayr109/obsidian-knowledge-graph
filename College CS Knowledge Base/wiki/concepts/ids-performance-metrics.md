---
title: "IDS Performance Metrics"
type: concept
tags: [csce465, security, intrusion-detection, metrics, false-positives, detection-rate, roc-curve]
sources: [csce465-lecture-14-intrusion-detection-system]
course: CSCE 465
updated: 2026-11-16
---

How good is an [[Intrusion Detection Systems|intrusion detection system]]? [[CSCE 465]] answers with a 2×2 table, five probabilities, and a curve. The notation is fixed on one slide: **A** is the event that the IDS raises an **alarm**, **I** is the event that there really is an **intrusion**.

## The Confusion Matrix

| | Alarm: **T** | Alarm: **F** |
|---|---|---|
| **Intrusion (reality): T** | True Positive | **False Negative** |
| **Intrusion (reality): F** | **False Positive** | True Negative |

The two bold cells are the two ways to be wrong: a missed attack, and an alarm about nothing.

## The Five Rates

```
Detection (true positive) rate     P(A|I)
    False negative rate            P(¬A|I)    = 1 - P(A|I)

False positive rate                P(A|¬I)
    True negative rate             P(¬A|¬I)   = 1 - P(A|¬I)

Bayesian detection rate            P(I|A)
```

The slide groups them this way, with each complement indented under its partner. The two equalities are not on the slide; they follow because each pair shares a condition and covers both outcomes.

> **Which way each one conditions, derived.** The first four are conditioned on **reality** — they are rows of the matrix. Given that there is an intrusion, how often does the alarm sound? Those are properties of the detector alone, and they are what a vendor quotes.
>
> The fifth is conditioned on the **alarm** — a column of the matrix. Given that the alarm sounded, how often is there really an intrusion? That is the number the person answering the alarm lives with, and it depends on something the first four do not mention: how common intrusions are. Getting from the rows to the column is Bayes' rule, and the result is the [[Base-Rate Fallacy]].

## The ROC Curve

```
  % Detect
  100 |                                    .-----------  IDS1
      |                     .-------------'
      |   +--------------.-'---------------------------  IDS2
      |   |          .--'                            .
      |   |       .-'                           .
      |   |     .'                         .
      |   |    /                      .
      |   |   /                  .          (dashed diagonal)
      |   |  /              .
      |   | /          .
      |   |/      .
      |   |  .
    0 +---+------------------------------------------------
      0                                              100
                         % False Alarm
```

(A sketch of the slide's figure, not to scale.)

> Ideal system should have **100% detection rate with 0% false alarm**.

That is the top-left corner. The slide draws two systems. **IDS1** is a smooth curve that climbs steeply, bends, and keeps rising until it reaches 100% detection at 100% false alarm. **IDS2** rises almost vertically to a plateau and then stays flat. The two cross, and a dashed diagonal runs corner to corner beneath both.

> **Reading the figure, derived.** The slide has no caption beyond the ideal. Each point on a curve is one setting of the detector's threshold: loosen it and both rates rise together, so the curve is the set of trade-offs that detector can offer. The diagonal is what guessing achieves, where the alarm fires at the same rate whether or not there is an intrusion.
>
> The two curves cross, so **neither IDS is better everywhere**. Read off the figure, IDS2's plateau is at roughly three quarters detection and the crossing is at roughly 13% false alarm; those are estimates from a rendered slide, not stated values. Left of the crossing IDS2 detects more for the same false-alarm rate; right of it IDS1 does, and IDS2 can never exceed its plateau however many false alarms are tolerated. Which one to buy depends on the operating point — and the [[Base-Rate Fallacy]] says an IDS has to operate at the far left, where false-alarm rates are tiny.

## The Architecture Metrics

The same slide lists two properties that are not probabilities:

> **Architecture** — scalable; resilient to attacks

They come back as the requirements list on [[Network Intrusion Detection]], where *resilience to attacks upon the IDS itself* gets an exclamation mark.

## The Same Numbers Elsewhere

[[Biometrics]] does true-positive and false-positive arithmetic for combining two tests, and makes the point that a biometric match is statistical where a password match is exact. An IDS is statistical in the same way: it has error *rates*, and tuning it moves along a curve from one kind of error toward the other.

## See Also

- [[Base-Rate Fallacy]]
- [[Intrusion Detection Systems]]
- [[Misuse and Anomaly Detection]]
- [[Network Intrusion Detection]]
- [[Host-Based Intrusion Detection]]
- [[Biometrics]]
- [[Bayes Rule]]
- [[CSCE 465]]
