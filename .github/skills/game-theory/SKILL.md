---
name: "game-theory"
description: "Technique for analyzing competitive situations with multiple decision-makers."
---

# Game Theory

Technique for analyzing competitive situations with multiple decision-makers.

## Sub-techniques

- Combinatorial games
- Game trees
- Mini-max
- Nim
- Games on graphs
- Games on graphs with loops
- Grundy numbers
- Bipartite games without repetition
- General games without repetition
- Alpha-beta pruning

## When to Use

- Two-player games with perfect information
- Problems asking who wins with optimal play
- Nim and Sprague-Grundy theory applications
- Minimax decision problems

## Key Considerations

- Identify winning and losing positions
- Compute Grundy numbers for game decomposition
- Use memoization for game state evaluation
- Consider whether the game has loops (may need special handling)

## Available Implementations

No standalone game theory implementations exist in the KACTL codebase. Game-theoretic solutions typically combine dynamic programming (for Grundy number computation) and graph techniques (for game state exploration).

### Cross-references

These implementations from other categories are commonly used in game theory solutions:
- `content/various/KnuthDP.h` — DP optimization applicable to game-theoretic interval problems (see also: dynamic-programming skill)
- `content/graph/SCC.h` — Strongly connected components for games on graphs with cycles (see also: graph-theory skill)
- `content/graph/2sat.h` — 2-SAT for constraint-based game analysis (see also: graph-theory skill)
- `content/numerical/LinearRecurrence.h` — Can model Markov chain / game state transitions (see also: numerical-methods skill)

## Troubleshooting

- **Wrong answer**: Verify game state transitions; check base cases for terminal positions
- **TLE**: Memoize game states; reduce state space
- **Infinite loops**: Handle games with cycles using draw detection
