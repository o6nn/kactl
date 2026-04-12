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

## Troubleshooting

- **Wrong answer**: Verify game state transitions; check base cases for terminal positions
- **TLE**: Memoize game states; reduce state space
- **Infinite loops**: Handle games with cycles using draw detection
