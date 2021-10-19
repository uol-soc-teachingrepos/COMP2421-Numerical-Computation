""" LeastSquaresTest.py

Solve the problem of fitting a quadratic polynomial to a given set of
data using least squares approximation.
"""

# Python modules
import sys

import numpy as np

# Comp2941 modules
sys.path.append("..")
from matrixSolve import *

# Fix the matrix dimension.
m = 5
n = 3

# Insert an example 5x3 matrix from the overdetermined system.
A = np.array(
    [
        [1.0, -1.0, 1.0],
        [1.0, -0.5, 0.25],
        [1.0, 0.0, 0.0],
        [1.0, 0.5, 0.25],
        [1.0, 1.0, 1.0],
    ]
)

# Insert an example column 5-vector for the right hand side.
b = np.array([[1.0], [0.5], [0.0], [0.5], [2.0]])

ATA = np.dot(A.T, A)
ATb = np.dot(A.T, b)

# Reduce  A' A x = A' b  to upper triangular form
[ATA, ATb] = gauss_elimination(ATA, ATb)
# Solve the resulting upper triangular system
x = upper_triangular_solve(ATA, ATb)

print(f"x = {x}")

# Calculate the residual.
r = b - np.dot(A, x)

# Calculate the norm of the residual.
norm = np.sqrt(np.dot(r.T, r))

print(f"\n||r||= {norm}")
