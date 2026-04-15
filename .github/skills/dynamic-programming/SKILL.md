---
name: "dynamic-programming"
description: "Technique for solving problems by breaking them into overlapping subproblems and storing intermediate results."
---

# Dynamic Programming

Technique for solving problems by breaking them into overlapping subproblems and storing intermediate results.

## Sub-techniques

- Knapsack — see [`content/various/FastKnapsack.h`](../../../content/various/FastKnapsack.h)
- Coin change
- Longest common subsequence
- Longest increasing subsequence — see [`content/various/LIS.h`](../../../content/various/LIS.h)
- Number of paths in a dag
- Shortest path in a dag
- Dynprog over intervals
- Dynprog over subsets
- Dynprog over probabilities
- Dynprog over trees
- 3^n set cover
- Divide and conquer (DP optimization) — see [`content/various/DivideAndConquerDP.h`](../../../content/various/DivideAndConquerDP.h)
- Knuth optimization — see [`content/various/KnuthDP.h`](../../../content/various/KnuthDP.h)
- Convex hull optimizations — see [`content/data-structures/LineContainer.h`](../../../content/data-structures/LineContainer.h) (cross-ref)
- RMQ (sparse table a.k.a 2^k-jumps) — see [`content/data-structures/RMQ.h`](../../../content/data-structures/RMQ.h) (cross-ref)
- Bitonic cycle
- Log partitioning (loop over most restricted)

## When to Use

- Problems with overlapping subproblems and optimal substructure
- Counting problems
- Optimization problems where greedy fails
- String comparison and edit distance
- Subset and bitmask problems

## Key Considerations

- Define the state space clearly
- Identify the recurrence relation
- Determine the base cases
- Choose between top-down (memoization) and bottom-up (tabulation)
- Consider space optimization (rolling arrays)

## Available Implementations

| Algorithm | File | Time | Description |
|-----------|------|------|-------------|
| Knuth DP | [`KnuthDP.h`](../../../content/various/KnuthDP.h) | O(N²) | Knuth optimization for interval DP |
| D&C DP | [`DivideAndConquerDP.h`](../../../content/various/DivideAndConquerDP.h) | O((N+hi−lo) log N) | Divide and conquer DP optimization |
| Fast Knapsack | [`FastKnapsack.h`](../../../content/various/FastKnapsack.h) | O(N·max(wᵢ)) | 0/1 knapsack for bounded weights |
| LIS | [`LIS.h`](../../../content/various/LIS.h) | O(N log N) | Longest increasing subsequence with index recovery |

**Cross-references (other skills):**

- [`content/data-structures/LineContainer.h`](../../../content/data-structures/LineContainer.h) — Convex hull trick for DP optimization (see also: data-structures skill)
- [`content/data-structures/RMQ.h`](../../../content/data-structures/RMQ.h) — Sparse table for DP range queries (see also: data-structures skill)
- [`content/numerical/LinearRecurrence.h`](../../../content/numerical/LinearRecurrence.h) — Compute k'th term of linear recurrence (see also: numerical-methods skill)

> **Note:** Many DP sub-techniques (Coin change, LCS, Dynprog over intervals/subsets/probabilities/trees, 3^n set cover, Bitonic cycle, Log partitioning) are _patterns_ rather than standalone implementations.

**Stress tests:** `FastKnapsack`, `LIS` (see `stress-tests/`)

## Troubleshooting

- **Wrong answer**: Check base cases and recurrence transitions; verify state definition covers all cases
- **TLE**: Reduce state space or apply optimizations (Knuth, convex hull trick, divide and conquer)
- **MLE**: Use rolling arrays or reduce state dimensions
- **Overflow**: Use appropriate data types for counting problems
