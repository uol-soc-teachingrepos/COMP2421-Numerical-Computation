""" runSecant.py

runs secant function on nonlinear functions and derivatives found in
file nonlinear_functions.py

To use:

python runSecant.py fnon x0 x1 tol

Example calls:

python runSecant.py sqrt2 1.4 1.5 0.0001

"""

# Python modules
import inspect
import sys

# Comp2941 modules
sys.path.append("..")
import nonlinear_functions
from nonlinearSolve import *


def main(argv):
    members = dict(inspect.getmembers(nonlinear_functions, inspect.isfunction))
    if argv[1] not in members:
        cout = (
            "Warning: One or more input functions not found in "
            "nonlinear_function.py. \nPlease ensure that these "
            "files are defined."
        )
        print(cout)
        return 0

    print("Running Secant method on nonlinear function: " + argv[1])
    print("With parameters (x0 x1 tol): ", argv[2:])

    fnon = members[argv[1]]
    num_params = list(map(float, argv[2:]))
    secant(fnon, num_params[0], num_params[1], num_params[2])


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("WARNING: not enough arguments passed")
        print(__doc__)

        print("continuing with default parameters instead...")
        main([sys.argv[0], "sqrt2", "1.4", "1.5", "0.0001"])
    else:
        main(sys.argv)
