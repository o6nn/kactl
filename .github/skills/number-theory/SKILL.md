---
name: "number-theory"
description: "Technique for solving problems involving properties of integers."
---

# Number Theory

Technique for solving problems involving properties of integers.

## Sub-techniques

- Integer parts
- Divisibility
- Euclidean algorithm
- Modular arithmetic
  - Modular multiplication
  - Modular inverses
  - Modular exponentiation by squaring
- Chinese remainder theorem
- Fermat's little theorem
- Euler's theorem
- Phi function
- Frobenius number
- Quadratic reciprocity
- Pollard-Rho
- Miller-Rabin
- Hensel lifting
- Vieta root jumping

## When to Use

- Problems involving divisibility, primes, or modular arithmetic
- Cryptography-related problems
- GCD/LCM computations
- Problems requiring modular inverses or exponentiation

## Key Considerations

- Use modular arithmetic to prevent overflow
- Choose appropriate primality testing (Miller-Rabin for large numbers)
- Precompute primes with sieve for range queries
- Handle edge cases with 0, 1, and negative numbers

## Troubleshooting

- **Wrong answer**: Check modular arithmetic operations; verify GCD edge cases
- **Overflow**: Use 128-bit or modular multiplication for large numbers
- **TLE**: Use efficient algorithms (binary exponentiation, sieve)
- **Division by zero**: Check for mod 0 cases
