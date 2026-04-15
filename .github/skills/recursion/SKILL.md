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

## Available Implementations

Recursion is a fundamental technique used throughout KACTL rather than a standalone implementation. Many algorithms rely on recursive approaches.

### Cross-references

These implementations are primarily recursive:
- `content/graph/SCC.h` — Tarjan's SCC via recursive DFS, O(E+V) (see also: graph-theory skill)
- `content/graph/BiconnectedComponents.h` — Recursive DFS for bridges/biconnected components, O(E+V) (see also: graph-theory skill)
- `content/graph/MaximalCliques.h` — Bron-Kerbosch recursive backtracking, O(3^(n/3)) (see also: graph-theory skill)
- `content/graph/LinkCutTree.h` — Recursive splay operations, O(log N) amortized (see also: graph-theory skill)
- `content/geometry/MinimumEnclosingCircle.h` — Welzl's recursive algorithm, O(n) expected (see also: geometry skill)
- `content/strings/SuffixTree.h` — Ukkonen's algorithm with recursive structure, O(26N) (see also: strings skill)
- `content/various/DivideAndConquerDP.h` — Recursive divide and conquer optimization (see also: dynamic-programming skill)

### Practical Notes

- The KACTL contest template (`content/contest/template.cpp`) can be extended with stack size adjustments for deep recursion
- Consider iterative alternatives when recursion depth exceeds ~10⁶ (typical stack limit)

## Troubleshooting

- **Stack overflow**: Check recursion depth; consider iterative conversion or increasing stack size
- **Wrong answer**: Verify base cases and recursive transitions
- **TLE**: Look for overlapping subproblems that could benefit from memoization
