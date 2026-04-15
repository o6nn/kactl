---
name: "matrices"
description: "Technique for solving problems using matrix operations."
---

# Matrices

Technique for solving problems using matrix operations.

## Sub-techniques

- Gaussian elimination
- Exponentiation by squaring

## When to Use

- Solving systems of linear equations
- Computing linear recurrences efficiently
- Graph problems expressible as matrix operations
- Problems involving state transitions that can be represented as matrices

## Key Considerations

- Use matrix exponentiation for linear recurrences with large n
- Handle modular arithmetic in matrix operations
- Consider numerical stability for floating-point matrices
- Optimize matrix size to reduce complexity

## Troubleshooting

- **Wrong answer**: Check matrix dimensions and indexing; verify modular arithmetic
- **TLE**: Reduce matrix size; ensure O(n^3 log k) for exponentiation
- **Overflow**: Use modular arithmetic throughout matrix operations
- **Precision errors**: Consider pivoting strategies for Gaussian elimination
