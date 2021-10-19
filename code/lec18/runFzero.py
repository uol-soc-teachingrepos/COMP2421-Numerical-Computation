""" runFzero.py

runs fzero defined in nonlinearSolve.py on nonlinear functions found
in file nonlinear_functions.py

To use:

python runFzero.py fnon x0 [options]

where optional parameters are: x1, tolx, tolfun, maxiter, verbose and
should be passed as option=value

Example

python runFzero.py sqrt2 1.0 tolx=1.0e-14

"""

# python modules
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

    # extract parameters
    fnon = members[argv[1]]
    x0 = float(argv[2])

    opt = {
        "x1": None,
        "tolx": 1.0e-4,
        "tolfun": 1.0e-4,
        "maxiter": 100,
        "verbose": True,
    }
    map = {"x1": float, "tolx": float, "tolfun": float, "maxiter": int, "verbose": bool}
    for arg in argv[3:]:
        o, a = arg.split("=")
        opt[o] = map[o](a)

    print("Running fzero method on nonlinear function: " + argv[1])
    print("With parameter x0: ", argv[2])
    print("and optional parameters: ", opt)

    fzero(fnon, x0, **opt)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("WARNING: not enough arguments passed")
        print(__doc__)

        print("continuing with default parameters instead...")
        main([sys.argv[0], "sqrt2", "1.4"])
    else:
        main(sys.argv)
