---
title: "Diffie-Hellman Key Exchange"
type: algorithm
tags: [csce465, security, cryptography, public-key, diffie-hellman, discrete-log, mitm]
sources: [csce465-lecture-05-public-key-cryptography, csce465-lecture-06a-user-authentication]
course: CSCE 465
updated: 2026-10-08
---

Diffie-Hellman negotiates a **shared secret key using only public communication** — two parties who have never met, talking entirely in the clear, end up holding the same secret. [[CSCE 465]] introduces it right after [[RSA]], and the contrast matters: DH is **not** an encryption algorithm and it **does not provide authentication of the communicating parties.** It solves exactly one problem, and its most instructive property is what happens when you forget that.

**Public parameters:**
- `p` — a large prime (about 512 bits)
- `g` — a **primitive root** of `p`, with `g < p`
- Both `p` and `g` are **publicly known**

## The Protocol

| Alice | Bob |
|---|---|
| Publishes or sends `g` and `p` | Reads `g` and `p` |
| Picks random `S_A`, keeps it private | Picks random `S_B`, keeps it private |
| Computes public key `T_A = g^S_A mod p` | Computes public key `T_B = g^S_B mod p` |
| Sends `T_A`, reads `T_B` | Sends `T_B`, reads `T_A` |
| Computes `T_B^S_A mod p` | Computes `T_A^S_B mod p` |

Both sides now hold the same value:

```
T_B^S_A = (g^S_B)^S_A = g^(S_A·S_B) = (g^S_A)^S_B = T_A^S_B   (all mod p)
```

**The shared secret is `g^(S_A·S_B) mod p`**, and it was never transmitted. `S_A` is the **discrete logarithm** of `T_A` mod p, and likewise for `S_B` — which is the hard problem the whole scheme rests on.

## Worked Example

Let `p = 353`, `g = 3`, with random `S_A = 97` and `S_B = 233`:

| Step | Computation | Result |
|---|---|---|
| Alice computes `T_A` | `3^97 mod 353` | **40** |
| Bob computes `T_B` | `3^233 mod 353` | **248** |
| *(they exchange T_A and T_B)* | | |
| Alice computes K | `248^97 mod 353` | **160** |
| Bob computes K | `40^233 mod 353` | **160** |

> **Verified during ingest** — all four values recomputed and match.

## Why Is This Secure?

**The discrete log problem:** given `T_A = g^S_A mod p`, plus `g` and `p`, it is **computationally infeasible to compute `S_A`.** The same holds for `T_B`.

The lecture adds an honest parenthetical worth keeping:

> *as always, to the best of our knowledge; doesn't mean there isn't a method out there waiting to be found.*

That is [[Cipher Security Models|provable security]] stated plainly — confidence resting on a famous unsolved problem, not on a proof. Compare [[RSA]], which makes the same bet on factoring.

## Limitations

- **Expensive exponential operation** is required — and the lecture asks *possible timing attacks??* (Yes: modular exponentiation is the same operation that leaks in [[RSA]]'s timing attack, and it leaks here for the same reason. Blinding-style countermeasures apply.)
- **Useful for key negotiation only** — not for public key encryption
- **Not for user authentication.** The lecture's phrasing is the memorable one: *in fact, you can negotiate a key with a complete stranger!*

That last bullet is not a footnote. It is the vulnerability.

## Man-in-the-Middle Attack

Trudy impersonates Alice to Bob, **and** Bob to Alice:

```
Alice  <--- g^S"B" ---  Trudy  --- g^S"A" --->  Bob
       --- g^S_A --->          <--- g^S_B ---

Alice and Trudy share K1 = g^(S_A · S"B")
Trudy and Bob   share K2 = g^(S_B · S"A")
```

**Alice thinks K1 is the shared key; Bob thinks K2 is.** Trudy intercepts messages from Alice, **decrypts with K1, substitutes her own message, re-encrypts with K2** for Bob — and the same in reverse. Neither party sees anything wrong, because from each one's perspective the protocol completed correctly.

The lecture asks **"Solution???"** and answers on the next slide.

> The attack works because the protocol authenticates *nothing*. Alice verifies that someone knows a discrete log; she never verifies *who*. "You can negotiate a key with a complete stranger" and "you can negotiate a key with an attacker" are the same sentence. This is the [[Security Attack Taxonomy|fabrication]] attack family, and it is why raw DH is never deployed alone.

> **The same failure, elsewhere in the course.** [[S/Key Protocol|S/Key]]'s relay attack is this attack exactly: a fake server sits between Alice and the real server and gets Alice to compute the one value it cannot. Both protocols are **one-way** — the client proves itself and nothing proves the server — and both are fixed the same way.

## Authenticating D-H Messages

To know **who** you are negotiating with, and that the messages have not been modified:

> **Requires that the communicating parties already share some kind of a secret.** Then use encryption, or a **[[Message Authentication Code|MAC]]** based on that previously-shared secret, over the D-H messages.

Note the circularity, and that it is not fatal. DH cannot bootstrap authentication from nothing — but the pre-shared secret needed to *authenticate* can be long-lived, low-bandwidth, and established once (a password, a certificate, a fingerprint verified in person), while DH generates a **fresh** session key every time. You trade a permanent secret for per-session secrecy. In practice the pre-shared element is a public key vouched for by a [[Public Key Infrastructure|certificate authority]], which is why the lecture goes there next.

## "Phone Book" Mode

DH without any live communication at all:

1. Alice and Bob each choose a **semi-permanent** secret number and generate `T_A`, `T_B`
2. Both **publish** `T_A` and `T_B` — either can fetch the other's at any time
3. They can then generate a semi-permanent shared key **without communicating** — but they must be using the same `p` and `g`

**Essential requirement: reliability of the published values** — no one can substitute false values. The lecture asks *how accomplished???*

> **Derived.** This is the MITM attack relocated from the wire to the directory: an attacker who can alter the published `T_B` becomes the man in the middle permanently, with no need to intercept anything in real time. The answer is the same as the answer to MITM generally — the published values must be **signed by a trusted authority**, i.e. [[Public Key Infrastructure|certificates]]. Note the loss relative to interactive DH: a semi-permanent secret means no forward secrecy, since one compromised `S_B` exposes every conversation ever conducted with it.

## Encryption Using D-H

How to do key distribution **and** message encryption in one step. Everyone publishes their own individual `<p_i, g_i, T_i>`, where `T_i = g_i^S_i mod p_i`.

For Alice to send to Bob:
1. Alice picks a random secret `S_A`
2. Alice computes `g_B^S_A mod p_B`
3. Alice uses `K_AB = T_B^S_A mod p_B` to encrypt the message
4. Alice sends the encrypted message **along with the unencrypted `g_B^S_A mod p_B`**

For Bob to decipher:
1. Bob computes `K_AB = (g_B^S_A)^S_B mod p_B`
2. Bob decrypts with `K_AB`

**Example** — Bob publishes `<p_B, g_B, T_B> = <401, 5, 51>` and keeps `S_B = 58` secret. Alice picks `S_A = 17`:

| Step | Computation | Result |
|---|---|---|
| Alice computes `g_B^S_A mod p_B` | `5^17 mod 401` | **173** |
| Alice computes `K_AB = T_B^S_A mod p_B` | `51^17 mod 401` | **360** |
| *(Alice sends ciphertext + 173)* | | |
| Bob computes `K_AB = (g_B^S_A)^S_B mod p_B` | `173^58 mod 401` | **360** |

> **Verified during ingest**, including that Bob's published `T_B = 5^58 mod 401` does equal 51.

This is ElGamal in all but name, and it turns DH into something that *can* encrypt — contradicting the "key negotiation only" limitation in a useful way. The trick is that Alice's fresh `S_A` plays the role of a per-message ephemeral key.

## Picking g and p

- **Advisable to change `g` and `p` periodically** — the longer they are used, the more information is available to an attacker
- **Advisable not to use the same `g` and `p` for everybody**
- For *"obscure mathematical reasons"* (the lecture's phrase):
  - `(p-1)/2` should be prime
  - `g^((p-1)/2)` should be `≡ -1 mod p`

> **Noticed during ingest:** the lecture's own example (`p = 353`, `g = 3`) satisfies the second rule — `3^176 mod 353 = 352 ≡ -1` — but **not the first**: `(p-1)/2 = 176 = 2⁴ × 11`, which is not prime. Toy examples are chosen for arithmetic that fits on a slide, not for conformance to the production rules stated later. Worth knowing so the mismatch does not read as an error.
>
> The "obscure reasons" are not that obscure: a **safe prime** (one where `(p-1)/2` is also prime) leaves the multiplicative group with no small subgroups for an attacker to confine the shared secret into, which defeats small-subgroup attacks. The second condition makes `g` generate the large subgroup rather than a small one.

## See Also

- [[Public Key Cryptography]]
- [[RSA]]
- [[Public Key Infrastructure]]
- [[S/Key Protocol]]
- [[Message Authentication Code]]
- [[Security Attack Taxonomy]]
- [[Cipher Security Models]]
- [[CSCE 465]]
