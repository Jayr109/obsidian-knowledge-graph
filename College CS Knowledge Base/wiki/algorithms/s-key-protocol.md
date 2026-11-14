---
title: "S/Key Protocol"
type: algorithm
tags: [csce465, security, authentication, one-time-password, lamport-hash]
sources: [csce465-lecture-06a-user-authentication]
course: CSCE 465
updated: 2026-10-08
---

The S/Key protocol — also known as **Lamport's hash** — gives one-time passwords from a single remembered secret, using nothing but a [[Hash Functions|one-way function]]. [[CSCE 465]] presents it as the practical answer to a good idea that does not scale.

## The Problem It Solves

**Disposable passwords.** Generate a long list of passwords and use each only once: *an attacker gains little or no advantage by eavesdropping on the password protocol, or cracking one password.* That defeats most of the [[Password Authentication|attacks on passwords]] at once — eavesdropping, keylogging, and replay all become useless, because the captured password is already spent.

The disadvantages are what kill it:

- **Storage overhead**
- **Users would have to memorize lots of passwords!**

S/Key keeps the property and removes both costs, by **generating the list from one secret on demand** rather than storing it.

## Generation

1. Alice selects a password `x`
2. Alice specifies `n`, the number of passwords to generate
3. Alice's computer generates a sequence by iterating the hash:

```
x1 = H(x)
x2 = H(x1)
x3 = H(x2)
...
xn = H(x_{n-1})
```

```
x ──H──> x1 ──H──> x2 ──H──> x3 ──H──> ... ──H──> xn
```

4. Alice communicates **securely** to the server the **last** value in the sequence: `xn`

> **The key feature:** no one knowing `xi` can easily find an `x_{i-1}` such that `H(x_{i-1}) = xi` — **only Alice possesses that information.**

That is the [[Hash Functions|one-way property]], and it is doing something clever: the chain is walked **forwards** to build and **backwards** to spend. Alice can compute any `x_i` from `x`; the server, holding `x_i`, can verify `x_{i-1}` but cannot produce it.

## Authentication

Assuming the server holds `x_i`:

```
Alice                           Server
        <------- i --------     (sends the current index)
        ---- x_{i-1} ----->     verifies H(x_{i-1}) = x_i
```

On success the server **replaces `x_i` with `x_{i-1}`** and counts down. Each login consumes one link of the chain, walking backwards from `xn` toward `x`.

The lecture asks: *is a dictionary attack still possible?*

> **Derived: yes — against the master password `x`, not against the one-time values.** An eavesdropper who captures `x_{i-1}` learns nothing about `x_{i-2}` (that is the whole construction), but `x` is still a user-chosen password, and the attacker knows the chain: guess a candidate `x'`, hash it `i-1` times, and compare against the captured `x_{i-1}`. If `x` is a dictionary word the whole chain falls.
>
> So S/Key removes the value of **intercepting** a password but not the value of **guessing the original**. It is a replay defense, not a password-strength defense — the two are independent, and S/Key only addresses one.

## Limitations

**1. The value of `n` limits the number of passwords.** The chain is finite; you *need to periodically regenerate a new chain*, which means repeating the secure transfer of a fresh `xn`.

**2. It does not authenticate the server.** The lecture gives the attack:

```
1. Real server sends i to the fake server, which is masquerading as Alice
2. Fake server sends i to Alice, who responds with x_{i-1}
3. Fake server presents x_{i-1} to the real server
```

> The fake server never breaks anything. It sits between the two and **relays**, letting Alice do the one computation it cannot do. This is the [[Diffie-Hellman Key Exchange|man-in-the-middle]] attack in its purest form, and the cause is identical: **the protocol is one-way.** Alice proves herself to the server; nothing proves the server to Alice.
>
> Worse than a simple relay: the fake server can request a *lower* index than the real session needs and bank unused links of the chain for later use.

The fix is the same as for DH — mutual authentication requires the verifier to authenticate too, which needs something the client can check. See [[Public Key Infrastructure|certificates]].

## What It Illustrates

S/Key is a small construction that recombines pieces the course has already established:

| Piece | Where it came from |
|---|---|
| One-wayness makes the chain walkable in one direction only | [[Hash Functions]] |
| A fresh value per session defeats replay | [[Hash Function Applications]] challenge-response |
| One-way authentication invites a man in the middle | [[Diffie-Hellman Key Exchange]] |

And per the lecture's summary, one-time passwords are **attractive, especially if combined with hardware** — which is where [[Authentication Tokens]] comes in, since a token can hold the chain and compute the hash so the user never handles `x`.

## See Also

- [[User Authentication]]
- [[Password Authentication]]
- [[Authentication Tokens]]
- [[Hash Functions]]
- [[Hash Function Applications]]
- [[Diffie-Hellman Key Exchange]]
- [[CSCE 465]]
