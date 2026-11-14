---
title: "Format String Vulnerabilities"
type: concept
tags: [csce465, security, software-security, format-string, printf, exploitation]
sources: [csce465-lecture-09-software-security-buffer-overflow]
course: CSCE 465
updated: 2026-10-25
---

A **format string vulnerability** arises when attacker-controlled data is passed to `printf` as the *format* argument rather than as a value to be printed. [[CSCE 465]] files it as a **third-generation** [[Buffer Overflow|buffer overflow]] technique, and it is the odd one in the family: nothing overflows. The attacker writes to memory using a feature of `printf` that works exactly as documented.

## Proper vs. Sloppy Use

**Proper use of a `printf` format string:**

```c
int foo = 1234;
printf("foo = %d in decimal, %X in hex", foo, foo);
```

prints `foo = 1234 in decimal, 4D2 in hex`.

**Sloppy use:**

```c
char buf[13] = "Hello, world!";
printf(buf);              // should've used printf("%s", buf);
```

> If the buffer contains format symbols starting with `%`, the location pointed to by `printf`'s **internal stack pointer** will be interpreted as an argument of `printf`. This can be exploited to **move `printf`'s internal stack pointer**.

> **Why this works, derived.** `printf` is variadic: it has no way to know how many arguments it was actually given. It trusts the **format string** to tell it, and walks the stack picking up one argument per conversion specifier. Hand it a format string with more specifiers than there are arguments and it keeps walking, reading whatever happens to be further up the stack. The attacker who controls the format string therefore controls *how far into the caller's frame `printf` reads* — a stack-disclosure primitive obtained with no overflow at all. The declared `buf[13]` holding a 13-character string is itself a second bug worth noticing: there is no room for the terminating `\0`.

## Reading Is Bad; `%n` Is Worse

The specifier that turns disclosure into corruption:

> **`%n`** tells `printf` to **write the number of characters that have been printed**.

```c
printf("Overflow this!%n", &myVar);
```

- The argument of `printf` is interpreted as a **destination address**
- This writes **14** into `myVar` — `"Overflow this!"` has 14 characters

Now remove the argument:

```c
char buf[16] = "Overflow this!%n";
printf(buf);
```

> The stack location pointed to by `printf`'s internal stack pointer will be interpreted as the **address into which the number of characters will be written**.

So the attacker gets an **arbitrary memory write**: the *address* comes from stack contents they can shift, and the *value* is the character count, which they control by padding the format string. That is enough to overwrite a return address or a function pointer — the same targets as every other attack in this unit, reached by a completely different route.

## Why It Belongs in This Unit

Stack smashing needs a missing bounds check. This needs only a programmer who wrote `printf(buf)` instead of `printf("%s", buf)` — a change that is invisible in testing, because both print the same thing for every input that contains no `%`.

The defense is correspondingly simple and is the first item on [[Buffer Overflow Defenses|the defense list]]: **never pass user data as a format string**, and compile with warnings that flag it. `printf` and `scanf` both appear on the lecture's list of [[Unsafe C Functions|unsafe C library functions]] for exactly this reason — unlike `strcpy`, they are unsafe not because they skip a length check but because their contract lets the caller's data reprogram them.

## See Also

- [[Buffer Overflow]]
- [[Stack Smashing]]
- [[Heap and Pointer Overflows]]
- [[Unsafe C Functions]]
- [[Buffer Overflow Defenses]]
- [[Security Design Principles]]
- [[CSCE 465]]
