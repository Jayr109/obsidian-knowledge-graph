---
title: "CSCE 421 T08 — Convolution"
type: source
tags: [lecture, csce421, convolution, image-filtering, sobel, edge-detection, box-filter]
sources: []
course: CSCE 421
updated: 2026-10-20
---

Topic deck 8 of [[CSCE 421]], *"Based on slides by J. Xiao"*, with figure credits to S. Seitz and David Lowe. 13 slides. A short, entirely visual deck that introduces [[Convolution]] as **classical image filtering** — before any learning is involved — so that [[Convolutional Neural Networks]] can be presented as the idea of *learning* the filters rather than designing them.

> **Extraction note:** this deck is almost pure figures. The filter kernels survive extraction as loose digit grids and the images do not survive at all. Kernels below are reassembled into their 3×3 form; the before/after image pairs are not reproduced. See `raw/CSCE421_T08-conv.pdf`.

## Image Filtering (slides 2–4)

Three build slides showing a 3×3 kernel of all ones sliding over an image grid, each output pixel formed by multiplying the kernel against the window beneath it and summing.

```
1 1 1
1 1 1
1 1 1
```

## Box Filter (slide 5)

The all-ones kernel gets a name and an interpretation:

> **What does it do?**
> - Replaces each pixel with an **average of its neighborhood**
> - Achieve **smoothing** effect (remove sharp features)

Slide 6 shows the result on a photograph. (In practice the kernel is normalized by $1/9$ so the image brightness is preserved; the slide shows the unnormalized form.)

## Practice With Linear Filters (slides 7–10)

Two question-and-answer pairs, each posing a kernel and asking what it does:

**First** — slides 7 and 8:

```
0 0 0
0 1 0        ->  "Filtered (no change)"
0 0 0
```

The identity. The single 1 in the center copies each pixel to itself.

**Second** — slides 9 and 10:

```
0 0 0
1 0 0        ->  "Shifted left by 1 pixel"
0 0 0
```

Moving the 1 off-center translates the image. The direction is worth thinking through carefully: the kernel entry sits to the *left* of center, so each output pixel takes the value of its right-hand neighbor, and the image shifts **left**.

Together these establish that a kernel is not inherently a blur — **the numbers in the kernel decide the operation**, which is precisely why learning them is a sensible thing to do.

## Sobel Filters (slides 11–12)

Two kernels for edge detection, each shown with *"(absolute value)"* — the response is signed and the magnitude is what gets displayed.

**Vertical edges:**

```
-1  0  1
-2  0  2
-1  0  1
```

**Horizontal edges:**

```
-1 -2 -1
 0  0  0
 1  2  1
```

Each is the transpose of the other. The structure is a **difference across the center** — the two sides carry opposite signs, so a region of constant brightness sums to zero and only a change in intensity produces a response. The centre row/column is weighted $2$ rather than $1$, which smooths along the edge while differencing across it.

## The Closing Argument (slide 13)

The only text-heavy slide in the deck, and the reason it exists:

> - Filters can be designed to **detect edges of different orientations**
> - The detected edges can be **combined to form object shapes**, which are important for object recognition
> - **Convolutional neural networks are based on the idea of image convolutions**
> - **Convolutional neural networks use data to train filter parameters**

The last two bullets are the hinge of the whole unit. A Sobel kernel is a filter a *human* designed to find edges. A CNN runs the identical sliding-dot-product machinery, but the nine numbers are **weights learned by gradient descent** — so the network discovers which filters are useful instead of being told.

This is the same substitution [[CSCE 421 T03 — Logistic Regression: From Binary to Multi-Class|T03]] previewed with *"how to learn x automatically?"* and that [[Linear Models]] flags as the step from hand-designed features to [[Deep Learning]].

## See Also

- [[Convolution]]
- [[Convolutional Neural Networks]]
- [[CSCE 421 T09 — Convolutional Neural Networks]]
- [[Deep Learning]]
- [[CSCE 421]]
