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

## Available Implementations

No standalone combinatorial search templates exist in KACTL. However, several implementations use combinatorial search techniques internally.

### Cross-references

These implementations employ combinatorial search strategies:
- `content/graph/MaximalCliques.h` — Bron-Kerbosch with pruning for all maximal cliques, O(3^(n/3)) (see also: graph-theory skill)
- `content/graph/MaximumClique.h` — Maximum clique with branch-and-bound pruning (see also: graph-theory skill)
- `content/graph/MaximumIndependentSet.h` — Maximum independent set via complement graph clique search (see also: graph-theory skill)
- `content/data-structures/MoQueries.h` — Uses TSP approximation for query ordering, O(N√Q) (see also: data-structures skill)
- `content/various/FastKnapsack.h` — Knapsack with bounded search space, O(N·max(wᵢ)) (see also: dynamic-programming skill)

## Troubleshooting

- **TLE**: Add more pruning; consider meet in the middle; reduce state space
- **Wrong answer**: Verify that pruning doesn't eliminate valid solutions
- **MLE**: Limit search depth; use iterative deepening
- **Stack overflow**: Use iterative deepening instead of deep recursion
