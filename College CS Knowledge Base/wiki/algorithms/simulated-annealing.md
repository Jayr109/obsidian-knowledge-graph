---
title: "Simulated Annealing"
type: algorithm
tags: [csce420, local-search, optimization, metropolis, temperature]
sources: [csce420-midterm-practice, csce420-lecture-02-search-and-game-playing]
course: CSCE 420
updated: 2026-09-01
---

Simulated annealing is [[Local Search|local search]] that escapes local optima by sometimes accepting a worsening move, with the probability of doing so controlled by a temperature parameter that decreases over time. The name and the schedule come from metallurgy: heat a metal, then cool it slowly enough that its atoms settle into a low-energy crystalline state rather than freezing into a defective one.

## Algorithm

1. Start from an initial state with temperature $T$ high.
2. Pick a random neighbor and compute $\Delta E$, the change in objective value.
3. If the move improves the objective, always accept it.
4. If it worsens the objective, accept it anyway with probability
   $$P(\Delta E) = e^{-\Delta E / T}$$
5. Decrease $T$ according to a cooling schedule; repeat.

As $T \to 0$ the acceptance probability for any worsening move goes to zero and the algorithm degenerates into hill climbing. As $T \to \infty$ it accepts nearly everything and becomes a random walk. The schedule interpolates between exploration and exploitation.

## Reading the Acceptance Probability (Midterm Practice, Problem 3)

The problem asks, for $\Delta E > 0$ (a suboptimal move), which conditions raise the probability of acceptance. Read it straight off $P = e^{-\Delta E / T}$:

| Factor | Effect on $P(\Delta E)$ | Answer |
|---|---|---|
| $\Delta E$ | Larger $\Delta E$ makes the exponent more negative, so $P$ falls | **Lower** $\Delta E$ |
| $T$ | Larger $T$ makes the exponent closer to zero, so $P$ rises | **Higher** $T$ |

The accompanying plot confirms both: it graphs $P(\Delta E)$ against $\Delta E$ for $T = 1, 5, 10$, and every curve decreases in $\Delta E$ while the higher-$T$ curves sit above the lower ones everywhere.

Intuitively: small mistakes are cheaper to accept than large ones, and a hot system is more willing to make mistakes than a cold one.

> Worked here from the figure; the practice exam ships without an answer key.

## Guarantee

With a sufficiently slow cooling schedule, simulated annealing finds the global optimum with probability approaching 1. "Sufficiently slow" is generally too slow to be practical, so real applications use faster schedules and settle for good solutions.

## From the Lecture

### The Physical Analogy

**Annealing** is heating metal to a liquid and cooling it slowly into a solid, which relieves internal stresses and reaches a more stable, lower-energy state. At high temperature atoms move actively over large distances with greater randomness; as temperature drops they become static.

Simulated annealing is **hill climbing with randomness that permits downhill (suboptimal) as well as uphill moves**, with the randomness reduced over time.

### The Acceptance Rule

The goal is to **minimize energy $E$**, as in statistical thermodynamics. For successors of the current node, with $\Delta E = E_{new} - E_{old}$:

- If $\Delta E \le 0$ (desired), **accept**.
- If $\Delta E > 0$ (undesired), accept with probability

$$P(\Delta E) = e^{-\Delta E / kT}$$

where $k$ is the **Boltzmann constant** and $T$ is temperature.

**The randomness lives in the comparison**: draw $\text{rand}(0,1)$ and accept if $P(\Delta E) > \text{rand}(0,1)$ — the *rejection method*.

### Reading the Two Knobs

- **Higher temperature $T$** → higher probability of a suboptimal move
- **Lower $\Delta E$** → higher probability of a suboptimal move

So downward moves of *any size* are allowed at high temperature, but at low temperature only *small* downward moves survive. The search anneals from exploration into exploitation.

### The Reduction Schedule

- **Too fast** → suboptimal solution (quenching into a local minimum)
- **Too slow** → wasted time

Whether the *form* of the curve matters — linear, quadratic, exponential — is posed as an open question; the lecture notes proper values are usually found **experimentally**.

### Applications

VLSI wire routing and placement, scheduling optimization, traffic control, and neural network training.

## See Also

- [[Local Search]]
- [[Heuristic Search]]
- [[CSCE 420]]
