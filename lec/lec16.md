---
subtitle: Solution of nonlinear equations ii
title: Lecture 16
---

# Newton's method: Python implementation

-   A python implementation is provided in the function [`newton`](../code/numericalSolve.html#newton) in [`numericalSolve.py`](../code/numericalSolve.html).

-   This has four parameters:

    ``` python
    newton(fnon, dfnon, x0, tol)
    ```

    -   the first two are "function handles" for $f(x)$ and $f'(x)$ (`Callable[[float], float]`);
    -   the third and fourth are initial guess and convergence tolerance(`float` and `float`).

-   The main loop is as follows:

    ``` python
    x = x0
    fnon(x)
    while abs(f) > tol:       # iterate until less than or eq tol
        x = x - f / dfnon(x)  # apply one Newton iteration
        f = fnon(x)           # reevaluate f at new estimate
    ```

## Examples

1.  Use Newton's method to approximate the value of $\sqrt{2}$ by solving $x^2 - R = 0$.

    $$
     f(x) = x^2 - R
     \:
     \Rightarrow
     \:
     f'(x) = 2x
     \:
     \Rightarrow
     \:
     x^{(i+1)} = x^{(i)} - \frac{(x^{(i)})^2 - R}{2 x^{(i)}}.
     $$

    -   The call `$ python runNewton.py sqrt2 dsqrt2 1.0 1.0e-4` gives the root as $x^* \approx 1.414216$ after 3 iterations.
    -   The iteration stopped when $|f(x^{(i)})| < 10^{-4}$.
    -   We could also require that $|x^{(i+1)} - x^{(i)} < 10^{-4}$.

## Examples (cont).

2.  The call `$ python runNewton.py naca0012 dnaca0012 1.0 1.0e-4` gives the root as $x^* \approx 0.765789$ after 3 iterations for the NACA0012 aerofoil example.

3.  The call `$ python runNewton.py naca0012 dnaca0012 0.1 1.0e-4` gives the root as $x^* \approx 0.033863$ after 3 iterations for the second solution to the NACA0012 aerofoil example.

In all cases the performance is considerable superior to that of the bisection method.

# Advantages/disadvantages
