---
name: "combinatorics"
description: "Technique for counting, arranging, and selecting objects."
---

# Combinatorics

Technique for counting, arranging, and selecting objects.

## Sub-techniques

- Computation of binomial coefficients
- Pigeon-hole principle
- Inclusion/exclusion
- Catalan number
- Pick's theorem

## When to Use

- Counting the number of ways to arrange or select objects
- Problems involving permutations and combinations
- Lattice point counting
- Problems requiring inclusion-exclusion principle

## Key Considerations

- Use modular arithmetic to prevent overflow in counting problems
- Precompute factorials and inverse factorials for efficient binomial coefficients
- Apply inclusion-exclusion carefully for overcounting
- Recognize Catalan number patterns (balanced parentheses, binary trees, etc.)

## Troubleshooting

- **Wrong answer**: Check for overcounting or undercounting; verify modular arithmetic
- **Overflow**: Use modular arithmetic throughout the computation
- **TLE**: Precompute combinatorial values; use efficient formulas
