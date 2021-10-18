"""
TODO doc me
"""
# Python modules
import numpy as np
import sys

# Comp2941 modules
sys.path.append("..")
from numericalSolve import *
from nonlinear_functions import *

if __name__ == "__main__":
    fzero(sqrt2, 1.0, tolx=1.0e-12, tolfun=1.0e-12)

    eps = np.finfo(float).eps
    fzero(sqrt2, 1.0, 2.0, tolx=eps, tolfun=eps)

    fzero(compound, 200, 300, tolx=1.0e-3, tolfun=1.0e-12)

    fzero(naca0012, 0.5, 1.0, tolx=1.0e-12, tolfun=1.0e-12)

    fzero(naca0012, 0.0, 0.5, tolx=1.0e-12, tolfun=1.0e-12)
