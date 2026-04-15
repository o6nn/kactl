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

## Available Implementations

Algorithm analysis is a meta-technique for evaluating correctness and efficiency. There are no standalone implementations, but KACTL provides reference material.

### Reference Material

- `content/appendix/techniques.txt` — Master list of 160 algorithmic techniques with categorized sub-techniques, useful for identifying the right approach during contests

### Cross-references

These implementations demonstrate key complexity analysis patterns:
- `content/data-structures/RMQ.h` — Example of O(|V| log |V|) preprocessing + O(1) query tradeoff (see also: data-structures skill)
- `content/data-structures/MoQueries.h` — O(N√Q) amortized block decomposition analysis (see also: data-structures skill)  
- `content/numerical/BerlekampMassey.h` — O(N²) amortized analysis for recurrence recovery (see also: numerical-methods skill)

## Troubleshooting

- **TLE**: Re-analyze complexity; look for hidden O(n) operations inside loops
- **Unexpected behavior**: Verify that amortized assumptions hold for the specific usage pattern
