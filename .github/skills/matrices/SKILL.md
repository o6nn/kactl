---
name: "matrices"
description: "Technique for solving problems using matrix operations."
---

# Matrices

Technique for solving problems using matrix operations.

## Sub-techniques

- Gaussian elimination → `content/numerical/Determinant.h`, `content/numerical/SolveLinear.h`, `content/numerical/MatrixInverse.h`
- Exponentiation by squaring → `content/data-structures/Matrix.h`

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

## Available Implementations

The following implementations from the KACTL codebase are available for this technique:

### Core Matrix Operations
| Algorithm | File | Time Complexity | Description |
|-----------|------|----------------|-------------|
| Matrix | `content/data-structures/Matrix.h` | — | Square matrix operations and exponentiation |
| Determinant | `content/numerical/Determinant.h` | O(N³) | Via Gaussian elimination |
| Integer Determinant | `content/numerical/IntDeterminant.h` | O(N³) | Determinant with modular arithmetic |
| Matrix Inverse | `content/numerical/MatrixInverse.h` | O(n³) | Via Gaussian elimination |
| Matrix Inverse (mod) | `content/numerical/MatrixInverse-mod.h` | O(n³) | Inversion modulo prime |

### Linear Systems
| Algorithm | File | Time Complexity | Description |
|-----------|------|----------------|-------------|
| Solve Ax=b | `content/numerical/SolveLinear.h` | O(n²m) | Solve linear system, returns rank |
| Solve Ax=b (extended) | `content/numerical/SolveLinear2.h` | — | Find all uniquely determined values |
| Solve Ax=b (binary) | `content/numerical/SolveLinearBinary.h` | O(n²m) | Solve over binary field F₂ |
| Tridiagonal | `content/numerical/Tridiagonal.h` | — | Tridiagonal system solver |

### Cross-references

These implementations from other categories also relate to matrices:
- `content/numerical/LinearRecurrence.h` — k'th term of linear recurrence via matrix exponentiation (see also: numerical-methods skill)

### Test Coverage

Stress tests: `IntDeterminant`, `SolveLinear`, `SolveLinear2`, `SolveLinearBinary`, `Tridiagonal`
Old unit tests: `Matrix`

## Troubleshooting

- **Wrong answer**: Check matrix dimensions and indexing; verify modular arithmetic
- **TLE**: Reduce matrix size; ensure O(n^3 log k) for exponentiation
- **Overflow**: Use modular arithmetic throughout matrix operations
- **Precision errors**: Consider pivoting strategies for Gaussian elimination
