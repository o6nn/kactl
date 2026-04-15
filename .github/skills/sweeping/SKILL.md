---
name: "sweeping"
description: "Technique for solving problems by processing events in a specific order."
---

# Sweeping

Technique for solving problems by processing events in a specific order.

## Sub-techniques

- Angle sweeping → `content/geometry/Angle.h`
- Discretization (convert to events and sweep) — Pattern, no standalone implementation
- Line sweeping — Pattern used by many algorithms, no standalone implementation
- Discrete second derivatives — Conceptual technique

## When to Use

- Interval and range problems
- Geometric intersection problems
- Problems that can be decomposed into events
- Finding overlaps, intersections, or coverage

## Key Considerations

- Sort events by the sweep coordinate
- Maintain an appropriate data structure during the sweep
- Handle simultaneous events carefully (tie-breaking)
- Consider what information needs to be tracked during the sweep

## Available Implementations

Sweeping is primarily a technique pattern. Most sweep-based algorithms in KACTL are found in the geometry and various folders.

### Direct Implementations

| Algorithm | File | Time | Description |
|-----------|------|------|-------------|
| Angle | `content/geometry/Angle.h` | — | Angle ordering class for rotational/angular sweeping |

### Cross-references

Implementations that use sweeping as a core technique:

- `content/various/IntervalContainer.h` — Disjoint interval set with event-based merging, O(log N) (see also: data-structures skill)
- `content/various/IntervalCover.h` — Minimum interval cover via greedy sweep, O(N log N) (see also: greedy-algorithm skill)
- `content/various/ConstantIntervals.h` — Splits monotone function into constant intervals, O(k log(n/k)) (see also: optimization skill)
- `content/geometry/ConvexHull.h` — Convex hull uses sorted sweep, O(n log n) (see also: geometry skill)
- `content/geometry/ClosestPair.h` — Closest pair via sweep-line, O(n log n) (see also: geometry skill)
- `content/geometry/PolygonUnion.h` — Polygon union via sweep, O(N²) (see also: geometry skill)
- `content/geometry/ManhattanMST.h` — Manhattan MST uses angle sweep, O(N log N) (see also: geometry skill)

## Troubleshooting

- **Wrong answer**: Check event ordering and tie-breaking rules
- **TLE**: Use efficient data structures (balanced BST, segment tree) during sweep
- **Edge cases**: Handle coincident events and boundary conditions
