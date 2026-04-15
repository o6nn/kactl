---
name: "combinatorics"
description: "Technique for counting, arranging, and selecting objects."
---

# Combinatorics

Technique for counting, arranging, and selecting objects.

## Sub-techniques

- Computation of binomial coefficients — Use `content/number-theory/ModInverse.h` for precomputed factorials (cross-ref)
- Pigeon-hole principle — Theoretical technique, no dedicated implementation
- Inclusion/exclusion — Theoretical technique, no dedicated implementation
- Catalan number — Theoretical technique, no dedicated implementation
- Pick's theorem — Theoretical technique, no dedicated implementation

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

## Available Implementations

| Algorithm | File | Time | Description |
|-----------|------|------|-------------|
| Integer Permutation | `content/combinatorial/IntPerm.h` | O(n) | Permutation ↔ integer conversion (not order preserving) |
| Multinomial | `content/combinatorial/multinomial.h` | — | Computes multinomial coefficients |

### Additional Resources

- `content/combinatorial/factorial.tex` — Mathematical formulas for factorials, derangements, Stirling numbers, etc.

### Cross-references

- `content/number-theory/ModInverse.h` — Precomputed modular inverses for binomial coefficients (see also: number-theory skill)
- `content/number-theory/ModPow.h` — Modular exponentiation for combinatorial computations (see also: number-theory skill)
- `content/numerical/FastSubsetTransform.h` — Subset convolution for inclusion-exclusion (see also: numerical-methods skill)

### Old Unit Tests

- `test_multinomial`

## Troubleshooting

- **Wrong answer**: Check for overcounting or undercounting; verify modular arithmetic
- **Overflow**: Use modular arithmetic throughout the computation
- **TLE**: Precompute combinatorial values; use efficient formulas
