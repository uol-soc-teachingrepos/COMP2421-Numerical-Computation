""" runBisection.py

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
from nonlinear_functions import *
from nonlinearSolve import *


def main(argv):
    print("Running bisection on nonlinear function: " + argv[1])
    print("With parameters: ", argv[2:])

    mode = argv[1]
    num_params = list(map(float, argv[2:]))

    if mode == "naca0012":
        bisection(naca0012, num_params[0], num_params[1], num_params[2])
    elif mode == "compound":
        bisection(compound, num_params[0], num_params[1], num_params[2])
    elif mode == "sqrt2":
        bisection(sqrt2, num_params[0], num_params[1], num_params[2])


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("WARNING: not enough arguments passed")
        print(__doc__)

        print("continuing with default parameters instead...")
        main([sys.argv[0], "naca0012", "0.5", "1.0", "0.0001"])
    else:
        main(sys.argv)
