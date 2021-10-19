""" runModifiedNewton.py

runs modified_newton function defined in nonlinearSolve.py on
nonlinear functions found in file nonlinear_functions.py

To use:

python runModifiedNewton.py fnon x0 tol

Example calls:

python runModifiedNewton.py sqrt2 1 0.0001

python runModifiedNewton.py naca0012 1 0.0001

python runModifiedNewton.py naca0012 0.1 0.0001

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
    if argv[1] not in members.keys():
        cout = """
Warning: Input function not found in nonlinear_functions.py.
Please ensure that these files are defined.
"""
        print(cout)
        return 1

    print("Running modified Newton method on nonlinear function: " + argv[1])
    print("With parameters (x0 tol): ", argv[2:])

    fnon = members[argv[1]]
    num_params = list(map(float, argv[2:]))
    modified_newton(fnon, num_params[0], num_params[1])


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("WARNING: not enough arguments passed")
        print(__doc__)

        print("continuing with default parameters instead...")
        main([sys.argv[0], "sqrt2", "1.4", "0.0001"])
    else:
        main(sys.argv)
