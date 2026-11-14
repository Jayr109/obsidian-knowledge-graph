---
title: "Password Authentication"
type: concept
tags: [csce465, security, authentication, passwords, dictionary-attack, salt]
sources: [csce465-lecture-06a-user-authentication]
course: CSCE 465
updated: 2026-11-04
---

The user demonstrates knowledge of a secret value — **the most common method of [[User Authentication|user authentication]]**, and per [[CSCE 465]]'s own summary, *by far the most widely used form of authentication, despite numerous problems.* This page is mostly about the problems.

The design tension in one line:

> A password should be **easy to remember but hard to guess** — that's difficult to achieve!

Three questions follow from it, and the lecture answers each: what makes a good password, **where is the password stored and in what form**, and **how is knowledge of the password verified**.

## Storage: Never the Password Itself

> Storing unencrypted passwords in a file is high risk — compromising the file system compromises **all** the stored passwords.

The better idea: use the password to compute a **one-way function** (a [[Hash Functions|hash]], an encryption) and store only the output. Verification then becomes:

1. Compute the one-way function of the submitted password
2. Compare with the stored value

The verifier never needs the password, only the ability to recompute `F(password)`. This is the [[Hash Functions|one-way property]] doing exactly the job it was defined for — and note that it means the system **cannot tell you your password**, only check it.

## Why Brute Force Is Not the Threat

The lecture does the arithmetic and then undercuts it:

> Passwords up to 9 characters long → **10¹⁸ possible passwords**; **320,000 years** to try them all at 10 million per second.
>
> *Unfortunately, not all passwords are equally likely to be used.*

That second line is the whole lecture. The key space is enormous and almost entirely unoccupied — which is the same lesson [[Classical Ciphers|mono-alphabetic ciphers]] taught, that **a large key space is necessary but not sufficient**. Here the structure the attacker exploits is not mathematical but human.

**The study the lecture cites** — a sample of over 3,000 passwords:

- **500** were easily guessed versions of dictionary words or first/last names
- **86% of passwords were easily guessed**

Length distribution in that sample:

| Length (characters) | 1 | 2 | 3 | 4 | 5 | 6 (lower case only) |
|---|---|---|---|---|---|---|
| Number of passwords | 15 | 72 | 464 | 477 | 706 | 605 |

Common choices: **pet names, common names, common words, dates**, and variations of those (backwards, a few digits appended).

## The Three Dictionary Attacks

The lecture separates these carefully, and the distinction is what makes salt analyzable.

### Attack 1 — Online

Build a dictionary of common words, names, and simple transformations; **use them to guess the password** against the live system.

```
Dictionary: Eagle, Wine, Rose, ...   -->   try each against the login prompt
```

Slow, and visible — rate limiting and lockouts are the natural defense.

### Attack 2 — Offline

> Usually `F` is public and so is the password file. In Unix, `F` is `crypt` and the password file is `/etc/passwd`.

Compute `F(word)` for each dictionary word and look for a match in the password file.

```
Dictionary --[F]--> F(Eagle) = XkPT   ==   XkPT in the password file   -->  found
```

No interaction with the live system at all, so no rate limit applies. This is why *the password file being publicly readable* is a design decision with consequences.

### Attack 3 — Offline, Precomputed

**Pre-compute `F(dictionary)` once**, then a simple lookup gives the password.

```
Dictionary --[F]--> precomputed table   -->   look up each password-file entry
```

The cost of `F` is paid once and amortized across every password file the attacker will ever see. This is the rainbow-table idea.

## Salt

> Salt is an **n-bit number between 0 and 2ⁿ**, derived from, for example, the **system clock and the process identifier**.

**Storage:** `F(Password + Salt)` is stored, and the record becomes `Username, Salt, F(Password + Salt)` — **the salt is stored in the clear**, next to the hash.

**Verification:** fetch the salt by username, compute `F(submitted password + salt)`, compare.

### Does Salt Help?

The lecture asks this once per attack and leaves the answers as diagrams.

> **Derived, attack by attack:**
>
> **Attack 1 (online): no.** Salt changes nothing. The attacker submits candidate passwords to the system, and the system applies the correct salt itself. Online guessing is unaffected.
>
> **Attack 2 (offline, per-file): no real help.** The attacker must now compute `F(word + salt)` using each entry's own salt rather than `F(word)` once, so the work multiplies by the number of distinct salts in the file — but attacking **one** chosen account costs exactly the same as before. Salt does not protect an individual target.
>
> **Attack 3 (precomputation): this is what salt destroys.** A precomputed table is built for one function; with an n-bit salt there are 2ⁿ functions, so the table would have to be 2ⁿ times larger to cover them. The one-time cost is no longer amortizable, and the attack collapses back to attack 2.
>
> **So salt's real purpose is narrow and specific: it defeats precomputation and forces per-password work.** The lecture's own phrasing is honest about the scale — it makes the dictionary attack *"a bit more difficult"*, not impossible. It is not a substitute for a strong password, and it does nothing about online guessing.

A second benefit the lecture notes separately: **users with identical passwords but different salt values will have different hash values**, so the password file no longer reveals which accounts share a password.

### Unix

> Keyed password hashes are stored with a **two-character (16-bit) salt** prepended; the **password file is publicly readable**.

16 bits is 65,536 salts — enough to make a single precomputed table useless in the era it was designed for, and far too few now.

## Guidelines for Users

1. Initial passwords are system-generated and must be changed on first login
2. Users must change passwords periodically
3. Passwords vulnerable to a dictionary attack are rejected
4. Users should not use the same password on multiple sites
5. *etc. etc.*

Rule 3 is the interesting one — it means the system runs the attack against its own users at enrollment time, which is the only way to enforce "hard to guess" rather than merely "long."

## Other Attacks

The lecture splits these, and the split is the same **technical vs human** division that runs through [[Security Assurance|Lecture 2's human issues]]:

**Technical**
- Eavesdropping on traffic containing unencrypted passwords — **especially keystroke logging**
- **Trojan horse** password-entry programs (a fake login prompt)
- **Man-in-the-middle** network attack

**"Social"**
- Careless password handling or sharing
- **Phishing**

None of these are defeated by a stronger password, a better hash, or more salt. They attack the *path* the password travels rather than the password itself — which is [[Cryptography|"cryptography is rarely the weakest link"]] applied to authentication, and the reason the next sections of the lecture move to [[S/Key Protocol|one-time passwords]] and [[Authentication Tokens|hardware]].

## See Also

- [[User Authentication]]
- [[S/Key Protocol]]
- [[Biometrics]]
- [[Authentication Tokens]]
- [[Hash Functions]]
- [[Classical Ciphers]]
- [[Security Threat Landscape]]
- [[CSCE 465]]
- [[Notable Worms]]
