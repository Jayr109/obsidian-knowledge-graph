---
title: "Self-Organizing Map"
type: algorithm
tags: [csce420, som, unsupervised, kohonen, topology-preserving, competitive-learning]
sources: [csce420-final-practice, csce420-som-notebook, csce420-lecture-06-machine-learning]
course: CSCE 420
updated: 2026-09-01
---

A Self-Organizing Map (SOM, or Kohonen map) is an unsupervised neural network that learns a **topology-preserving** low-dimensional representation of an input distribution. Units are arranged on a fixed grid — the course uses a 2D $n \times n$ grid — and each unit $j$ holds a weight vector $\mathbf{w}_j$ living in the input space. Training pulls each unit toward inputs it wins, and drags its grid neighbors along with it, so nearby units end up representing nearby inputs.

## Learning Rule

$$\mathbf{w}_j \leftarrow \mathbf{w}_j + \alpha\, \Lambda(i(\mathbf{x}), j)\,(\mathbf{x} - \mathbf{w}_j)$$

| Symbol | Meaning |
|---|---|
| $\mathbf{w}_j$ | Weight vector for unit $j$ |
| $\alpha$ | Learning rate |
| $\Lambda(\cdot,\cdot)$ | Neighborhood function over **grid** distance |
| $i(\mathbf{x})$ | Index of the **best matching unit** (BMU) for input $\mathbf{x}$ |

**It is unsupervised** — see [[Machine Learning Paradigms]]. No target or reward appears in the rule; the only external quantity is the input $\mathbf{x}$ itself, and the "error" $(\mathbf{x} - \mathbf{w}_j)$ measures distance from the input rather than from a label. This is Final Practice Problem 8, answer **(2) Unsupervised Learning**.

## Algorithm

1. Initialize weights (a regular grid plus noise, or fully random).
2. Draw an input $\mathbf{x}$ at random from the dataset.
3. Find the **BMU**: the unit whose weight vector is nearest $\mathbf{x}$ in input space.
4. Update *every* unit by the rule above, scaled by its neighborhood value relative to the BMU.
5. Decay $\alpha$ and the neighborhood radius; repeat.

Two distances are in play and confusing them is the usual mistake: step 3 measures distance in the **input space**, while $\Lambda$ in step 4 measures distance on the **grid**. Topology preservation is exactly this coupling — competition in input space, cooperation in grid space.

## Course Implementation

`som.ipynb` by [[Yoonsuck Choe]] implements the above on an $n \times n$ grid over 2D inputs, storing the two weight components as separate matrices `W0` and `W1`.

**Weight initialization** (`som_w_init(n, r)`) builds a regular grid via an outer product, then blends in uniform noise controlled by a randomness parameter $r \in [0,1]$:

```python
W0 = np.outer(a_ones, a_idx) / n     # columns 0..n-1, normalized
W1 = np.transpose(W0)                 # rows
W0 = W0*(1-r) + (np.random.rand(n,n)*r)
W1 = W1*(1-r) + (np.random.rand(n,n)*r)
```

At $r = 0$ the map starts as a perfect grid; at $r = 1$ it starts fully scrambled. Watching an $r = 1$ map untangle itself is the point of the demo.

**Best matching unit** (`som_bmu`) uses squared Euclidean distance and recovers grid coordinates from the flat argmin:

```python
dist = (W0-x[0])**2 + (W1-x[1])**2
idx  = dist.argmin()
bmu  = np.array([idx // n, idx % n])   # row, col
```

**Neighborhood function** (`som_neigh`) is an unnormalized-radius Gaussian over grid distance, with $s$ acting as the neighborhood radius:

$$\Lambda(u,v) = \frac{1}{s\sqrt{2\pi}} \exp\!\left(-\frac{\|u-v\|^2}{2s^2}\right)$$

**Decay.** Both parameters shrink multiplicatively each iteration:

```python
alpha  = alpha  * (1 - 1/(num_loop/alpha_reduce_rate))
radius = radius * (1 - 1/(num_loop/radius_reduce_rate))
```

A representative run (`n=15`, 1000 uniform random 2D inputs, `alpha=0.3`, `radius=4.0`, `radius_reduce_rate=1.5`, `w_rand=0.7`, `num_loop=2000`) decays $\alpha$ from 0.300 to about 0.149 and the radius from 4.0 to about 1.40 by iteration 1401.

The schedule is the crux of the algorithm. A **large early radius** moves big patches of the map together, unfolding the global topology; a **small late radius** tunes individual units to local detail. Cooling too fast leaves the map folded — a knot it can never undo, since by then no update reaches far enough to pull it apart. This is the same exploration-to-exploitation annealing idea as [[Simulated Annealing]].

The notebook offers three input distributions to train on: uniform random, Gaussian, and uniform-with-a-hole (points outside a central disk), the last of which shows the map stretching to cover a non-convex support.

## From the Lecture

### Setup

Kohonen (1982). A 1-D, 2-D, or 3-D **layout of units**, each carrying **one reference vector**, trained by unsupervised learning with **no target output**.

### The Algorithm

1. **Randomly initialize** reference vectors $w_i$
2. **Randomly sample** an input vector $x$
3. **Find the Best Matching Unit (BMU)**: $i(x) = \arg\min_j \lVert x - w_j \rVert$
4. **Update reference vectors**: $w_j \leftarrow w_j + \alpha \Lambda(i(x), j)(x - w_j)$
   - $\alpha$ — learning rate
   - $\Lambda(i(x), j)$ — **neighborhood function** of the BMU
5. **Repeat** steps 2–4

### Reading the Update Rule

The term $(x - w_j)$ moves the reference vector **toward the input** — the deck illustrates that $w_i + (x_k - w_i) = x_k$ would move it all the way, so $\alpha$ controls the fraction of that distance travelled.

The neighborhood function $\Lambda$ is what makes it a *map* rather than plain clustering: units **near the BMU on the lattice** are dragged along too, so lattice adjacency comes to reflect input-space proximity. That is the **feature mapping** capability listed in [[Unsupervised Learning]] — a topographic mapping of input space onto the network's configuration.

### Why It Is Unsupervised

Every term in the update is a weight, a hyperparameter, the input itself, or a function of the network's own geometry. **No target value and no reward appears anywhere** — see [[Machine Learning Paradigms]], where this equation is the worked exam example.

## See Also

- [[Machine Learning Paradigms]]
- [[Neural Networks]]
- [[Simulated Annealing]]
- [[Yoonsuck Choe]]
- [[Foundations of AI]]
