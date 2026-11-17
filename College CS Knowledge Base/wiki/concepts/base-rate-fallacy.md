---
title: "Base-Rate Fallacy"
type: concept
tags: [csce465, security, intrusion-detection, base-rate, bayes-rule, false-positives, probability]
sources: [csce465-lecture-14-intrusion-detection-system]
course: CSCE 465
updated: 2026-11-16
---

The **base-rate fallacy** is judging how much to trust an alarm from the detector's accuracy alone, while ignoring how rare the thing being detected is. In [[CSCE 465]] it is the central quantitative result of the intrusion detection lecture: an [[Intrusion Detection Systems|IDS]] with a tiny false alarm rate can still be wrong most of the times it rings, because intrusions are rarer still.

Notation, from [[IDS Performance Metrics]]: **A** is an alarm, **I** is an intrusion.

## Bayesian Detection Rate

The probability that an alarm is a real intrusion:

```
                      P(I) · P(A|I)
P(I|A)  =  ---------------------------------------
            P(I) · P(A|I)  +  P(¬I) · P(A|¬I)
```

The numerator is real intrusions that raise an alarm. The denominator is *everything* that raises an alarm: the same real ones, plus false alarms from the non-intrusions. **P(I)** is the **base rate** — how often the monitored events are intrusions at all.

## The Fallacy

> Even if false alarm rate `P(A|¬I)` is very low, Bayesian detection rate `P(I|A)` is still low if base-rate `P(I)` is low.

## The Lecture's Example

> E.g. if `P(A|I) = 1`, `P(A|¬I) = 10⁻⁵`, `P(I) = 2×10⁻⁵`, then `P(I|A) = 66%`

A detector that **never misses**, with a false alarm rate of **one in a hundred thousand**, is right two times in three.

**Verified during ingest.** The slide's 66% is 0.6667, rounded down:

```
numerator    =  2×10⁻⁵ × 1                          =  2×10⁻⁵
denominator  =  2×10⁻⁵  +  (1 − 2×10⁻⁵) × 10⁻⁵     =  2.99998×10⁻⁵
P(I|A)       =  2×10⁻⁵ / 2.99998×10⁻⁵               =  0.6667
```

> **In counts, derived.** Take a million events. Twenty are intrusions, and all twenty raise an alarm. The other 999,980 are harmless, and one in a hundred thousand of them raises an alarm too: about ten. Thirty alarms, twenty real. The ten false ones come from a population fifty thousand times larger than the population producing the real ones, and that is the whole effect.

## How Fast It Falls Apart

The lecture gives one point. Holding its other two numbers fixed — perfect detection, base rate 2×10⁻⁵ — and varying only the false alarm rate:

| False alarm rate | Alarms that are real | False alarms per real one |
|---|---|---|
| 10⁻⁶ | 95.2% | 0.05 |
| **10⁻⁵** (the slide) | **66.7%** | 0.5 |
| 10⁻⁴ | 16.7% | 5 |
| 10⁻³ | 2.0% | 50 |
| 10⁻² | 0.2% | 500 |

> **Derived, same formula.** A detector with a 1% false alarm rate sounds excellent and is wrong 499 times out of 500. Each factor of ten in the false alarm rate costs roughly a factor of ten in false alarms per real one, and the detection rate is no help: it is already 1 in every row.

## Implications to IDS

> - **Design algorithms to reduce false alarm rate**
> - **Deploy IDS to appropriate point/layer with sufficiently high base rate**

> **The second one, derived.** The base rate is not a fixed fact about the world; it depends on *where the detector is looking*. Traffic that has already passed a [[Firewalls|firewall]] has had most of the noise removed. A honeypot offers no legitimate service, so nearly everything reaching it is hostile and the base rate is close to 1 — the argument [[Worms]] records for honeypot-based detection. And requiring several alarms to line up, as [[Botnets|BotHunter's dialog correlation]] does, replaces a common event (one odd packet) with a rare and specific one (a whole infection sequence), which raises the base rate of the thing being tested.
>
> The first implication is why [[Misuse and Anomaly Detection|anomaly detection]]'s *relatively high false positive rate* is a more serious weakness than it sounds. *Relatively high* on a quantity that needs to be around 10⁻⁵ is fatal.

## The Same Arithmetic in CSCE 420

[[Bayes Rule]] works this exact calculation as a medical test, in a different course:

| | CSCE 420 | CSCE 465 |
|---|---|---|
| Rare condition | Disease, 1 in 10,000 | Intrusion, 2 in 100,000 |
| Signal | Positive test | Alarm |
| Hit rate | 0.99 | 1 |
| False positive rate | 0.01 | 10⁻⁵ |
| Chance the signal is real | **just under 1%** | **66%** |

Same formula, same denominator-by-conditioning, same lesson. The IDS does better because its false positive rate is a thousand times smaller — its base rate is in fact five times *lower* — and it still loses a third of its alarms to noise.

## Where the Example Comes From

The example appears to be the one in Stefan Axelsson's 1999 paper *The Base-Rate Fallacy and Its Implications for the Difficulty of Intrusion Detection*, which uses the same base rate. The slide does not cite it; the attribution is recorded here, not taken from the deck.

## See Also

- [[IDS Performance Metrics]]
- [[Intrusion Detection Systems]]
- [[Misuse and Anomaly Detection]]
- [[Bayes Rule]]
- [[Probability Basics]]
- [[Biometrics]]
- [[Botnets]]
- [[CSCE 465]]
- [[CSCE 420]]
