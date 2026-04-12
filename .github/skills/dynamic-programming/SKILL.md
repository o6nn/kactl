---
name: "dynamic-programming"
description: "Technique for solving problems by breaking them into overlapping subproblems and storing intermediate results."
---

# Dynamic Programming

Technique for solving problems by breaking them into overlapping subproblems and storing intermediate results.

## Sub-techniques

- Knapsack
- Coin change
- Longest common subsequence
- Longest increasing subsequence
- Number of paths in a dag
- Shortest path in a dag
- Dynprog over intervals
- Dynprog over subsets
- Dynprog over probabilities
- Dynprog over trees
- 3^n set cover
- Divide and conquer
- Knuth optimization
- Convex hull optimizations
- RMQ (sparse table a.k.a 2^k-jumps)
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

## Troubleshooting

- **Wrong answer**: Check base cases and recurrence transitions; verify state definition covers all cases
- **TLE**: Reduce state space or apply optimizations (Knuth, convex hull trick, divide and conquer)
- **MLE**: Use rolling arrays or reduce state dimensions
- **Overflow**: Use appropriate data types for counting problems
