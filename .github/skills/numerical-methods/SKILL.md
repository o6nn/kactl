---
name: "numerical-methods"
description: "Technique for solving mathematical problems using numerical approximation."
---

# Numerical Methods

Technique for solving mathematical problems using numerical approximation.

## Sub-techniques

- Numeric integration
- Newton's method
- Root-finding with binary/ternary search
- Golden section search

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

## Troubleshooting

- **Wrong answer**: Check convergence tolerance; verify initial conditions
- **TLE**: Reduce number of iterations; use faster converging methods
- **Precision errors**: Use double precision; increase iteration count
- **Divergence**: Check that initial guess is within convergence basin
