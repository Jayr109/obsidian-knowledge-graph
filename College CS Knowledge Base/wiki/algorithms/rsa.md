---
title: "RSA"
type: algorithm
tags: [csce465, security, cryptography, public-key, rsa, factoring, timing-attack]
sources: [csce465-lecture-05-public-key-cryptography]
course: CSCE 465
updated: 2026-09-26
---

RSA (Rivest, Shamir, Adleman) is **the most popular public key method**, and the only one of the three [[Public Key Cryptography|public key algorithms]] in [[CSCE 465]] that provides both encryption and digital signatures. Its trapdoor is the one-way gap between multiplying primes and factoring their product:

> **Basis: factorization of large numbers is hard.**

- **Variable key length** — 1024 bits or greater
- **Variable plaintext block size** — the plaintext block must be **smaller than the key size**; the ciphertext block is the **same size** as the key

## Generating a Key Pair

1. Find (using **Miller-Rabin**) large primes `p` and `q`
2. Let `n = p * q` — **do not disclose p and q**
3. Compute `φ(n) = (p-1)(q-1)`, where φ is **Euler's totient function**
4. Choose `e` relatively prime to `φ(n)`, i.e. `gcd(e, φ(n)) = 1`
5. **Public key = <e, n>**
6. Find `d` = the multiplicative inverse of `e` mod `φ(n)`, i.e. `e*d ≡ 1 mod φ(n)`
7. **Private key = <d, n>**

`p` and `q` are discarded-but-fatal: they are not part of either key, and anyone who recovers them recovers the private key immediately (step 3 then step 6).

## The Four Operations

```
Encryption:    c = m^e mod n      (m < n)
Decryption:    m = c^d mod n

Signing:       s = m^d mod n      (m < n)
Verification:  m = s^e mod n
```

Signing and decryption are the *same operation* — exponentiate by `d`. Encryption and verification are the same — exponentiate by `e`. The difference is entirely in which key is whose and what the result means, which is why [[Digital Signatures|signing and encrypting]] are so easy to confuse.

## Worked Example

Choose `p = 23`, `q = 11` (both prime):
- `n = p*q = 253`
- `φ(n) = (p-1)(q-1) = 220`
- Choose `e = 39` (relatively prime to 220) → **public key = <39, 253>**
- Find `e⁻¹ mod 220 = d = 79` (note `39*79 ≡ 1 mod 220`) → **private key = <79, 253>**

With plaintext `m = 80`:

| Operation | Computation | Result |
|---|---|---|
| **Encryption** | `c = 80^39 mod 253` | **37** |
| **Decryption** | `m = 37^79 mod 253` | **80** |
| **Signing** | `s = 80^79 mod 253` | **224** |
| **Verification** | `m = 224^39 mod 253` | **80** |

> **Verified during ingest.** Every value above was recomputed and matches the slide. Note the signature (224) and the ciphertext (37) are different numbers from the same message — signing and encrypting are different operations, not two names for one.

## Key Negotiation with RSA

RSA can establish a shared symmetric key ([[Public Key Cryptography|application 5]]):

1. A sends random number `R1` to B, **encrypted with B's public key**
2. B sends random number `R2` to A, **encrypted with A's public key**
3. Both decrypt with their own private keys
4. Both compute `K = H(R1 XOR R2)` and use it as the shared key

**Example** — Alice `<e=39, d=79, n=253>`; Bob `<e=23, d=47, n=589>` (589 = 19×31); `R1 = 15`, `R2 = 55`:

| Step | Computation | Result |
|---|---|---|
| Alice sends | `15^23 mod 589` | 306 |
| Bob sends | `55^39 mod 253` | 187 |
| Alice recovers R2 | `187^79 mod 253` | 55 |
| Bob recovers R1 | `306^47 mod 589` | 15 |

Then both compute `K = H(R1 XOR R2)`.

> **Verified during ingest**, including Bob's key: 19×31 = 589, φ = 540, and 23×47 ≡ 1 mod 540.
>
> **Why both random numbers, and why hash them?** Neither party alone determines the key, so a party with a broken random number generator cannot force a predictable key on the other. The hash then mixes both contributions so that any structure in either input is destroyed. Note this is *not* forward-secret — anyone who later obtains a private key can decrypt the recorded exchange and recover K, which is what [[Diffie-Hellman Key Exchange]] avoids.

## Proof of Correctness

Given public `<e, n>`, private `<d, n>`, `n = p*q`, `φ(n) = (p-1)(q-1)`, and `e*d ≡ 1 mod φ(n)`:

```
Decryption of c = m^e mod n:
  c^d mod n
= (m^e)^d mod n
= m^(ed) mod n
= m mod n            (why?)
= m                  (since m < n)
```

The lecture marks the fourth line **"(why?)"** and moves on.

> **Derived, not stated on the slide.** Since `e*d ≡ 1 mod φ(n)`, we can write `ed = 1 + kφ(n)` for some integer `k`. Then
> ```
> m^(ed) = m^(1 + kφ(n)) = m * (m^φ(n))^k
> ```
> **Euler's theorem** says `m^φ(n) ≡ 1 mod n` whenever `gcd(m, n) = 1`. So the whole bracket collapses to 1 and `m^(ed) ≡ m mod n`.
>
> (The edge case where `gcd(m, n) ≠ 1` — i.e. `m` is a multiple of `p` or `q` — still works out via the Chinese Remainder Theorem, but it is vanishingly unlikely for a random `m` and the lecture does not raise it.)
>
> The final step `m mod n = m` needs `m < n`, which is exactly the constraint stated in the operations: **the plaintext block must be smaller than the key.**

The digital signature proof is the same argument with `d` and `e` swapped.

## Is RSA Secure?

`<e, n>` is public information. **If you could factor `n` into `p*q`**, then you could compute `φ(n) = (p-1)(q-1)`, then `d = e⁻¹ mod φ(n)` — and you would know the private key.

So RSA's security *is* the hardness of factoring: **a classical problem worked on for centuries, with no known reliable, fast method.** This is [[Cipher Security Models|provable security]] in the lecture's sense — a reduction to a famous unsolved problem, not a proof.

**Key sizes:** 1024 bits is *considered* secure at present; **2048 is better.**

**Making `n` hard to factor:**
1. `p` and `q` lengths should be similar (~500 bits each for a 1024-bit key)
2. Both `(p-1)` and `(q-1)` should contain a **large prime factor**
3. `gcd(p-1, q-1)` should be **small**
4. `d` should be **larger than n^(1/4)**

Each rule blocks a specific specialized factoring attack (Pollard's p−1 targets rule 2; Wiener's attack on small `d` is rule 4). The rules are not folklore — they exist because the general problem being hard does not make every *instance* hard.

## Attacks

### Brute Force
Try all possible private keys. Defeated by a large enough key space (1024 bits or larger).

### Mathematical
1. **Factor `n`** — possible for special cases of `n`, which is what the four rules above guard against
2. **Determine `d` directly from `e`** without computing `φ(n)` — at least as difficult as factoring `n`

### Probable-Message Attack
Using the public `<e, n>`, **encrypt all possible plaintext messages** and look for a match with the observed ciphertext. This works because **RSA is deterministic**: the same message under the same public key always gives the same ciphertext, and the attacker holds the public key needed to build the dictionary. It **only works for small plaintext message sizes.**

**Solution: pad the plaintext with random text before encryption.** The lecture gives the **PKCS #1 v1** format, each field 8 bits:

```
00 | 02 | R1 R2 R3 R4 R5 R6 R7 R8 | data... | 00
```

> **Recorded as the slide draws it.** In the actual PKCS #1 v1.5 standard the `00` separator sits *between* the random padding and the data (`00 02 <random padding> 00 <data>`), not at the end. The slide's box order may be a figure artifact; treat the raw deck as authoritative for the exam and the standard as authoritative for implementation.

The deeper point: padding makes encryption **non-deterministic**, which is the same fix an [[Initialization Vector]] provides for [[Block Cipher Modes of Operation|block cipher modes]]. Determinism leaks, in every corner of cryptography.

### Timing Attacks

A [[Side-Channel Attacks|side-channel attack]] that **recovers the private key from the running time of the decryption algorithm.** The target is the repeated-squaring exponentiation used to compute `m = c^d mod n`:

```
m = 1
for i = k-1 downto 1:
    m = m*m mod n
    if d_i == 1:
        m = m*c mod n        <-- this step runs only when the key bit is 1
return m
```

**The attack proceeds bit by bit.** The attacker knows `c` and `m`, and can determine bit `i` of `d` because for some values the conditional step is **extremely slow when `d_i = 1`.** The key leaks one bit per observation, and the algorithm never had to be broken.

**Countermeasures:**

| # | Countermeasure | Disadvantage |
|---|---|---|
| 1 | Delay the result if the computation is too fast | *the lecture leaves this `?`* |
| 2 | Add a random delay | *the lecture leaves this `?`* |
| 3 | **Blinding** — multiply the ciphertext by a random number before decrypting | < 10% slowdown |

> **The two `?` marks, derived.** Padding every decryption out to a fixed worst-case time (1) costs *every* operation the slowest path's latency — you pay the maximum always, which on a busy server is a large throughput loss. Adding a random delay (2) does not remove the signal, it only adds noise: the underlying timing difference is still there, so an attacker who averages over enough samples recovers it anyway. Only blinding removes the *correlation* between the secret and the observable, which is why it is the one with a real number attached to its cost.

### RSA's Blinding Algorithm

To confound timing attacks during decryption:

1. Generate a random `r` in `0..n-1` with `gcd(r, n) = 1`
2. Compute `c' = c * r^e mod n`
3. Compute `m' = (c')^d mod n` ← *this is where the timing attack would occur*
4. Compute `m = m' * r⁻¹ mod n`

**The attacker will not know what the bits of `c'` are**, so the timing observations cannot be tied to any known input. **Performance penalty: less than 10% slowdown in decryption speed.**

Why it works algebraically: `(c * r^e)^d = c^d * r^(ed) = c^d * r`, so multiplying by `r⁻¹` at the end recovers `m` exactly. The secret exponent operates on a value the attacker cannot predict.

## See Also

- [[Public Key Cryptography]]
- [[Diffie-Hellman Key Exchange]]
- [[Digital Signatures]]
- [[Public Key Infrastructure]]
- [[Side-Channel Attacks]]
- [[Cipher Security Models]]
- [[CSCE 465]]
