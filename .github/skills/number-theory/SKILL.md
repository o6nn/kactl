---
name: "number-theory"
description: "Technique for solving problems involving properties of integers."
---

# Number Theory

Technique for solving problems involving properties of integers.

## Sub-techniques

- Integer parts
- Divisibility
- Euclidean algorithm — [`content/number-theory/euclid.h`](../../../content/number-theory/euclid.h)
- Modular arithmetic — [`content/number-theory/ModularArithmetic.h`](../../../content/number-theory/ModularArithmetic.h)
  - Modular multiplication — [`content/number-theory/ModMulLL.h`](../../../content/number-theory/ModMulLL.h)
  - Modular inverses — [`content/number-theory/ModInverse.h`](../../../content/number-theory/ModInverse.h)
  - Modular exponentiation by squaring — [`content/number-theory/ModPow.h`](../../../content/number-theory/ModPow.h)
- Chinese remainder theorem — [`content/number-theory/CRT.h`](../../../content/number-theory/CRT.h)
- Fermat's little theorem
- Euler's theorem
- Phi function — [`content/number-theory/phiFunction.h`](../../../content/number-theory/phiFunction.h)
- Frobenius number
- Quadratic reciprocity
- Pollard-Rho — [`content/number-theory/Factor.h`](../../../content/number-theory/Factor.h)
- Miller-Rabin — [`content/number-theory/MillerRabin.h`](../../../content/number-theory/MillerRabin.h)
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

## Available Implementations

### Modular Arithmetic

| Algorithm | File | Time | Description | Stress Test |
|-----------|------|------|-------------|-------------|
| Modular Arithmetic | [`ModularArithmetic.h`](../../../content/number-theory/ModularArithmetic.h) | — | Operators for modular arithmetic | ✅ |
| Modular Inverse | [`ModInverse.h`](../../../content/number-theory/ModInverse.h) | — | Pre-computes modular inverses (prime mod) | ✅ |
| Modular Exponentiation | [`ModPow.h`](../../../content/number-theory/ModPow.h) | O(log b) | Fast modular exponentiation | — |
| Discrete Logarithm | [`ModLog.h`](../../../content/number-theory/ModLog.h) | O(√m) | Baby-step giant-step: smallest x where a^x ≡ b (mod m) | ✅ |
| Modular Sum | [`ModSum.h`](../../../content/number-theory/ModSum.h) | O(log m) | Sums of mod'ed arithmetic progressions | ✅ |
| Modular Multiply (128-bit) | [`ModMulLL.h`](../../../content/number-theory/ModMulLL.h) | O(1) | a·b mod c for values up to 7.2×10¹⁸ | ✅ |
| Modular Square Root | [`ModSqrt.h`](../../../content/number-theory/ModSqrt.h) | O(log² p) | Tonelli-Shanks algorithm | ✅ |

### Primality & Factorization

| Algorithm | File | Time | Description | Stress Test |
|-----------|------|------|-------------|-------------|
| Fast Sieve | [`FastEratosthenes.h`](../../../content/number-theory/FastEratosthenes.h) | — | Segmented sieve, ~1.5s for 10⁹ | — |
| Simple Sieve | [`Eratosthenes.h`](../../../content/number-theory/Eratosthenes.h) | — | Eratosthenes sieve, ~0.8s for 10⁸ | ✅ |
| Miller-Rabin | [`MillerRabin.h`](../../../content/number-theory/MillerRabin.h) | — | Deterministic primality test up to 7×10¹⁸ | ✅ |
| Pollard-Rho | [`Factor.h`](../../../content/number-theory/Factor.h) | O(n^(1/4)) | Fast integer factorization | ✅ |

### GCD & Number-Theoretic Functions

| Algorithm | File | Time | Description | Stress Test |
|-----------|------|------|-------------|-------------|
| Extended GCD | [`euclid.h`](../../../content/number-theory/euclid.h) | — | Finds x,y where ax+by=gcd(a,b) | — |
| Chinese Remainder Theorem | [`CRT.h`](../../../content/number-theory/CRT.h) | O(log n) | Solves system of congruences | ✅ |
| Continued Fractions | [`ContinuedFractions.h`](../../../content/number-theory/ContinuedFractions.h) | O(log N) | Best rational approximation | ✅ |
| Fraction Binary Search | [`FracBinarySearch.h`](../../../content/number-theory/FracBinarySearch.h) | O(log N) | Smallest fraction p/q satisfying condition | ✅ |
| Euler's Totient | [`phiFunction.h`](../../../content/number-theory/phiFunction.h) | — | Computes φ(n) | — |

## Troubleshooting

- **Wrong answer**: Check modular arithmetic operations; verify GCD edge cases
- **Overflow**: Use 128-bit or modular multiplication for large numbers
- **TLE**: Use efficient algorithms (binary exponentiation, sieve)
- **Division by zero**: Check for mod 0 cases
