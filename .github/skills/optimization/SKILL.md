---
name: "optimization"
description: "Technique for finding optimal values of functions."
---

# Optimization

Technique for finding optimal values of functions.

## Sub-techniques

- Binary search
- Ternary search → `content/various/TernarySearch.h`
- Unimodality and convex functions → `content/numerical/GoldenSectionSearch.h`, `content/numerical/HillClimbing.h`
- Binary search on derivative — no dedicated implementation (conceptual pattern)

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

## Available Implementations

| Algorithm | File | Time | Description |
|-----------|------|------|-------------|
| Ternary Search | `content/various/TernarySearch.h` | O(log(b-a)) | Discrete ternary search for unimodal function |
| Golden Section Search | `content/numerical/GoldenSectionSearch.h` | O(log((b-a)/ε)) | Minimizes unimodal function on continuous interval |
| Hill Climbing | `content/numerical/HillClimbing.h` | — | Simple optimization for unimodal functions |
| Simplex | `content/numerical/Simplex.h` | — | Linear programming: maximize c^T x subject to Ax ≤ b, x ≥ 0 |

### Cross-references

- `content/number-theory/FracBinarySearch.h` — Binary search on fractions p/q (see also: number-theory skill)
- `content/various/ConstantIntervals.h` — Splits monotone function into constant intervals (see also: sweeping skill)

### Old unit tests

- goldenSectionSearch

## Troubleshooting

- **Wrong answer**: Verify the function is monotonic/unimodal; check boundary conditions
- **TLE**: Ensure convergence criteria are not too tight
- **Precision errors**: Use sufficient iterations; consider epsilon-based termination
