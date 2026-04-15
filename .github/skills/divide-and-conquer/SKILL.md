---
name: "divide-and-conquer"
description: "Technique for solving problems by dividing them into smaller subproblems, solving each independently, and combining results."
---

# Divide and Conquer

Technique for solving problems by dividing them into smaller subproblems, solving each independently, and combining results.

## Sub-techniques

- Finding interesting points in N log N → `content/geometry/ClosestPair.h`

## When to Use

- Problems where the input can be split into independent halves
- Merge sort, quicksort, and related sorting algorithms
- Closest pair of points
- Counting inversions
- Problems solvable by processing halves and merging results

## Key Considerations

- Identify how to divide the problem into subproblems
- Ensure the combine step is efficient
- Analyze complexity using the Master theorem
- Consider edge cases when the input size is small or odd

## Available Implementations

| Algorithm | File | Time | Description |
|-----------|------|------|-------------|
| Divide & Conquer DP | `content/various/DivideAndConquerDP.h` | O((N+hi-lo) log N) | D&C optimization when optimal split point is monotone |
| Closest Pair | `content/geometry/ClosestPair.h` | O(n log n) | Closest pair of points via divide and conquer |

### Cross-references

These algorithms use divide and conquer internally but live under other skills:

- `content/numerical/FastFourierTransform.h` — FFT uses divide and conquer (see also: numerical-methods skill)
- `content/numerical/NumberTheoreticTransform.h` — NTT uses divide and conquer (see also: numerical-methods skill)
- `content/strings/SuffixArray.h` — Suffix array construction (see also: strings skill)

### Stress Tests

No dedicated stress tests for these as D&C implementations, but ClosestPair has stress tests (via geometry).

## Troubleshooting

- **TLE**: Verify that the divide and combine steps are efficient; check the recurrence relation
- **Wrong answer**: Ensure merging handles boundary elements correctly
- **Off-by-one errors**: Check partition indices carefully
