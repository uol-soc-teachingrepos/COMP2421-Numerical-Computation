---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.15.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Lecture 18: Robust nonlinear solvers

### Recap

-   In the previous lecture we consider a modified version of Newton's method in which $f'(x^{(i)})$ is approximated:

    $$
    f'(x^{(i)}) \approx \frac{f(x^{(i)} + \mathrm{d}x) - f(x^{(i)})}{\mathrm{d}x}.
    $$

-   For a suitable choice of $\mathrm{d}x$ this was shown to work very well, producing results of the same accuracy as Newton's method in almost the same number of iterations.

-   We then introduced another popular modification of Newton's method that also approximates $f'(x^{(i)})$ as above for a particular choice of $\mathrm{d}x = x^{(i-1)} - x^{(i)}$.

-   The resulting iteration is known as the **secant method**.

## Reliability

-   The Newton, modified Newton and secant methods may not always converge for a particular choice of $x^{(0)}$.

-   The secant method in particular will fail if $x^{(0)} = x^{(1)}$ or $f(x^{(0)}) = f(x^{(1)})$.

-   Each of these methods can break down when

    -   $f'(x^{(i)}) = 0$ for $x^{(i)} \neq x^*$;
    -   $f'(x^{(i)})$ is small but nonzero, in which case $x^{(i+1)}$ may be further away from $x^*$ than $x^{(i)}$.

-   These methods are guaranteed to converge when $x^{(0)}$ is "sufficiently close" to $x^*$.

-   In practice a good initial estimate $x^{(0)}$ may not be known in advance.

## A combined approach

In this algorithm we seek to combine the reliability of the bisection algorithm with the speed of the secant algorithm:

0.  Take a function $f(x)$ and initial estimate $x^{(0)}$.

1.  Search for an initial point $x^{(1)}$ such that $f(x^{(0)}) f(x^{(1)}) < 0$, i.e. an initial bracket $[x^{(0)}, x^{(1)}]$ for $x^*$.

2.  Take a single step with the secant method

    $$
    x^{(2)} = x^{(1)} - f(x^{(1)}) \frac{x^{(1)} - x^{(0)}}{f(x^{(1)}) - f(x^{(0)})}
    $$

	to produce a new estimate.

3.  If $x^{(2)}$ is outside $[x^{(0)}, x^{(1)}]$ then reject it and apply a single bisection step, i.e. find $x^{(2)} = (x^{(0)} + x^{(1)}) / 2$.

4.  Update the bracket to

    $$
    \begin{cases}
    [x^{(0)}, x^{(2)}] & \text{ if } f(x^{(0)}) f(x^{(2)}) \le 0; \\
    [x^{(2)}, x^{(1)}] & \text{ if } f(x^{(2)}) f(x^{(1)}) \le 0.
    \end{cases}
    $$

5.  If the method has not yet converged return to step 3 with the new interval.

### Notes

-   When the secant iteration becomes unreliable the algorithm reverts to the bisection approach.

-   When the approximation is close to the root the secant method will usually be used and should converge (almost) as rapidly as Newton.

-   The approach can easily be adapted to find all of the roots in a given interval.

-   Variations and other hybrid methods are implemented in `scipy` as [`scipy.optimize.root_scalar`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root_scalar.html?highlight=root_scalar#scipy.optimize.root_scalar).

### Stopping criteria

The algorithm stops if any of the following holds:

-   ${|x^{(i)} - x^{(i-1)}|}/{|x^{(i)}|} < \texttt{tolx}$;
-   $|f(x^{(i)})| < \texttt{tolfun}$;
-   the number of iterations exceeds a specified number `maxiter`.

Criticisms:

-   convergence criteria should ideally satisfy *both* ${|x^{(i)} - x^{(i-1)}|}/{|x^{(i)}|} < \texttt{tolx}$ and $|f(x^{(i)})| < \texttt{tolfun}$;
-   cannot find solutions which do not cross the $x$-axis.

### Implementation

The method has been slightly improved to become [Brent's method](https://en.wikipedia.org/wiki/Brent%27s_method) which is implemented in `scipy` as [`scipy.optimize.brentq`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.brentq.html).

Note that this method requires both initial estimates $x^{(0)}$ and $x^{(1)}$.

```{code-cell} ipython3
:tags: [hide-input]

from scipy.optimize import brentq

help(brentq)
```

#### Exercise

How can we estimate this initial bracket from an initial guess?

### Examples

We will test `scipy`'s implementation with our three examples from before.

Consider the example with $f(x) = x^2 - R$ and $R=2$. Take $x^{(0)} = 0$ and $x^{(1)} = 2$ and use the function call

```{code-cell} ipython3
def sqrt2(x):
    return x**2 - 2.0


brentq(sqrt2, 0.0, 2.0, xtol=1.0e-4, maxiter=100, full_output=True)
```

-   The algorithm gives $x^* = 1.4142$ after 7 iterations.

Consider the example with $f(x) = x^2 - R$ with $R=2$, take $x^{(0)} = 0$ and $x^{(1)} = 2$ and use the function call

```{code-cell} ipython3
import numpy as np

eps = np.finfo(np.double).eps
brentq(sqrt2, 0.0, 2.0, xtol=4 * eps, maxiter=100, full_output=True)
```

-   The algorithm gives $x^* = 1.414214$ after 9 iterations.
-   Convergence is to *machine precision* - so it takes more iterations than previously - but not too many!

Consider the compound interest example with $[x^{(0)}, x^{(1)}] = [200, 300]$, using the function call

```{code-cell} ipython3
def compound(n):
    # Set P, M and r.
    P = 150000
    M = 1000
    r = 5.0
    # Evaluate the function.
    i = r / 1200
    f = M - P * (i * (1 + i) ** n) / ((1 + i) ** n - 1)

    return f


brentq(compound, 200, 300, xtol=1.0e-1, full_output=True)
```

-   This converges to the root $x^* = 235.87$ after 5 iterations (using quite a large stopping tolerance in this case).


Consider the NACA0012 aerofoil example with $[x^{(0)}, x^{(1)}] = [0.5, 1]$ using the function call

```{code-cell} ipython3
def naca0012(x):
    # Set the required thickness at the intersection to be 0.1.
    t = 0.1

    # Evaluate the function.
    yp = (
        -0.1015 * np.power(x, 4)
        + 0.2843 * np.power(x, 3)
        - 0.3516 * np.power(x, 2)
        - 0.126 * x
        + 0.2969 * np.sqrt(x)
    )
    f = yp - 0.5 * t

    return f


brentq(naca0012, 0.5, 1.0, xtol=1.0e-4, full_output=True)
```

This converges to the root $x^* = 0.765249$ in 6 iterations.

Consider the NACA0012 aerofoil example with $[x^{(0)}, x^{(1)}] = [0, 0.5]$ using the function call

```{code-cell} ipython3
brentq(naca0012, 0.0, 0.5, xtol=1.0e-4, full_output=True)
```

-   This converges to the other root $x^* = 0.33899$ after 44 iterations.

## Summary

-   Solving nonlinear equations is hard.

-   It is not always possible to guarantee an accurate solution.

-   However, it is possible to design a robust algorithm that will usually give a good answer.

-   Finding all possible solutions is particularly challenging since we may not know how many solutions there are in advance.

## Further reading

- `scipy`: Optimization and root finding [`scipy.optimize`](https://docs.scipy.org/doc/scipy/reference/optimize.html)

The [slides used in the lecture](./lec18_.ipynb) are also available
