"""
nonlinear_functions.py

various nonlinear functions

"""

import numpy as np


def compound(n):
    """
    Evaluate the nonlinear function for finding the number of months required
    to repay a mortgage of P pounds at a repayment of M pounds per month and
    an annual interest rate of r percent.
    
    ARGUMENTS:  n   the point at which to evaluate the function
    
    RETURNS:    f   the value of the function at n
    """
    # Set P, M and r.
    P = 150000
    M = 1000
    r = 5.0
    # Evaluate the function.
    i = r / 1200
    f = M - P * (i * (1 + i)**n) / ((1 + i)**n - 1)

    return f


def naca0012(x):
    """
    Evaluate the nonlinear function for the naca0012 aerofoil example.
    
    ARGUMENTS:  x   the point at which to evaluate
    
    RETURNS:    f   the value of the function at x
    """

    # Set the required thickness at the intersection to be 0.1.
    t = 0.1

    # Evaluate the function.
    yp = -0.1015 * np.power(x, 4) \
         + 0.2843 * np.power(x, 3) \
         - 0.3516 * np.power(x, 2) \
         - 0.126 * x \
         + 0.2969 * np.sqrt(x)
    f = yp - 0.5 * t

    return f


def dnaca0012(x):
    """
    Evaluate the derivative function for the naca0012 aerofoil example.
    
    ARGUMENTS:  x   the point at which to evaluate
    
    RETURNS:    f   the value of the function at x
    """

    # Evaluate the derivative.
    dy = -4 * 0.1015 * np.power(x, 3) \
         + 3 * 0.2843 * np.power(x, 2) \
         - 2 * 0.3516 * x \
         - 0.126 \
         + 0.2969 * 0.5 * np.power(x, -0.5)
    f = dy

    return f


def lin(x):
    """
    Evaluate the nonlinear function for the double root test case.
    
    ARGUMENTS:  x   the point at which to evaluate
    
    RETURNS:    f   the value of the function at x
    """

    return (x - 1)**2


def dlin(x):
    """
    Evaluate the derivative of the function for the double root test case.
    
    ARGUMENTS:  x   the point at which to evaluate
    
    RETURNS:    f   the value of the function at x
    """

    return 2 * (x - 1)


def sqrt2(x):
    """
    Evaluate the nonlinear function for finding the square root of 2.
    
    ARGUMENTS:  x   the point at which to evaluate
    
    RETURNS:    f   the value of the function at x
    """
    # Set R for evaluating sqrt(2).
    R = 2.0
    # Evaluate the function.
    f = x * x - R
    return f


def dsqrt2(x):
    """
    Evaluate the derivative function for finding the square root of 2.
    
    ARGUMENTS:  x   the point at which to evaluate
    
    RETURNS:    f   the value of the function at x
    """
    # Evaluate the function.
    return 2.0 * x


def cuberoot3(x):
    """
    Evaluate the f(x)=x^3-3.
    
    ARGUMENTS:  x   the point at which to evaluate
    
    RETURNS:    f   the value of the function at x
    """
    # Set R for evaluating cuberoot(3).
    R = 3.0
    # Evaluate the function.
    return x**3 - R


def dcuberoot3(x):
    """
    Evaluate the derivative f(x)=x^3-R.
    
    ARGUMENTS:  x   the point at which to evaluate
    
    RETURNS:    f   the value of the function at x
    """
    # Evaluate the function.
    return 3 * x**2


def sqrtR(x, R):
    """
    Evaluate the nonlinear function for finding the square root of R.
    
    ARGUMENTS:  x   the point at which to evaluate
                R   value of which to find square root
    
    RETURNS:    f   the value of the function at x
    """

    return x * x - R


def cuberootR(x, R):
    """
    Evaluate the nonlinear function for finding the cube root of R.
    
    ARGUMENTS:  x   the point at which to evaluate
                R   value of which to find cube root
    
    RETURNS:    f   the value of the function at x
    """

    return x * x * x - R


def poly3(x):
    """
    ARGUMENTS:  x   the point at which to evaluate
    
    RETURNS:    f   the value of the function at x
    """
    # Evaluate the function.
    return x**3 + x**2 - 3


def dpoly3(x):
    """
    ARGUMENTS:  x   the point at which to evaluate
    
    RETURNS:    f   the value of the function at x
    """
    # Evaluate the function.
    return 3 * x**2 + 2 * x


def poly4(x):
    """
    ARGUMENTS:  x   the point at which to evaluate
    
    RETURNS:    f   the value of the function at x
    """
    # Evaluate the function.
    return x**4 - x - 1


def dpoly4(x):
    """
    ARGUMENTS:  x   the point at which to evaluate
    
    RETURNS:    f   the value of the function at x
    """
    # Evaluate the function.
    return 4 * x**3 - 1


def polyN(x, N):
    """
    Evaluate the nonlinear function f(x).

    ARGUMENTS:  x   the point at which to evaluate
                N   degree of polynomial

    RETURNS:    f   the value of the function at x
    """

    return x**N - x - 1
