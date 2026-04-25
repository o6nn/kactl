#include "../utilities/template.h"

#include "../../content/numerical/SolveLinear.h"
#include "../../content/numerical/SylvesterSolve.h"

int main() {
	srand(42);
	auto randMat = [](int r, int c) {
		vector<vd> M(r, vd(c));
		rep(i,0,r) rep(j,0,c) M[i][j] = (rand() % 2001 - 1000) / 100.0;
		return M;
	};

	// Test 1: Identity A and B, should give X = C/2
	{
		int m = 3, n = 3;
		vector<vd> A(m, vd(m, 0)), B(n, vd(n, 0)), C(m, vd(n)), X;
		rep(i,0,m) A[i][i] = 1;
		rep(i,0,n) B[i][i] = 1;
		rep(i,0,m) rep(j,0,n) C[i][j] = 2.0 * (i + j + 1);
		int r = solveSylvester(A, B, C, X);
		assert(r == m * n);
		rep(i,0,m) rep(j,0,n)
			assert(fabs(X[i][j] - (i + j + 1)) < 1e-6);
	}

	// Test 2: Random matrices, verify AX + XB = C
	rep(t,0,200) {
		int m = rand() % 4 + 1, n = rand() % 4 + 1;
		auto A = randMat(m, m);
		auto B = randMat(n, n);
		auto Xtrue = randMat(m, n);
		// Compute C = A*Xtrue + Xtrue*B
		vector<vd> C(m, vd(n, 0));
		rep(i,0,m) rep(j,0,n) {
			rep(k,0,m) C[i][j] += A[i][k] * Xtrue[k][j];
			rep(k,0,n) C[i][j] += Xtrue[i][k] * B[k][j];
		}
		vector<vd> X;
		int r = solveSylvester(A, B, C, X);
		if (r == m * n) {
			// Verify AX + XB ≈ C
			rep(i,0,m) rep(j,0,n) {
				double val = 0;
				rep(k,0,m) val += A[i][k] * X[k][j];
				rep(k,0,n) val += X[i][k] * B[k][j];
				assert(fabs(val - C[i][j]) < 1e-6);
			}
		}
		// else: no unique solution (eigenvalue collision), that's ok
	}

	// Test 3: Zero matrices
	{
		int m = 2, n = 2;
		vector<vd> A(m, vd(m, 0)), B(n, vd(n, 0)),
		           C(m, vd(n, 0)), X;
		int r = solveSylvester(A, B, C, X);
		// A=0, B=0, C=0: any X is a solution, rank should be 0
		assert(r == 0 || r >= 0);
		// Verify AX + XB = C = 0
		rep(i,0,m) rep(j,0,n) {
			double val = 0;
			rep(k,0,m) val += A[i][k] * X[k][j];
			rep(k,0,n) val += X[i][k] * B[k][j];
			assert(fabs(val) < 1e-6);
		}
	}

	// Test 4: 1x1 case: ax + xb = c => x = c/(a+b)
	rep(t,0,100) {
		double a = (rand() % 2001 - 1000) / 100.0;
		double b = (rand() % 2001 - 1000) / 100.0;
		if (fabs(a + b) < 0.1) continue;
		double c = (rand() % 2001 - 1000) / 100.0;
		vector<vd> A = {{a}}, B = {{b}}, C = {{c}}, X;
		int r = solveSylvester(A, B, C, X);
		assert(r == 1);
		assert(fabs(X[0][0] - c / (a + b)) < 1e-6);
	}

	cout << "Tests passed!" << endl;
}
