---
name: "sorting"
description: "Technique for arranging elements in a specific order."
---

# Sorting

Technique for arranging elements in a specific order.

## Sub-techniques

- Radix sort

## When to Use

- Problems requiring ordered data
- As a preprocessing step for other algorithms
- Problems where sorting reveals structure (e.g., greedy approaches)
- Counting and ranking problems

## Key Considerations

- Choose the right sorting algorithm for the data size and type
- Use stable sort when relative order matters
- Consider radix sort for integer data with bounded range
- Custom comparators must be strict weak orderings

## Available Implementations

Sorting in KACTL relies on `std::sort` from the C++ standard library rather than standalone implementations. Sorting is used as a subroutine in many algorithms throughout the codebase.

### Cross-references

These implementations use sorting as a key subroutine:
- `content/geometry/ConvexHull.h` — Sorts points before hull construction, O(n log n) (see also: geometry skill)
- `content/geometry/ClosestPair.h` — Sort-based divide and conquer, O(n log n) (see also: geometry skill)
- `content/geometry/Angle.h` — Angle sorting for rotational sweep (see also: geometry, sweeping skills)
- `content/various/IntervalCover.h` — Sorts intervals for greedy covering, O(N log N) (see also: greedy-algorithm skill)
- `content/strings/SuffixArray.h` — Suffix sorting via radix sort, O(n log n) (see also: strings skill)
- `content/geometry/ManhattanMST.h` — Sorts by coordinate differences, O(N log N) (see also: geometry skill)
- `content/various/LIS.h` — Uses sorted structure for patience sorting, O(N log N) (see also: dynamic-programming skill)

## Troubleshooting

- **Wrong answer**: Verify the comparison function defines a strict weak ordering
- **TLE**: Use O(n log n) sorting; consider radix sort for integers
- **Runtime error**: Check comparator consistency (antisymmetry, transitivity)
