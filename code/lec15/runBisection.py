"""
runBisection.py

runs bisection function on nonlinear functions found in file 
nonlinear_functions.py

To use:

python runBisection.py fnon xL xR tol

Example calls:

python runBisection.py naca0012 0.5 1.0 0.0001

python runBisection.py compound 1 10000 0.1

python runBisection.py sqrt2 0 2 0.0001


"""

# Python modules
import sys

# Comp2941 modules
sys.path.append("..")
from numericalSolve import *
from nonlinear_functions import *


def main(argv):
    print("Running bisection on nonlinear function: " + argv[1])
    print("With parameters: ", argv[2:])

    mode = argv[1]
    num_params = list(map(float, argv[2:]))

    if mode == "naca0012":
        x, f = bisection(naca0012, num_params[0], num_params[1], num_params[2])
    elif mode == "compound":
        x, f = bisection(compound, num_params[0], num_params[1], num_params[2])
    elif mode == "sqrt2":
        x, f = bisection(sqrt2, num_params[0], num_params[1], num_params[2])

    print(f"solution: x = {x}, f = {f}")


if __name__ == "__main__":
    main(sys.argv)
