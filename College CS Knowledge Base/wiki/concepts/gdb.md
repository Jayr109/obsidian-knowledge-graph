---
title: "GDB"
type: concept
tags: [csce465, tools, debugging, gdb, stack-inspection, lab]
sources: [csce465-recitation-gdb-basics]
course: CSCE 465
updated: 2026-10-25
---

**GDB** is the GNU project debugger, and [[CSCE 465]] teaches it in a recitation because the [[Buffer Overflow|buffer overflow]] labs are unworkable without it. Its pitch:

> - You can see **"inside" of your executed program**
> - Debugging **"low-level"** of your program

That second line is why it appears in a security course rather than a programming one. The attacks in this unit are about the **stack frame** — saved return addresses, frame pointers, buffer offsets — and GDB is how you read those directly instead of guessing.

## The Debugging Loop

1. **Start** your program, specifying anything that might affect its behavior
2. Make your program **stop** on specified conditions
3. **Examine** what has happened when your program stops
4. **Change things** in your program, then repeat 1–3

## Commands

Compiling and starting:

| Command | Effect |
|---|---|
| `gcc -g [file] -o [program]` | Compile with `-g` to **enable gdb** |
| `gdb [program]` | Start the debugger on your executable |
| `(gdb)` | The prompt you see when gdb is on |
| `run` | Run the program |

Breakpoints and stepping:

| Command | Effect |
|---|---|
| `break [file]:7` | Set a breakpoint at line 7 of the file |
| `b main` | Set a breakpoint at the beginning of the program |
| `continue` | Continue until the next breakpoint or error |
| `s` | Execute the next line of the program |
| `n` | Similar to `s`, but **does not step into functions** |
| `u 7` | Run for the next 7 lines from the current line |
| `info break` | List all the breakpoints you set up |
| `d N` | Delete breakpoint number N |
| `print var` | Print the variable `var` |
| `q` | Quit. **The settings you set won't be saved.** |

Stack inspection — the two that matter for this course:

| Command | Effect |
|---|---|
| `bt` | Print the **stack trace**. Summarizes how your program got where it is; shows the function chain. |
| `info frame` | List all the frames in **low-level information**. |

Pressing **Enter** on an empty prompt repeats the previous command.

## The Worked Example

The recitation's sample program is deliberately recursive, so the backtrace has something to show:

```c
#include <stdio.h>

void level0() {
    printf("Reached level 0\n");
}

void test(int level) {
    if (level > 0) {
        int prevLevel = level - 1;
        printf("Level %d\n", level);
        test(prevLevel);
    } else {
        level0();
    }
}

int main() {
    test(5);
    return 0;
}
```

`backtrace` at the innermost call, with `test(5)` having recursed down to `level0()`:

```
#0  level0 () at test.c:5
#1  0x00000000004005bb in test (level=0) at test.c:17
#2  0x00000000004005af in test (level=1) at test.c:14
#3  0x00000000004005af in test (level=2) at test.c:14
#4  0x00000000004005af in test (level=3) at test.c:14
#5  0x00000000004005af in test (level=4) at test.c:14
#6  0x00000000004005af in test (level=5) at test.c:14
#7  0x00000000004005cc in main () at test.c:22
```

and `info frame` for the innermost one:

```
Stack level 0, frame at 0x7fffffffed500:
 rip = 0x40056a in level0 (test.c:5); saved rip = 0x4005bb
 called by frame at 0x7fffffffed530
 source language c.
 Arglist at 0x7fffffffed4f0, args:
 Locals at 0x7fffffffed4f0, Previous frame's sp is 0x7fffffffed500
 Saved registers:
  rbp at 0x7fffffffed4f0, rip at 0x7fffffffed4f8
```

> **Why this output is the whole bridge to the attack, derived.** The recitation presents `info frame` as a debugging aid, but read it next to [[Stack Smashing]] and it is a map of the target. **`saved rip = 0x4005bb`** is the return address an overflow overwrites, and **`rip at 0x7fffffffed4f8`** is the exact address where that value is stored. `rbp at 0x7fffffffed4f0` is the saved frame pointer — the thing an [[Heap and Pointer Overflows|off-by-one]] corrupts — sitting **8 bytes below** the saved return address, exactly as the frame diagram predicts. The distance from a local buffer to `0x7fffffffed4f8` is the offset the attacker spends most of their effort guessing; under a debugger it is simply printed. Note also the frame addresses here are **not randomized**, because gdb disables [[Buffer Overflow Defenses|ASLR]] by default — which is convenient for the lab and the reason an exploit developed under gdb often fails outside it.

Notice too that the recursion makes frames `#2` through `#6` share the return address `0x4005af`: every recursive call returns to the same line. Frame `#1` differs (`0x4005bb`) because that is the call to `level0()` on the other branch.

## A Second Example: `s` Steps Into Library Code

```
(gdb) b main
Breakpoint 1 at 0x40056e: file test.c, line 4.
(gdb) run
Breakpoint 1, main () at test.c:4
4           char *c = "hello world";
(gdb) s
5           printf("%d\n", strlen(c));
(gdb)
strlen () at ../sysdeps/x86_64/strlen.S:66
66      ../sysdeps/x86_64/strlen.S: No such file or directory.
```

This is the `s` versus `n` distinction made concrete: `s` descended into `strlen`, landing in hand-written assembly whose source is not installed. Use `n` to stay in your own code.

## References Given

- `https://www.gnu.org/software/gdb/`
- `https://www.cs.umd.edu/~srhuang/teaching/cmsc212/gdb-tutorial-handout.pdf`
- `https://www.tutorialspoint.com/gnu_debugger/gdb_commands.htm`
- `https://ftp.gnu.org/old-gnu/Manuals/gdb/html_node/gdb_42.html`
- `https://visualgdb.com/gdbreference/commands/info_frame`

## See Also

- [[Buffer Overflow]]
- [[Stack Smashing]]
- [[Heap and Pointer Overflows]]
- [[Buffer Overflow Defenses]]
- [[Unsafe C Functions]]
- [[Process Attributes]]
- [[Processes]]
- [[CSCE 465]]
