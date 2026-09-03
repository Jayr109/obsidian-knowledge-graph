---
title: "SOM Notebook — Self-Organizing Maps (2D Grid)"
type: source
tags: [csce420, som, notebook, python, numpy, unsupervised]
sources: []
course: CSCE 420
updated: 2026-08-25
---

Jupyter notebook implementing a [[Self-Organizing Map]] on a 2D grid (`raw/CSCE420_som.ipynb`, 7 cells, ~8 KB of code, authored by [[Yoonsuck Choe]], dated 1/7/2022). It is a from-scratch NumPy implementation with matplotlib visualization at ten checkpoints during training — the course's hands-on companion to Final Practice Problem 8.

## Structure

| Cell | Type | Contents |
|---|---|---|
| 0 | markdown | Title |
| 1 | code | Docstring header (author, date) |
| 2 | markdown | "Utility Code: weight initialization and plotting" |
| 3 | code | Five utility functions + three self-tests |
| 4 | markdown | "SOM: Main algorithm" |
| 5 | code | `som()` training loop + a configured test run |
| 6 | code | Commented-out alternative parameter run |

## Utility Functions (cell 3)

| Function | Role |
|---|---|
| `som_w_init(n, r)` | Build an $n \times n$ grid of 2D weights via outer product, blended with uniform noise at ratio $r$ |
| `som_w_plot(W0, W1)` | Draw the map as a mesh in input space (rows and columns as connected lines, units as points) |
| `som_neigh(u, v, s)` | Gaussian neighborhood over Euclidean **grid** distance, std $s$ |
| `som_bmu(W0, W1, x)` | Best matching unit — argmin of squared distance in **input** space, converted to (row, col) |
| `som_plot_inp(inp)` | Scatter the input samples on an equal-aspect unit square |
| `som_plot_model(...)` | Composite diagnostic: neighborhood heatmap, the map mesh, the current input (red star), the BMU in grid space (green dot) and in input space (white ×) |

Weights are stored as **two separate $n \times n$ matrices**, `W0` and `W1`, rather than one $n \times n \times 2$ array — so the grid's row/column structure stays visible in the plotting code, and `W1 = W0.T` gives the initial regular grid for free.

## Training Loop (cell 5)

`som(n, inp, alpha, radius, alpha_reduce_rate, radius_reduce_rate, w_rand, num_loop)`:

1. Initialize weights with randomness `w_rand`.
2. For each of `num_loop` iterations: draw a random input, find the BMU, then update **every** unit $(i,j)$ scaled by its Gaussian neighborhood value relative to the BMU.
3. Multiplicatively decay `alpha` and `radius` each iteration.
4. Plot diagnostics ten times across the run.

The inner update is a doubly-nested Python loop over all $n^2$ units — clear rather than vectorized, which suits a teaching implementation.

## Recorded Run

Configuration: `n=15`, 1000 uniform random 2D inputs, `alpha=0.3`, `radius=4.0`, `alpha_reduce_rate=1`, `radius_reduce_rate=1.5`, `w_rand=0.7`, `num_loop=2000`.

| Iteration | $\alpha$ | radius |
|---|---|---|
| 1 | 0.300 | 3.997 |
| 401 | 0.245 | 2.961 |
| 801 | 0.201 | 2.193 |
| 1201 | 0.165 | 1.625 |
| 1401 | 0.149 | 1.398 |

Both decay smoothly by roughly half over the run, with the radius falling faster (its reduce rate is 1.5 against alpha's 1) — the map settles its global topology early, then refines locally.

## Input Distributions

The notebook offers three via `test_select`:

1. **Uniform random** over the unit square (the run above)
2. **Gaussian**, rescaled to $[0,1]$
3. **Hole in the middle** — uniform points filtered to those outside a central disk of radius $\sqrt{0.1}$

The third is the interesting one: it shows the map stretching to cover a **non-convex** support, which is where topology preservation becomes visible rather than trivial.

## Extraction Notes

Outputs are preserved in the notebook: 4 figures from the cell-3 self-tests and 11 from the training run, plus the stdout iteration log. The figures were not extracted during ingest; the numeric log was.

## See Also

- [[Self-Organizing Map]]
- [[Machine Learning Paradigms]]
- [[Yoonsuck Choe]]
- [[CSCE 420]]
