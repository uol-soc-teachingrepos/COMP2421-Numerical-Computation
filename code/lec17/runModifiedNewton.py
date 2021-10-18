"""
TODO doc me
"""
# Python modules
import sys

# Comp2941 modules
sys.path.append("..")
from numericalSolve import *
from nonlinear_functions import *


if __name__ == "__main__":
    print("\n\n--- sqrt2, 1, 1.0e-12")
    modified_newton(sqrt2, 1, 1.0e-12)
    print("\n\n--- naca0012, 1, 1.0e-4")
    modified_newton(naca0012, 1, 1.0e-4)
    print("\n\n--- naca0012, 1, 1.0e-5")
    modified_newton(naca0012, 1, 1.0e-5)
    print("\n\n--- naca0012, 0.1, 1.0e-4")
    modified_newton(naca0012, 0.1, 1.0e-4)
