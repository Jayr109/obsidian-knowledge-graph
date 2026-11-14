---
title: "Block Cipher Modes of Operation"
type: concept
tags: [csce465, security, cryptography, block-cipher, ecb, cbc, ofb, cfb, ctr]
sources: [csce465-lecture-03b-secret-key-cryptography-ii-modes-of-operation]
course: CSCE 465
updated: 2026-09-22
---

A [[Block Ciphers|block cipher]] encrypts one fixed-size block. Real messages are longer than one block, so something has to say **how the blocks are chained together** — that is a *mode of operation*, and the choice matters more than most students expect. [[CSCE 465]] covers five: **ECB, CBC, OFB, CFB, CTR**. The lecture's closing verdict is blunt: **ECB mode is not secure; CBC is the most commonly used mode of operation.**

The cipher is the same in every mode. Only the wiring changes, and the wiring is what leaks.

## The Four Questions

The lecture evaluates every mode against the same four criteria. Learning these as a checklist is worth more than memorizing any single mode's diagram:

1. **Information leakage** — does the mode reveal information about the plaintext blocks?
2. **Ciphertext manipulation** — can an attacker modify or *rearrange* ciphertext blocks to produce a predictable, desired change in the decrypted plaintext? The lecture attaches an assumption that makes this concrete: **assume the structure of the plaintext is known** — block 1 is employee #1's salary, block 2 is employee #2's salary, and so on.
3. **Parallel/sequential** — can blocks be encrypted (or decrypted) in parallel?
4. **Error propagation** — if one block has an error, does the damage spread beyond one block?

Criterion 2's assumption is the one to internalize. Confidentiality is not the only thing a mode can fail at; a mode can hide *what* the salaries are and still let an attacker swap his salary with his boss's.

## ECB — Electronic Code Book

The easiest mode: **each block is independently encrypted** with the same key.

```
M1     M2     M3     M4
 |      |      |      |
[E]    [E]    [E]    [E]     <- same key, no connection between blocks
 |      |      |      |
C1     C2     C3     C4
```

Decryption is the mirror image, each block independent.

| Question | ECB |
|---|---|
| Information leakage | **Yes** — identical plaintext blocks produce identical ciphertext blocks |
| Ciphertext manipulation | **Yes** — blocks can be reordered, duplicated, or deleted freely |
| Parallel processing | **Yes**, both directions |
| Error propagation | **No** — an error stays in its own block |

The lecture poses these four as questions and answers them with a picture rather than words: a decryption diagram fed `C1 C4 C3 C2` that produces `M1 M4 M3 M2`.

> **Derived from that diagram.** The attacker never breaks the cipher and never learns a key. He permutes the ciphertext blocks and the plaintext permutes with them. Under the lecture's salary assumption, swapping two ciphertext blocks swaps two employees' salaries. Independence is the whole problem: with no chaining, position carries no meaning, so nothing detects that the blocks moved.
>
> The leakage is the same defect from the other side. Because the mapping from block to block is fixed, ECB is a [[Classical Ciphers|mono-alphabetic cipher]] whose "alphabet" is 2⁶⁴ blocks wide. It preserves structure exactly as frequency analysis needs — which is why an ECB-encrypted bitmap still shows the picture.

**ECB's two good properties — full parallelism and no error propagation — are the direct consequence of the independence that makes it insecure.** That trade is the theme of the whole lecture.

## CBC — Cipher Block Chaining

**Each ciphertext block depends on all preceding plaintext blocks.** Before encrypting, each plaintext block is XORed with the previous ciphertext block; the first block is XORed with an [[Initialization Vector]].

```
   IV     C1     C2     C3
    |      |      |      |
M1-XOR  M2-XOR M3-XOR M4-XOR
    |      |      |      |
   [E]    [E]    [E]    [E]
    |      |      |      |
   C1     C2     C3     C4
```

Decryption reverses it: `M_i = D(C_i) XOR C_{i-1}`. The lecture asks *how many ciphertext blocks does each plaintext block depend on?*

> **Derived.** On decryption, exactly **two** — `C_i` and `C_{i-1}`. That asymmetry is the source of CBC's error behavior: encryption chains forward forever, but decryption only reaches back one block.

| Question | CBC |
|---|---|
| Information leakage | **No** — identical plaintext blocks produce different ciphertext blocks |
| Ciphertext manipulation | The lecture leaves this `???` — see below |
| Parallel processing | **No** for encryption, **yes** for decryption |
| Error propagation | **Yes** for encryption, **a little** for decryption |

> **The `???` answered.** Manipulation is *constrained but not prevented*. Flipping a bit in `C_{i-1}` flips the corresponding bit in `M_i` (because `M_i = D(C_i) XOR C_{i-1}`) while turning `M_{i-1}` into unpredictable garbage. So an attacker can make a **targeted, predictable** change to one block at the cost of destroying the one before it. If the destroyed block is ignored or unchecked, the attack lands. CBC gives confidentiality; it does **not** give integrity — which is why the lecture immediately turns to [[Message Authentication Code|MACs]].
>
> **Error propagation, both directions.** On *encryption*, one bad plaintext bit corrupts that ciphertext block and every block after it, since the chain carries it forward. On *decryption*, one bad ciphertext bit garbles its own block entirely and flips the corresponding bit in the next block — then the chain recovers. "A little" means exactly two blocks. CBC is **self-synchronizing**.

CBC's sequential encryption is its main cost: you cannot start block *i* until block *i−1* is done.

## OFB, CFB, and CTR — Turning a Block Cipher Into a Keystream

The remaining three modes share a structure the lecture flags twice with the note **"No block decryption required!"** — and it is worth naming, because it makes all three easier to remember at once.

> **Synthesis, not the lecture's own grouping.** OFB, CFB, and CTR all use the block cipher to *generate a pseudo-random pad*, then XOR the pad with the plaintext. The plaintext never enters the cipher. Consequently: decryption runs the cipher **forward** (E, never D), the block cipher's decryption circuit is never needed, and all three behave like [[Stream Ciphers|stream ciphers]] built out of a block cipher. The OFB diagram labels its keystream *"one-time pad"* and its generator *"Pseudo-Random Number Generator"* outright.

### OFB — Output Feedback

The cipher is iterated on its own output — `E(IV)`, `E(E(IV))`, … — producing a keystream independent of the message.

| Question | OFB |
|---|---|
| Information leakage | **No** |
| Ciphertext manipulation | `???` — see below |
| Parallel processing | **No** for generating the pad, **yes** for XORing it |
| Error propagation | `???` — see below |

**Advantages:** the pseudo-random stream can be **pre-computed** before the message arrives, and XOR is very cheap. It also allows bit-wise rather than block-wise processing, so encryption can happen in real time on a stream.

**The warning the lecture states outright:** if you know one plaintext/ciphertext pair you can derive the pad that was used — so **a pad must never be reused**, which means **the IV must be different every time.** This is the [[One-Time Pad|one-time pad's]] key-reuse failure inherited wholesale.

The lecture then asks: *if a bad guy knows the plaintext and ciphertext, can he send arbitrary (valid) messages?*

> **Derived: yes.** Knowing `M` and `C` gives `pad = M XOR C`. With the pad in hand the attacker encrypts *any* message of that length — `C' = M' XOR pad` — and it decrypts cleanly. This also answers the manipulation `???` for all three keystream modes: **bit flips in the ciphertext flip exactly the corresponding plaintext bits, with no other damage.** That is strictly worse than CBC for integrity, because there is no collateral garbage to give the tampering away.
>
> **Error propagation `???`: none.** A corrupted ciphertext bit corrupts exactly one plaintext bit. The keystream does not depend on the ciphertext, so nothing carries forward.

### CFB — Cipher Feedback

Like OFB, but the *ciphertext* is fed back into the cipher, so **ciphertext block `C_j` depends on all preceding plaintext blocks**.

| Question | CFB |
|---|---|
| Information leakage | **No** |
| Ciphertext manipulation | `???` — targeted bit flips, as above, plus garbage in the following block |
| Parallel processing | **No** for encryption, **yes** for decryption |
| Error propagation | `???` — self-limiting; see below |

**General k-bit CFB** processes `k` bits at a time rather than a full block.

- **Advantage over CBC:** with `k = 8`, an error in one byte of ciphertext affects only **8 more bytes beyond it** when the IV is 64 bits. Damage is bounded and the stream resynchronizes.
- **Disadvantage versus OFB:** the keystream depends on the ciphertext, so it **cannot be computed in advance**.

### CTR — Counter Mode

The cipher encrypts a counter — `E(IV)`, `E(IV++)`, `E(IV++)` — and the results form the keystream.

| Question | CTR |
|---|---|
| Information leakage | **No** |
| Ciphertext manipulation | `???` — targeted bit flips, no collateral damage |
| Parallel processing | **Yes, both** generating the pad and XORing |
| Error propagation | `???` — none; one bit affects one bit |

**CTR allows decryption of the ciphertext at any location** — *ideal for random access to ciphertext.* Because block *i*'s pad is `E(IV + i)` and depends on nothing else, you can decrypt block 5,000 of a disk image without touching the first 4,999. That property plus full parallelism is why CTR dominates modern high-throughput use, even though this lecture's summary still names CBC as most common.

## Comparison

| | Leaks? | Manipulable? | Parallel (enc) | Parallel (dec) | Error propagation (dec) | Pad precomputable |
|---|---|---|---|---|---|---|
| **ECB** | **Yes** | **Yes — reorder** | Yes | Yes | 1 block | n/a |
| **CBC** | No | Targeted + collateral | No | Yes | 2 blocks | n/a |
| **OFB** | No | Targeted only | No (pad) | No (pad) | 1 bit | **Yes** |
| **CFB** | No | Targeted + collateral | No | Yes | bounded (k-dependent) | No |
| **CTR** | No | Targeted only | **Yes** | **Yes** | 1 bit | **Yes** |

Read the table as one trade repeated: **the more independent the blocks, the more parallelism and the less error propagation — and the more an attacker can rearrange things.** ECB is the extreme case of independence and is unusable; CBC buys integrity-adjacent structure by giving up parallel encryption; the keystream modes get parallelism back by moving the dependency into a counter or feedback register instead of the data.

**None of the five provides integrity.** Every one of them permits some targeted modification. That is the gap [[Message Authentication Code|MACs]] exist to close.

## See Also

- [[Initialization Vector]]
- [[Message Authentication Code]]
- [[Stream Ciphers]]
- [[Block Ciphers]]
- [[Secret Key Cryptography]]
- [[One-Time Pad]]
- [[AES]]
- [[CSCE 465]]
