---
title: "Topographic Maps"
type: concept
tags: [maps, topography, contours, gradient, relief, lab-skills]
sources: [lab-05-topographic-maps]
course: GEOL 101
updated: 2026-07-20
---

A **topographic map** shows the three-dimensional shape of the land surface on a two-dimensional sheet by means of **contour lines** — lines connecting points of equal elevation. Reading and constructing them is a core laboratory skill: contours encode slope, relief, landform shape, and drainage direction, and they support quantitative measurements of distance and gradient.

## Contour Lines

A **contour line** connects all points at the same elevation above sea level. The **shoreline of the ocean is the 0-foot contour** by definition.

### Rules Contours Always Obey
- Contours **never cross** and never branch.
- A contour either **closes on itself** or **runs off the edge of the map**. It never simply stops in the middle.
- Contours pass **through** points of equal elevation, not near them.
- **Closely spaced contours = steep slope**; widely spaced = gentle slope.
- **Evenly spaced** contours indicate a uniform slope.

### The Rule of V's
Where a contour crosses a stream valley it **bends upstream**, forming a V that points up-valley (uphill). This is the single most reliable way to determine which way a stream flows on a contour map: the V's point upstream.

### Depression Contours
A closed depression is drawn with **hachures** — short tick marks pointing down into the hollow.

- The **first hachured contour repeats the elevation** of the regular contour enclosing it.
- Successive hachured contours then **decrease** inward by the contour interval.

A hill and a depression can look identical without the hachures, so the tick marks carry all the information.

## Contour Interval

The **contour interval (CI)** is the elevation difference between adjacent contours.

**To determine it:** find two contours whose elevations are printed, count the number of contour **spaces** between them, and divide the elevation difference by that count. Counting lines instead of spaces is the classic error.

**Index contours** are the heavier, labeled lines. By USGS convention **every 5th contour is an index contour**, so where index contours are 200 ft apart the interval is 200 ÷ 5 = 40 ft.

## Relief

**Relief** is the difference in elevation between two points. **Total relief** is the difference between the highest and lowest points on a map.

A **benchmark** (`BM`, often with a triangle symbol) is a surveyed point with a precisely known elevation. A benchmark elevation caps the contours: if the summit benchmark reads 675 ft with a 100 ft interval, the highest contour drawn is 600 — there is no 700.

## Gradient (Slope)

**Gradient** is elevation change divided by horizontal distance, with both expressed in the same units:

> gradient = elevation change ÷ horizontal distance

Reported as ft/ft, as ft per mile, or as a ratio. A gradient of 0.17 ft/ft is roughly 1:6.

Because the two distances are measured the same way, gradient is **scale-independent** — it comes out the same regardless of how the map is printed.

## Map Scale

A **bar scale** shows a known ground distance as a bar on the map. To convert a measured map distance to ground distance, set up a proportion:

> if 30 mm = 1000 ft, then 72 mm = (72 ÷ 30) × 1000 = 2400 ft

The ratio of the two measured lengths is what matters, so this works on any printed copy regardless of size.

## Interpolation and Map Construction

**Interpolation** estimates an elevation between two known points by assuming a uniform slope between them. To place the 100 ft contour between a point at 84 ft and one at 110 ft, it falls (100 − 84) ÷ (110 − 84) = 62% of the way from the first point toward the second.

**Extrapolation** extends the trend beyond the outermost data points, out to the edge of the map.

## Digital Tools

**Google Earth** provides latitude, longitude, and elevation readouts, a ruler for measuring distance, layer toggles, and (in the Pro desktop version only) historical imagery. It is useful in geology for identifying landforms from above, tracing fault traces and fold outcrop patterns, reading seafloor bathymetry at [[Plate Tectonics]] boundaries, measuring features, and observing change through time — coastal retreat, glacier recession, landslide scars, and channel migration.

## See Also
- [[Latitude and Longitude]]
- [[Lab 5: Topographic Maps and Google Earth]]
- [[Streams and Rivers]]
- [[Mountain Building]]
- [[Glacial Landforms]]
