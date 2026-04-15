---
name: "optimization"
description: "Technique for finding optimal values of functions."
---

# Optimization

Technique for finding optimal values of functions.

## Sub-techniques

- Binary search
- Ternary search
- Unimodality and convex functions
- Binary search on derivative

## When to Use

- Finding the minimum or maximum of a function
- Searching for a threshold or boundary value
- Problems with monotonic or unimodal properties
- Parametric search problems

## Key Considerations

- Verify monotonicity before applying binary search
- Verify unimodality before applying ternary search
- Handle floating-point precision in continuous search
- Choose appropriate convergence criteria

## Troubleshooting

- **Wrong answer**: Verify the function is monotonic/unimodal; check boundary conditions
- **TLE**: Ensure convergence criteria are not too tight
- **Precision errors**: Use sufficient iterations; consider epsilon-based termination
