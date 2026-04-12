---
name: "algorithm-analysis"
description: "Technique for analyzing the time and space complexity of algorithms."
---

# Algorithm Analysis

Technique for analyzing the time and space complexity of algorithms.

## Sub-techniques

- Master theorem
- Amortized time complexity

## When to Use

- Determining whether an algorithm will pass within time and memory limits
- Comparing alternative approaches
- Identifying bottlenecks in a solution
- Verifying that optimizations are effective

## Key Considerations

- **Master theorem**: For recurrences of the form T(n) = aT(n/b) + O(n^d)
- **Amortized analysis**: For operations that are expensive occasionally but cheap on average (e.g., dynamic arrays, splay trees)
- Consider constant factors for tight time limits
- Account for hidden complexity in STL operations (e.g., map vs unordered_map)

## Troubleshooting

- **TLE**: Re-analyze complexity; look for hidden O(n) operations inside loops
- **Unexpected behavior**: Verify that amortized assumptions hold for the specific usage pattern
