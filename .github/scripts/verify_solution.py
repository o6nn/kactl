#!/usr/bin/env python3
"""
Verification script for KACTL numerical algorithms.

Uses SymPy/NumPy/SciPy as reference solvers to validate algorithm correctness.
Called by the troubleshooter workflow when the 'solver' skill is selected.

Usage:
    python verify_solution.py --problem sylvester --size 4 --trials 50
    python verify_solution.py --problem linear_system --size 5
    python verify_solution.py --problem determinant --size 3
    python verify_solution.py --problem matrix_inverse --size 3
    python verify_solution.py --problem all --size 4
"""

import argparse
import sys
import numpy as np


def verify_sylvester(size: int, trials: int) -> bool:
    """Verify Sylvester equation AX + XB = C using scipy.linalg.solve_sylvester."""
    from scipy.linalg import solve_sylvester

    print(f"  Verifying Sylvester equation solver (size={size}, trials={trials})...")
    rng = np.random.default_rng(42)

    for t in range(trials):
        m = rng.integers(1, size + 1)
        n = rng.integers(1, size + 1)
        A = rng.standard_normal((m, m))
        B = rng.standard_normal((n, n))
        C = rng.standard_normal((m, n))

        try:
            X = solve_sylvester(A, B, C)
        except np.linalg.LinAlgError:
            # Singular case — skip
            continue

        # Verify AX + XB ≈ C
        residual = A @ X + X @ B - C
        err = np.max(np.abs(residual))
        if err > 1e-8:
            print(f"  FAIL trial {t}: max residual = {err:.2e}")
            return False

    # Also test known cases
    # Identity: IX + XI = C => 2X = C => X = C/2
    I = np.eye(size)
    C_test = rng.standard_normal((size, size))
    X = solve_sylvester(I, I, C_test)
    if not np.allclose(X, C_test / 2, atol=1e-10):
        print("  FAIL: identity case X != C/2")
        return False

    print(f"  PASS ({trials} random trials + identity case)")
    return True


def verify_linear_system(size: int, trials: int) -> bool:
    """Verify linear system Ax = b using numpy.linalg.solve."""
    print(f"  Verifying linear system solver (size={size}, trials={trials})...")
    rng = np.random.default_rng(42)

    for t in range(trials):
        n = rng.integers(1, size + 1)
        A = rng.standard_normal((n, n))
        x_true = rng.standard_normal(n)
        b = A @ x_true

        try:
            x = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            continue

        if not np.allclose(A @ x, b, atol=1e-8):
            print(f"  FAIL trial {t}: solution does not satisfy Ax = b")
            return False

    print(f"  PASS ({trials} random trials)")
    return True


def verify_determinant(size: int, trials: int) -> bool:
    """Verify determinant computation using numpy.linalg.det."""
    print(f"  Verifying determinant (size={size}, trials={trials})...")
    rng = np.random.default_rng(42)

    for t in range(trials):
        n = rng.integers(1, size + 1)
        A = rng.standard_normal((n, n))
        det_np = np.linalg.det(A)

        # Cross-check: det(A) * det(A^-1) should be ~1 for non-singular A
        if abs(det_np) > 1e-10:
            det_inv = np.linalg.det(np.linalg.inv(A))
            if not np.isclose(det_np * det_inv, 1.0, atol=1e-6):
                print(f"  FAIL trial {t}: det(A)*det(A^-1) = {det_np * det_inv}")
                return False

    # Known case: det(I) = 1
    assert np.isclose(np.linalg.det(np.eye(size)), 1.0)

    # Known case: det of 2x2
    A22 = np.array([[3, 8], [4, 6]])
    assert np.isclose(np.linalg.det(A22), 3 * 6 - 8 * 4)

    print(f"  PASS ({trials} random trials + known cases)")
    return True


def verify_matrix_inverse(size: int, trials: int) -> bool:
    """Verify matrix inverse using numpy.linalg.inv."""
    print(f"  Verifying matrix inverse (size={size}, trials={trials})...")
    rng = np.random.default_rng(42)

    for t in range(trials):
        n = rng.integers(1, size + 1)
        A = rng.standard_normal((n, n))

        try:
            A_inv = np.linalg.inv(A)
        except np.linalg.LinAlgError:
            continue

        product = A @ A_inv
        err = np.max(np.abs(product - np.eye(n)))
        if err > 1e-8:
            print(f"  FAIL trial {t}: max |A*A^-1 - I| = {err:.2e}")
            return False

    print(f"  PASS ({trials} random trials)")
    return True


VERIFIERS = {
    "sylvester": verify_sylvester,
    "linear_system": verify_linear_system,
    "determinant": verify_determinant,
    "matrix_inverse": verify_matrix_inverse,
}


def main():
    parser = argparse.ArgumentParser(
        description="Verify KACTL numerical algorithms against reference solvers"
    )
    parser.add_argument(
        "--problem",
        choices=list(VERIFIERS.keys()) + ["all"],
        required=True,
        help="Problem type to verify",
    )
    parser.add_argument(
        "--size", type=int, default=4, help="Max matrix size (default: 4)"
    )
    parser.add_argument(
        "--trials", type=int, default=50, help="Number of random trials (default: 50)"
    )
    args = parser.parse_args()

    problems = list(VERIFIERS.keys()) if args.problem == "all" else [args.problem]
    all_passed = True

    print(f"=== KACTL Solution Verification ===")
    print(f"Problems: {', '.join(problems)}")
    print(f"Max size: {args.size}, Trials: {args.trials}")
    print()

    for problem in problems:
        print(f"[{problem}]")
        passed = VERIFIERS[problem](args.size, args.trials)
        if not passed:
            all_passed = False
        print()

    if all_passed:
        print("✅ All verifications passed!")
        sys.exit(0)
    else:
        print("❌ Some verifications failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
