---
name: "recursion"
description: "Technique for solving problems by breaking them into smaller subproblems of the same type."
---

# Recursion

Technique for solving problems by breaking them into smaller subproblems of the same type.

## When to Use

- Problems that have a naturally recursive structure
- Tree and graph traversals
- Generating permutations and combinations
- Problems where the solution depends on solutions to smaller instances

## Key Considerations

- Define clear base cases to avoid infinite recursion
- Ensure the recursive calls converge toward the base case
- Consider stack depth limits for deep recursion
- Evaluate whether memoization or iterative approaches would be more efficient

## Troubleshooting

- **Stack overflow**: Check recursion depth; consider iterative conversion or increasing stack size
- **Wrong answer**: Verify base cases and recursive transitions
- **TLE**: Look for overlapping subproblems that could benefit from memoization
