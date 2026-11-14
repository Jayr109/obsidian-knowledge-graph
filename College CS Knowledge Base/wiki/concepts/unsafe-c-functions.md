---
title: "Unsafe C Functions"
type: concept
tags: [csce465, security, software-security, c, strcpy, strncpy, range-checking]
sources: [csce465-lecture-09-software-security-buffer-overflow]
course: CSCE 465
updated: 2026-10-25
---

The C standard library ships functions that write into a caller-supplied buffer without knowing how big it is. [[CSCE 465]] treats this as the root cause of the whole [[Buffer Overflow|buffer overflow]] unit, and spends an unusual amount of the deck on a case study where the *published fix* was also wrong.

## The Problem: No Range Checking

> `strcpy` does not check input size. `strcpy(buf, str)` simply copies memory contents into `buf` starting from `*str` **until `\0` is encountered**, ignoring the size of the area allocated to `buf`.

The lecture's list of unsafe C library functions:

| Function | Signature |
|---|---|
| `strcpy` | `strcpy(char *dest, const char *src)` |
| `strcat` | `strcat(char *dest, const char *src)` |
| `gets` | `gets(char *s)` |
| `scanf` | `scanf(const char *format, …)` |
| `printf` | `printf(const char *format, …)` |

The first three are unsafe for the same reason — **no destination size parameter exists**, so no check is possible even in principle. `scanf` and `printf` are unsafe for a different reason: see [[Format String Vulnerabilities]].

## Does Range Checking Help?

The obvious replacement:

> `strncpy(char *dest, const char *src, size_t n)` — if `strncpy` is used instead of `strcpy`, **no more than `n` characters** will be copied from `*src` to `*dest`.
>
> **The programmer has to supply the right value of `n`.**

That last line is the whole lecture. The case study is Apache.

### The Apache `htpasswd` Overflow

The original code (Apache 1.3) copies a username into a buffer, then appends `":"` and a hashed password:

```c
strcpy(record, user);
strcat(record, ":");
strcat(record, cpw);
```

Three unbounded writes into one fixed buffer. The **published fix**:

```c
strncpy(record, user, MAX_STRING_LEN-1);
strcat(record, ":");
strncat(record, cpw, MAX_STRING_LEN-1);
```

> **Do you see the problem?**

The lecture's own diagram answers it. `record` holds `MAX_STRING_LEN` bytes total, but:

```
|<--------------- MAX_STRING_LEN bytes allocated for record --------------->|
[ contents of *user .......... ][:][ contents of *cpw ..........            ]
  up to MAX_STRING_LEN-1 chars       up to MAX_STRING_LEN-1 chars AGAIN
```

Each call is individually bounded, and the bound each one uses is **the size of the whole buffer** rather than the space remaining in it. Write `MAX_STRING_LEN-1` characters of username, add a colon, then append up to `MAX_STRING_LEN-1` more characters of password — the buffer can receive nearly **twice** its capacity.

> **The general lesson, derived.** `strncpy` moves the bounds check from the library to the programmer, and the programmer now has to track a quantity the library never gave them: **how much room is left**. That is a running total across calls, and the Apache fix failed because each call was audited in isolation and each one looked correct. A per-call bound is not a per-buffer bound. This is [[Security Design Principles|economy of mechanism]] cutting the other way — the "safe" function is safe only inside a discipline the type system does not enforce.

The lecture adds the practical consequence:

> **`strlcpy` can count and return the length of the entire source string while `strncpy` cannot.**

Which is why the recommendation below names `strlcpy` rather than `strncpy`.

## Writing Correct Code

The lecture's first and most fundamental defense family:

- **Use safe programming languages, e.g. Java** — *what about legacy C code?*
- Use **compilers that warn** about linking to unsafe functions, e.g. `gcc`
- **Static analysis** of source code to find overflows
- **Black-box testing** with long strings
- Use safer versions of functions — **`gets` and `strcpy` should be replaced with `getline` and `strlcpy`**

### Bugs to Detect in Source Code Analysis

The lecture's list of what a static analyser should look for — broader than overflows, and a good checklist in its own right:

| | |
|---|---|
| Crash causing defects | Uninitialized variables |
| Null pointer dereference | Invalid use of negative values |
| Use after free | Passing large parameters by value |
| Double free | Underallocations of dynamic data |
| Array indexing errors | Memory leaks |
| Mismatched array new/delete | File handle leaks |
| Potential stack overrun | Network resource leaks |
| Potential heap overrun | Unused values |
| Return pointers to local variables | Unhandled return codes |
| Logically inconsistent code | Use of invalid iterators |

Note that only four of the twenty are overflows. The others are the memory- and resource-lifetime bugs that *become* exploitable primitives once an attacker starts looking — use-after-free and double-free in particular are the modern successors to stack smashing.

## See Also

- [[Buffer Overflow]]
- [[Stack Smashing]]
- [[Format String Vulnerabilities]]
- [[Heap and Pointer Overflows]]
- [[Buffer Overflow Defenses]]
- [[Security Design Principles]]
- [[GDB]]
- [[CSCE 465]]
