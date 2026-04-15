---
name: "probability-theory"
description: "Technique for solving problems involving randomness and expected values."
---

# Probability Theory

Technique for solving problems involving randomness and expected values.

## When to Use

- Problems involving expected values
- Random processes and Markov chains
- Probabilistic analysis of algorithms
- Problems requiring probability calculations

## Key Considerations

- Use linearity of expectation to simplify calculations
- Handle floating-point precision carefully
- Consider using fractions or modular arithmetic for exact probability
- Model state transitions for Markov chain problems

## Available Implementations

No standalone probability theory implementations exist in the KACTL codebase. Probability problems in competitive programming typically use dynamic programming over states or matrix exponentiation for Markov chains.

### Cross-references

These implementations from other categories are commonly used in probability problems:
- `content/numerical/LinearRecurrence.h` — Compute k'th term of linear recurrence, useful for Markov chain steady-state, O(n² log k) (see also: numerical-methods skill)
- `content/data-structures/Matrix.h` — Matrix exponentiation for transition matrices (see also: matrices skill)
- `content/numerical/Integrate.h` — Numerical integration for continuous probability distributions (see also: numerical-methods skill)
- `content/numerical/IntegrateAdaptive.h` — Adaptive integration for complex probability density functions (see also: numerical-methods skill)
- `content/various/KnuthDP.h` — DP optimization for probability-related interval computations, O(N²) (see also: dynamic-programming skill)

## Troubleshooting

- **Wrong answer**: Check probability calculations; verify independence assumptions
- **Precision errors**: Use sufficient decimal places or exact arithmetic
- **TLE**: Simplify probability model; use DP over states
