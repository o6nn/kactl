---
name: "greedy-algorithm"
description: "Technique for solving optimization problems by making locally optimal choices at each step."
---

# Greedy Algorithm

Technique for solving optimization problems by making locally optimal choices at each step.

## Sub-techniques

- Scheduling → `content/various/IntervalCover.h` (interval scheduling/covering is a classic greedy problem)
- Max contiguous subvector sum — Kadane's algorithm pattern, no standalone implementation
- Invariants — Conceptual technique
- Huffman encoding — Not implemented in KACTL

## When to Use

- Problems where a locally optimal choice leads to a globally optimal solution
- Scheduling and interval problems
- Minimum spanning trees
- Huffman coding and data compression
- Problems with optimal substructure and greedy choice property

## Key Considerations

- Prove that the greedy choice property holds before implementing
- Verify optimal substructure
- Consider whether sorting the input first enables a greedy approach
- Watch for cases where greedy fails and DP is needed instead

## Available Implementations

### Direct Greedy Implementations

| Algorithm | File | Time | Description |
|-----------|------|------|-------------|
| Interval Cover | `content/various/IntervalCover.h` | O(N log N) | Finds minimum number of intervals covering a target interval |

### Cross-references

These algorithms use greedy strategies internally but live under other skills:

- `content/geometry/ConvexHull.h` — Greedy hull construction, O(n log n) (see also: geometry skill)
- `content/graph/DirectedMST.h` — Greedy arborescence construction, O(E log V) (see also: graph-theory skill)
- `content/various/LIS.h` — Patience sorting (greedy + binary search) for LIS, O(N log N) (see also: dynamic-programming skill)

> **Note:** Greedy algorithms in KACTL are typically embedded within other implementations rather than provided as standalone templates.

## Troubleshooting

- **Wrong answer**: The greedy choice property may not hold; consider DP or other approaches
- **Edge cases**: Check empty input, single-element input, and tied values
- **Sorting issues**: Verify the comparison function is correct and consistent
