---
title: "Hash Function Applications"
type: concept
tags: [csce465, security, cryptography, hash, commitment, authentication]
sources: [csce465-lecture-04-hash-functions, csce465-lecture-06a-user-authentication]
course: CSCE 465
updated: 2026-10-08
---

[[CSCE 465]] gives six applications of [[Hash Functions|hashing]], and the set is more interesting than it looks: only the first uses a hash the obvious way. The rest get their power from **mixing a secret key or a random challenge into the input**, which turns a keyless integrity primitive into authentication, into a commitment, and even into encryption. The lecture attaches a question to nearly every one, and the questions are the content.

## 1. File Authentication

Detect whether a file has been changed after it was stored.

```
Compute H(F).  Store H(F) separately from F.
Later: compute H(F') and compare against the stored H(F).
```

Example tool: **Tripwire**.

The lecture asks: *why not just store a duplicate copy of F?*

> **Derived.** Three reasons. **Space** — a digest is 128 bits regardless of whether `F` is a kilobyte or a terabyte, so you can keep digests for an entire filesystem in the space one file would take. **Comparison cost** — comparing two digests is constant-time, versus reading both copies end to end. And most importantly, **the thing you must protect is smaller**: "store H(F) separately from F" is feasible for a small digest (burn it to read-only media, print it, keep it offline) in a way that mirroring every file to protected storage is not. The integrity guarantee rests on the digest being tamper-proof, and small secrets are cheap to make tamper-proof.

## 2. User Authentication

Alice authenticates to Bob; they already share secret key `K`.

```
Alice                                   Bob
        ---- "I'm Alice" ---->
                                        picks random number R
        <-------- R ----------
computes Y = H(R|K)
        -------- Y ---------->          verifies Y = H(R|K)
```

The lecture asks: *why not just send K in plaintext? Or H(K) — what is the purpose of R?*

> **Derived.** Sending `K` in plaintext hands the shared secret to any eavesdropper, who can then impersonate Alice forever. Sending `H(K)` is no better: `H(K)` is a *fixed value*, so an eavesdropper who records it once can **replay** it and be accepted as Alice — the digest has become the password.
>
> `R` is a **nonce** and it defeats replay. Bob chooses a fresh random `R` each time, so `Y = H(R|K)` is different every session and a recorded `Y` is worthless for the next one. Bob can verify it because he knows both `R` (he picked it) and `K`. This is a **challenge-response** protocol, and it proves Alice knows `K` **without transmitting `K`**. [[User Authentication]] names this as the general crypto-based approach, and [[S/Key Protocol]] builds a one-time-password scheme from the same one-way function — the same goal RSA achieves in [[Public Key Cryptography|user authentication]], here with a shared secret instead of a key pair.

## 3. Commitment Protocols

A and B play "odd or even" over a network: A picks `X`, B picks `Y`, they exchange *simultaneously*, A wins if `X+Y` is odd. The problem: whoever sees the other's number first can cheat trivially. *How to prevent this?*

**Proposal: A must commit to X before B will send Y.**

```
A                                       B
picks X, computes Z = H(X)
        -------- Z = H(X) ---->
                                        picks Y
        <-------- Y ----------
        -------- X ---------->          verifies H(X) = Z
```

The lecture asks four questions about this.

> **Why is sending H(X) better than sending X?** Because of the **one-way property** — `Z` tells B nothing about `X`, so B must choose `Y` blind. Sending `X` outright would defeat the whole point.
>
> **Why is H(X) good enough to prevent A from cheating?** Because of **[[Hash Functions|weak collision resistance]]**. Once A has sent `Z`, A is bound: to change her mind after seeing `Y` she would need some `X' ≠ X` with `H(X') = H(X)`, and that is infeasible. The commitment is *binding* on A and *hiding* from B — the two properties any commitment scheme needs, supplied here by collision resistance and one-wayness respectively.
>
> **Why need B not send H(Y)?** Because by the time B picks `Y`, A is already committed. B gains nothing from seeing `Z` (it is opaque), and A gains nothing from seeing `Y` (she cannot change `X`). The asymmetry in the protocol matches the asymmetry in the game: only the second mover needs to be constrained, and A was constrained first.
>
> **The two failure cases.** If **the set of possible X is small**, B simply hashes every candidate and reads `X` off the table — a dictionary attack on the commitment. The standard fix is to commit to `H(X | r)` for a large random `r` revealed alongside `X`. If **B can predict the next X A will pick**, the commitment is no commitment at all; B chooses `Y` to win. Both failures are about **entropy in X**, not about the hash — which is the same lesson as [[Initialization Vector|IV]] unpredictability and [[RSA|RSA's]] need for random padding.

## 4. Message Encryption

A and B share secret `K` but do not want to encrypt the message with `K` directly. A sends encrypted random `R1`, B sends encrypted `R2`, and then the pair is used to drive a keystream — but with **concatenate-then-hash (C+H) replacing the encryption function**:

```
R1 | R2  plays the role of the IV in OFB mode
C+H      replaces E at each stage
keystream XOR M1..M4  ->  C1..C4
```

This is structurally the [[Block Cipher Modes of Operation|OFB mode]] diagram with the block cipher swapped out for a hash. The lecture asks: *as good as encryption?*

> **Derived: for confidentiality, broadly yes — with the same caveats, and one extra.** The construction is a [[Stream Ciphers|stream cipher]] whose PRNG happens to be a hash, so it inherits every keystream property: the pad must never repeat (hence fresh `R1|R2` each time), and it provides **no integrity** whatsoever, since XOR lets an attacker flip chosen plaintext bits. Its security rests on the hash being indistinguishable from random when iterated, which is a *different* assumption from collision resistance and not one the hash was designed for. The honest answer is that it is as good as the hash's pseudorandomness, and a block cipher is the better-studied choice for the job.

## 5. Message Authentication

A authenticates — but does not encrypt — message `M`; A and B share `K`.

```
A                                       B
picks random R
computes Y = H(M|K|R)
        ---- M, R, Y ------->           verifies Y = H(M|K|R)
```

The lecture asks: *why is R needed? Why is K needed?*

> **Derived.** `K` provides **authentication**: without it, anyone could compute `H(M|R)` and forge a message, since the hash has no secret and is public. The key is what makes the digest unforgeable rather than merely a checksum.
>
> `R` provides **freshness**. Without it, `Y = H(M|K)` is a fixed value for a given message, so an attacker who records `(M, Y)` can replay that exact message later and have it accepted — a replay attack on a legitimate message. `R` makes each authentication single-use.
>
> This is a **[[Message Authentication Code|MAC]]**, built from a hash instead of from CBC. Note the construction is `H(M|K|R)` — key *inside* the hash, which is the naive approach. Putting the key next to the message inside a single hash call is exactly what the extension attack exploits, and is why [[HMAC]] exists.

## 6. Digital Signatures

```
Generating:  Message m -> Hash -> H(m) -> Sign with Bob's PRIVATE key -> signature
Verifying:   Message m -> Hash -> H(m) -> Verify with Bob's PUBLIC key -> Valid / Not Valid
```

**Only one party (Bob) knows the private key**, which is what makes the signature attributable. The hash is what makes it *practical*: [[RSA]] requires `m < n`, so a long message cannot be signed directly, and a 128-bit digest can. See [[Digital Signatures]] for the full treatment.

## The Pattern Across All Six

Only file authentication uses a bare hash. Every other application adds one of two ingredients:

| Ingredient | Supplies | Appears in |
|---|---|---|
| **A secret key in the input** | Authentication — nobody without `K` can produce the value | 2, 4, 5 |
| **A fresh random value** | Freshness — defeats replay, and forces blind choices | 2, 3, 5 |

A hash alone proves a message *has not changed*. A hash plus a key proves *who* produced it. A hash plus a nonce proves it is *not a recording*. Most real protocols need all three.

## See Also

- [[Hash Functions]]
- [[HMAC]]
- [[Message Authentication Code]]
- [[Digital Signatures]]
- [[Block Cipher Modes of Operation]]
- [[Stream Ciphers]]
- [[Birthday Attack]]
- [[User Authentication]]
- [[S/Key Protocol]]
- [[CSCE 465]]
