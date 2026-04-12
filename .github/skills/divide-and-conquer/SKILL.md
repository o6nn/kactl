---
name: "divide-and-conquer"
description: "Technique for solving problems by dividing them into smaller subproblems, solving each independently, and combining results."
---

# Divide and Conquer

Technique for solving problems by dividing them into smaller subproblems, solving each independently, and combining results.

## Sub-techniques

- Finding interesting points in N log N

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

## Troubleshooting

- **TLE**: Verify that the divide and combine steps are efficient; check the recurrence relation
- **Wrong answer**: Ensure merging handles boundary elements correctly
- **Off-by-one errors**: Check partition indices carefully
