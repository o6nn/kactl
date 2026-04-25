/**
 * Author: KACTL contributors
 * Date: 2026-04-15
 * License: CC0
 * Description: Solves the Sylvester equation $AX + XB = C$ where
 *  $A$ is $m \times m$, $B$ is $n \times n$, $C$ is $m \times n$,
 *  and $X$ is the $m \times n$ unknown matrix.
 *  Uses Kronecker product reduction to $(I_n \otimes A + B^T \otimes I_m)\text{vec}(X) = \text{vec}(C)$,
 *  then solves via Gaussian elimination.
 *  A unique solution exists iff $A$ and $-B$ share no eigenvalues.
 *  Returns rank of the system, or -1 if no solution.
 *  Data in $A$, $B$, $C$ is preserved.
 * Time: O(m^3 n^3)
 * Status: stress-tested
 */
#pragma once

#include "SolveLinear.h"

int solveSylvester(vector<vd>& A, vector<vd>& B, vector<vd>& C,
                   vector<vd>& X) {
	int m = sz(A), n = sz(B);
	assert(m && n);
	assert(sz(A[0]) == m && sz(B[0]) == n);
	assert(sz(C) == m && sz(C[0]) == n);
	int mn = m * n;
	// Build K = (I_n ⊗ A) + (B^T ⊗ I_m), size mn × mn
	// K[i*m+r][j*m+s] = A[r][s]*(i==j) + B[j][i]*(r==s)
	vector<vd> K(mn, vd(mn, 0));
	rep(i,0,n) rep(j,0,n) rep(r,0,m) rep(s,0,m) {
		K[i*m+r][j*m+s] = A[r][s] * (i == j) + B[j][i] * (r == s);
	}
	// vec(C): column-major vectorization
	vd c(mn), x(mn);
	rep(i,0,n) rep(r,0,m) c[i*m+r] = C[r][i];

	int rank = solveLinear(K, c, x);
	// Unpack x into X
	X.assign(m, vd(n, 0));
	if (rank >= 0) {
		rep(i,0,n) rep(r,0,m) X[r][i] = x[i*m+r];
	}
	return rank;
}
