---
name: "numerical-methods"
description: "Technique for solving mathematical problems using numerical approximation."
---

# Numerical Methods

Technique for solving mathematical problems using numerical approximation.

## Sub-techniques

- Numeric integration — `content/numerical/Integrate.h`, `content/numerical/IntegrateAdaptive.h`
- Newton's method
- Root-finding with binary/ternary search — `content/numerical/PolyRoots.h`
- Golden section search — `content/numerical/GoldenSectionSearch.h`
- FFT/NTT — `content/numerical/FastFourierTransform.h`, `content/numerical/FastFourierTransformMod.h`, `content/numerical/NumberTheoreticTransform.h`
- Berlekamp-Massey — `content/numerical/BerlekampMassey.h`
- Linear recurrence — `content/numerical/LinearRecurrence.h`
- Simplex method — `content/numerical/Simplex.h`
- Matrix operations — `content/numerical/Determinant.h`, `content/numerical/SolveLinear.h`, `content/numerical/MatrixInverse.h`

## When to Use

- Problems requiring numerical solutions to equations
- Integration and area computation
- Root finding for non-linear equations
- Optimization of continuous functions

## Key Considerations

- Control numerical precision with appropriate tolerances
- Be aware of convergence conditions for iterative methods
- Handle edge cases where methods may diverge
- Use appropriate step sizes for integration

## Available Implementations

### Polynomials
| Algorithm | File | Time | Description |
|-----------|------|------|-------------|
| Polynomial | `content/numerical/Polynomial.h` | — | Polynomial struct with evaluation and differentiation |
| Polynomial Roots | `content/numerical/PolyRoots.h` | O(n² log(1/ε)) | Finds real roots via ternary search |
| Polynomial Interpolation | `content/numerical/PolyInterpolate.h` | O(n²) | Lagrange interpolation |

### Linear Recurrences
| Algorithm | File | Time | Description |
|-----------|------|------|-------------|
| Berlekamp-Massey | `content/numerical/BerlekampMassey.h` | O(N²) | Recovers linear recurrence from 2n terms |
| Linear Recurrence | `content/numerical/LinearRecurrence.h` | O(n² log k) | k'th term of linear recurrence |

### Optimization
| Algorithm | File | Time | Description |
|-----------|------|------|-------------|
| Golden Section Search | `content/numerical/GoldenSectionSearch.h` | O(log((b-a)/ε)) | Minimizes unimodal function |
| Hill Climbing | `content/numerical/HillClimbing.h` | — | Optimization for unimodal functions |
| Simplex | `content/numerical/Simplex.h` | — | Linear programming: maximize c^T x subject to Ax ≤ b |

### Integration
| Algorithm | File | Time | Description |
|-----------|------|------|-------------|
| Simpson's Rule | `content/numerical/Integrate.h` | — | Numerical integration via Simpson's rule |
| Adaptive Simpson | `content/numerical/IntegrateAdaptive.h` | — | Fast adaptive Simpson's integration |

### Matrix Operations
| Algorithm | File | Time | Description |
|-----------|------|------|-------------|
| Determinant | `content/numerical/Determinant.h` | O(N³) | Gaussian elimination determinant |
| Integer Determinant | `content/numerical/IntDeterminant.h` | O(N³) | Determinant with modular arithmetic |
| Solve Linear | `content/numerical/SolveLinear.h` | O(n²m) | Solve Ax=b, returns rank |
| Solve Linear 2 | `content/numerical/SolveLinear2.h` | — | Extended: finds all uniquely determined values |
| Solve Linear Binary | `content/numerical/SolveLinearBinary.h` | O(n²m) | Solve Ax=b over F₂ |
| Matrix Inverse | `content/numerical/MatrixInverse.h` | O(n³) | Matrix inversion via Gaussian elimination |
| Matrix Inverse (mod) | `content/numerical/MatrixInverse-mod.h` | O(n³) | Matrix inversion modulo prime |
| Tridiagonal | `content/numerical/Tridiagonal.h` | — | Tridiagonal system solver |
| Sylvester AX+XB=C | `content/numerical/SylvesterSolve.h` | O(m³n³) | Sylvester equation via Kronecker product reduction |

### Transforms
| Algorithm | File | Time | Description |
|-----------|------|------|-------------|
| FFT | `content/numerical/FastFourierTransform.h` | O(N log N) | Fast Fourier Transform for convolution |
| FFT (mod) | `content/numerical/FastFourierTransformMod.h` | O(N log N) | FFT for arbitrary modulus |
| NTT | `content/numerical/NumberTheoreticTransform.h` | O(N log N) | Number Theoretic Transform for nice primes |
| Fast Subset Transform | `content/numerical/FastSubsetTransform.h` | O(N log N) | AND/OR/XOR convolution |

### Stress Tests
Implementations with stress tests in `stress-tests/`: BerlekampMassey, FastFourierTransform, FastFourierTransformMod, FastSubsetTransform, IntDeterminant, LinearRecurrence, NumberTheoreticTransform, SolveLinear, SolveLinear2, SolveLinearBinary, SylvesterSolve, Tridiagonal.

### Old Unit Tests
Implementations with old unit tests in `old-unit-tests/`: goldenSectionSearch.

### Cross-references
- `content/data-structures/Matrix.h` — Basic matrix operations and exponentiation (see also: matrices, data-structures skills)
- **solver** skill — Cross-check numerical algorithms against SciPy/NumPy reference solvers

## Troubleshooting

- **Wrong answer**: Check convergence tolerance; verify initial conditions
- **TLE**: Reduce number of iterations; use faster converging methods
- **Precision errors**: Use double precision; increase iteration count
- **Divergence**: Check that initial guess is within convergence basin
