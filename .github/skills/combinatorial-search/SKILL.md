---
name: "combinatorial-search"
description: "Technique for exploring solution spaces systematically."
---

# Combinatorial Search

Technique for exploring solution spaces systematically.

## Sub-techniques

- Meet in the middle
- Brute-force with pruning
- Best-first (A*)
- Bidirectional search
- Iterative deepening DFS / A*

## When to Use

- Problems with small input sizes where exhaustive search is feasible
- Optimization problems where heuristic search is effective
- Problems that can be split and solved from both ends
- Puzzle-solving and state-space exploration

## Key Considerations

- Estimate the search space size before choosing an approach
- Use pruning to reduce the search space
- Meet in the middle can reduce O(2^n) to O(2^(n/2))
- Choose appropriate heuristics for A* search

## Troubleshooting

- **TLE**: Add more pruning; consider meet in the middle; reduce state space
- **Wrong answer**: Verify that pruning doesn't eliminate valid solutions
- **MLE**: Limit search depth; use iterative deepening
- **Stack overflow**: Use iterative deepening instead of deep recursion
