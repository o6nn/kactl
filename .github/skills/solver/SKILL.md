---
name: "solver"
description: "Skill for symbolically and numerically verifying algorithmic solutions using external solver backends."
---

# Solver / Verifier

Skill for verifying algorithmic solutions using computer algebra systems, numerical libraries, and (optionally) formal proof assistants.

## Purpose

The troubleshooter and Copilot agent can generate algorithms and code, but LLMs sometimes hallucinate incorrect math or buggy implementations. This skill provides **external verification** by running the same problem through a trusted solver backend and comparing results.

## When to Use

- Verifying a newly generated algorithm produces correct output
- Cross-checking a C++ numerical implementation against a reference solver
- Symbolically simplifying or solving a mathematical equation
- Confirming edge cases (singular matrices, degenerate inputs, boundary conditions)
- Validating that an optimization finds the true optimum

## Available Backends (tiered by integration effort)

### Tier 1 — Zero-install (Python standard ecosystem)

| Backend | Capabilities | Install | Best For |
|---------|-------------|---------|----------|
| **SymPy** | Symbolic math, equation solving, matrix algebra, simplification | `pip install sympy` | Verifying closed-form solutions, symbolic matrix equations |
| **NumPy** | Numerical linear algebra, random test generation | `pip install numpy` | Generating test cases, numerical spot-checks |
| **SciPy** | Specialized solvers (Sylvester, Lyapunov, Riccati, ODE, optimization) | `pip install scipy` | Reference solutions for matrix equations, optimization |

These are the **recommended** backends — they require no API keys, install in seconds, and cover the vast majority of verification needs for a competitive programming library.

### Tier 2 — API-based (requires secrets)

| Backend | Capabilities | Integration | Best For |
|---------|-------------|-------------|----------|
| **Wolfram Cloud API** | Full Wolfram Language: symbolic math, number theory, graph theory | REST API, needs `WOLFRAM_APP_ID` secret | Problems beyond SymPy's reach (e.g., holonomic functions, advanced combinatorics) |
| **SageMath (CoCalc API)** | Open-source CAS, algebraic geometry, number theory | REST API or `apt install sagemath` (~2GB) | When SymPy lacks a specific algorithm |

### Tier 3 — Proof assistants (heavy, for formal verification)

| Backend | Capabilities | Integration | Best For |
|---------|-------------|-------------|----------|
| **Lean4** | Formal proofs of algorithm correctness | ~1GB install, `elan` toolchain | Proving loop invariants, termination, correctness theorems |
| **Coq** | Formal verification, certified extraction | `apt install coq` (~500MB) | Extracting verified implementations |
| **Prover9/Mace4** | First-order automated theorem proving / model finding | Lightweight binary | Equational reasoning, finding counterexamples |

> **Note:** Tier 3 backends are not recommended for routine use. They are included for completeness and for cases where formal correctness guarantees are needed (e.g., verifying a novel algorithm before adding to KACTL).

## Verification Script

The solver skill uses `.github/scripts/verify_solution.py` to run verification. It supports several problem types:

### Usage

```bash
pip install sympy numpy scipy
python .github/scripts/verify_solution.py --problem sylvester --size 4
python .github/scripts/verify_solution.py --problem linear_system --size 5
python .github/scripts/verify_solution.py --problem determinant --size 3
python .github/scripts/verify_solution.py --problem matrix_inverse --size 3
```

### Supported Problem Types

| Problem | What It Verifies | Reference Solver |
|---------|-----------------|-----------------|
| `sylvester` | Sylvester equation AX + XB = C | `scipy.linalg.solve_sylvester` |
| `linear_system` | Linear system Ax = b | `numpy.linalg.solve` |
| `determinant` | Matrix determinant | `numpy.linalg.det` |
| `matrix_inverse` | Matrix inverse | `numpy.linalg.inv` |

### Adding New Problem Types

To add verification for a new algorithm:
1. Add a new function in `verify_solution.py` following the existing pattern.
2. Register it in the `VERIFIERS` dict.
3. Update this skill file with the new problem type.

## Workflow Integration

The troubleshooter workflow automatically selects this skill when the problem description contains keywords like: `verify`, `prove`, `check`, `solve`, `symbolic`, `numerical`, `correct`, `validate`.

When selected, it adds a verification step that:
1. Installs Python + SymPy + SciPy in the workflow runner.
2. Runs `verify_solution.py` for any applicable problem types.
3. Reports pass/fail results back to the issue.

## Cross-references

- **matrices** skill — Matrix-related verifications (determinant, inverse, Sylvester, linear systems)
- **numerical-methods** skill — Numerical algorithm verifications (integration, optimization, FFT)
- **optimization** skill — Optimization result verification (Simplex, golden section)

## Troubleshooting

- **SymPy too slow**: Symbolic verification can be slow for large matrices (n > 10). Use NumPy/SciPy numerical verification instead.
- **SciPy missing a solver**: Check if the solver exists in `scipy.linalg` or `scipy.optimize`. If not, fall back to SymPy or Wolfram.
- **Numerical precision mismatch**: Use `numpy.allclose(a, b, atol=1e-9)` rather than exact equality for floating-point comparisons.
- **Verification passes but C++ fails**: The algorithm is correct but the C++ implementation has a bug — check indexing, precision, or overflow.
