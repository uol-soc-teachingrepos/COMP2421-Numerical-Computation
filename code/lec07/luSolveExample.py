"""
luSolveExample

Examples of LU_solve

To run via commandline use one of the folllowing:

python luSolveExample.py -m 3
python luSolveExample.py -m 3b
python luSolveExample.py -m 4
python luSolveExample.py -m 5

"""
# Python modules
import getopt
import sys

import numpy as np

# Comp2941 modules
sys.path.append("..")
from matrixSolve import *


def main(argv):
    try:
        opts, args = getopt.getopt(argv[1:], "m:", ["mode="])
    except getopt.GetoptError:
        print("Warning: Unknown flag!")
        sys.exit(2)

    mode = None

    for opt, arg in opts:
        if opt in ("-m", "--mode"):
            mode = arg

    if mode == "3":
        lu_solve_3()
    elif mode == "3b":
        lu_solve_3b()
    elif mode == "4":
        lu_solve_4()
    elif mode == "5":
        lu_solve_5()


def lu_solve_3():
    """
    Solve a 3x3 example linear system of the form A x = b
    """

    # Assign the example 3x3 matrix
    A = np.array([[2, 1, 4], [1, 2, 2], [2, 4, 6]])

    # Assign an example right hand side column 3-vector
    b = np.array([[12, 9, 22]])
    b = np.transpose(b)

    # Factorise A into LU form
    L, U = lu_factorise(A)

    # Solve lower triangular system L z = b for z
    z = lower_triangular_solve(L, b)

    # Solve the upper triangular system U x = z for x
    x = upper_triangular_solve(U, z)

    print(L)
    print(U)
    print(z)
    print(x)


def lu_solve_3b():
    """
    Solve a 3x3 example linear system of the form A x = b
    """

    # Assign the example 3x3 matrix
    A = np.array([[4, 2, 0], [2, 3, 1], [0, 1, 2.5]])

    # Assign an example right hand side column 3-vector
    b = np.array([[12, 9, 22]])
    b = np.transpose(b)

    # Factorise A into LU form
    L, U = lu_factorise(A)

    # Solve lower triangular system L z = b for z
    z = lower_triangular_solve(L, b)

    # Solve the upper triangular system U x = z for x
    x = upper_triangular_solve(U, z)

    print(L)
    print(U)
    print(z)
    print(x)


def lu_solve_4():
    """
    Solve a 4x4 example linear system of the form A x = b
    """

    # Assign the example 3x3 matrix
    A = np.array(
        [
            [1, 1.0 / 2, 1.0 / 3, 1.0 / 4],
            [1.0 / 2, 1.0 / 3, 1.0 / 4, 1.0 / 5],
            [1.0 / 3, 1.0 / 4, 1.0 / 5, 1.0 / 6],
            [1.0 / 4, 1.0 / 5, 1.0 / 6, 1.0 / 7],
        ]
    )

    # Assign an example right hand side column 3-vector
    b = np.array([[25.0 / 12, 77.0 / 60, 57.0 / 60, 319.0 / 420]])
    b = np.transpose(b)

    # Factorise A into LU form
    L, U = lu_factorise(A)

    # Solve lower triangular system L z = b for z
    z = lower_triangular_solve(L, b)

    # Solve the upper triangular system U x = z for x
    x = upper_triangular_solve(U, z)

    print(L)
    print(U)
    print(z)
    print(x)


def lu_solve_5():
    """
    Solve a 5x5 example linear system of the form A x = b
    """

    # Assign the example 3x3 matrix
    A = np.array(
        [
            [1, 1.0 / 2, 1.0 / 3, 1.0 / 4, 1.0 / 5],
            [1.0 / 2, 1.0 / 3, 1.0 / 4, 1.0 / 5, 1.0 / 6],
            [1.0 / 3, 1.0 / 4, 1.0 / 5, 1.0 / 6, 1.0 / 7],
            [1.0 / 4, 1.0 / 5, 1.0 / 6, 1.0 / 7, 1.0 / 8],
            [1.0 / 5, 1.0 / 6, 1.0 / 7, 1.0 / 8, 1.0 / 9],
        ]
    )

    # Assign an example right hand side column 3-vector
    b = np.array([[1.0, 1.0 / 2, 1.0 / 3, 1.0 / 4, 1.0 / 5]])
    b = np.transpose(b)

    # Factorise A into LU form
    L, U = lu_factorise(A)

    # Solve lower triangular system L z = b for z
    z = lower_triangular_solve(L, b)

    # Solve the upper triangular system U x = z for x
    x = upper_triangular_solve(U, z)

    print(L)
    print(U)
    print(z)
    print(x)


if __name__ == "__main__":
    main(sys.argv)
