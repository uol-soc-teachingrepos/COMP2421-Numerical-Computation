"""
TODO doc me
"""

# Python modules
import inspect
import sys

# Comp2941 modules
sys.path.append("..")
from numericalSolve import *
import nonlinear_functions


def main(argv):
    members = dict(inspect.getmembers(nonlinear_functions, inspect.isfunction))
    if argv[1] not in members.keys() or argv[2] not in members.keys():
        cout = (
            "Warning: One or more input functions not found in "
            "nonlinear_function.py. \nPlease ensure that these "
            "files are defined."
        )
        print(cout)
        print(members.keys())
        return 1

    print("Running difference method on nonlinear function: " + argv[1])
    print("With parameters (x0): ", argv[3:])

    fnon = members[argv[1]]
    dfnon = members[argv[2]]
    num_params = list(map(float, argv[3:]))
    make_table(fnon, dfnon, num_params[0])


def make_table(f, df, x0):
    # table header
    print("dx      approx       abs error  rel error")
    print("------- ------------ ---------- ----------")

    for dx in [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14, 1e-16]:
        # get approximation and errors
        approx, abs_error = difference(f, df, x0, dx)
        rel_error = abs_error / abs(x0)

        # print table row
        print(f"{dx:.1e} {approx:.10f} {abs_error:.4e} {rel_error:.4e}")


if __name__ == "__main__":
    main(sys.argv)
