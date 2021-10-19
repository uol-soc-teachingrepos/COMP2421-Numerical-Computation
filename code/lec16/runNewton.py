""" runNewton.py

runs newton function defined in nonlinearSolve.py on nonlinear
functions and derivatives found in file nonlinear_functions.py

To use:

python runNewton.py fnon dfnon x0 tol

Example calls:

python runNewton.py sqrt2 dsqrt2 1 0.0001

python runNewton.py naca0012 dnaca0012 1 0.0001

python runNewton.py naca0012 dnaca0012 0.1 0.0001


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
    if argv[1] not in members.keys() or argv[2] not in members.keys():
        cout = (
            "Warning: One or more input functions not found in "
            "nonlinear_function.py. \nPlease ensure that these "
            "files are defined."
        )
        print(cout)
        return 1

    print("Running Newton method on nonlinear function: " + argv[1])
    print("With parameters (x0 tol): ", argv[3:])

    fnon = members[argv[1]]
    dfnon = members[argv[2]]
    num_params = list(map(float, argv[3:]))
    newton(fnon, dfnon, num_params[0], num_params[1])


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("WARNING: not enough arguments passed")
        print(__doc__)

        print("continuing with default parameters instead...")
        main([sys.argv[0], "sqrt2", "dsqrt2", "1.0", "0.001"])
    else:
        main(sys.argv)
