---
title: "Biometrics"
type: concept
tags: [csce465, security, authentication, biometrics, multifactor, privacy]
sources: [csce465-lecture-06a-user-authentication]
course: CSCE 465
updated: 2026-10-08
---

Biometrics **relies upon physical characteristics of people to authenticate them** — the "what the user *is*" basis of [[User Authentication]]. [[CSCE 465]]'s verdict is cautious: *biometrics hold promise but are expensive, inconvenient, and compromise privacy.*

## Six Desired Qualities

1. **Uniquely identifying**
2. **Very difficult to forge or mimic**
3. **Highly accurate, does not vary**
4. **Easy to scan or collect**
5. **Fast to measure or compare**
6. **Inexpensive to implement**

The lecture asks: *which of these are concerns for passwords?*

> **Derived.** Passwords satisfy 4, 5, and 6 effortlessly — typing is easy, comparison is a hash and a string compare, and the marginal cost per user is zero. They fail 1 and 2 badly (two users can pick the same password, and a password is trivially copied once known). Quality 3 is the interesting one: a password **does not vary at all**, which is a strength for matching and a weakness for secrecy.
>
> That inverts for biometrics. They are strong on 1 and 2 and weak on 3 through 6 — a fingerprint reader must tolerate variation between scans, which is precisely why biometric matching has error *rates* where password matching has none. **Passwords are exact; biometrics are statistical.** That single difference drives everything else on this page.

## Assessment

> Convenient for users (you always have your fingerprints, never have to remember them), **but**:
>
> - potentially troubling **sacrifice of private information**
> - **no technique yet has all the desired properties**

The privacy problem is structural rather than incidental. A biometric is **not revocable** — if a fingerprint template leaks, the user cannot be issued a new fingerprint. A password compromised today is replaced in a minute; a biometric compromised today is compromised for life. And unlike a password, a biometric identifies the person across every system that uses it, so a template is a cross-system correlation key.

This is also where the [[User Authentication|identification vs. authentication]] distinction bites. A false-positive rate that is acceptable for *authentication* (one comparison against one record) becomes a flood of matches for *identification* (one comparison against a million records). The same technology can be adequate for one and useless for the other.

## Example Technologies

- Signature / penmanship / typing style
- Fingerprints
- Palm geometry
- Retina scan
- Iris scan
- Face recognition
- Voice recognition

Note the first is behavioral rather than physical — *how* you write rather than *what* you are — which makes it the only one on the list that is arguably revocable.

> **Visual gap:** the deck includes a slide captioned *"The Scorecard From One Study"* comparing these technologies, which is an image with no text layer. The comparative ratings are not recoverable from the PDF.

## Multifactor Authentication

> If one characteristic is pretty good, two or more characteristics should be better?

The lecture does the arithmetic for combining two tests, taking **true positives as AND** and **false positives as OR**:

```
TP = TP1 · TP2
FP = 1 - (1 - FP1)(1 - FP2)
```

Both formulas move in the direction you would *not* want if the goal is simply "better":

> **Worked out.** Suppose each test has TP = 0.95 and FP = 0.01. Then `TP = 0.95 × 0.95 = 0.9025` and `FP = 1 - 0.99² = 0.0199`. **Both got worse** — the system rejects legitimate users more often *and* accepts impostors more often.
>
> That is the consequence of the stated combining rule: requiring **both** to pass makes false rejection more likely, while accepting **either** false positive makes false acceptance more likely. It is the worst of both. The useful configuration is the opposite — demand that **both** tests accept for a match (AND on the false positives), giving `FP = FP1 · FP2 = 0.0001`, at the cost of `TP = 0.9025`.
>
> So the lecture's formulas are a caution, not a recommendation: **combining biometrics only helps if you combine them the right way around**, and whichever way you choose, one error rate improves and the other degrades. There is no free accuracy.

**Alternative: combine a biometric technique with passwords.** This is the configuration the lecture's summary endorses (*two factor authentication is commonly used for higher security*), and it is better than two biometrics for a reason the formulas do not capture — the two factors fail for **independent** reasons. Two fingerprint readers fooled by the same lifted print are not two factors; a fingerprint plus something the user knows are.

## See Also

- [[User Authentication]]
- [[Password Authentication]]
- [[Authentication Tokens]]
- [[CIA Triad]]
- [[CSCE 465]]
