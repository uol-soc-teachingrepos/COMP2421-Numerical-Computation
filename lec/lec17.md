---
subtitle: Quasi-Newton methods
title: Lecture 17
---

# Approximation of the derivative

-   The formula $x^{(i+1)} = x^{(i)} - \frac{f(x^{(i)})}{f'(x^{(i)})}$ requires that we are able to compute an expression for the derivative of $f(x)$.

-   This may not always be possible:

    -   the function $f(x)$ may be a "black box";
    -   the formula for $f(x)$ may be known but may be difficult for us to differentiate.

-   We can modify Newton's method by simply approximating $f'(x^{(i)})$, rather like we approximated $y'(t)$ when solving a differential equation.

## Approximation of $f'(x)$

-   Recall that $$f'(x) = \lim_{\mathrm{d}x \to 0} \frac{f(x + \mathrm{d}x) - f(x)}{\mathrm{d}x}$$.

-   Hence we can choose a small value for $\mathrm{d}x$ (how small?) and approximate: $$
    f'(x) \approx \frac{f(x + \mathrm{d}x) - f(x)}{\mathrm{d}x}.
    $$

-   This modified-Newton method then becomes $$
    x^{(i+1)} = x^{(i)} - \frac{\mathrm{d}x \times f(x^{(i)})}{f(x^{(i)} + \mathrm{d}x) - f(x^{(i)})}.
    $$

## The choice of $\mathrm{d}x$

-   Note that the computational cost of calculating each iterate is about the same as for Newton's method.

-   What is not obvious however is what choice should be made for the value of $\mathrm{d}x$.

-   In theory (exact arithmetic) the smaller the choice of $\mathrm{d}x$ the better the approximation of the derivative.

-   In practice, however, we know that the operation of subtracting two very similar values from each other can lead to significant rounding errors when using floating point arithmetic.

-   Consider the following example...

# Problems with floating point arithmetic

-   When $f(x) = x^3$ then $f'(x) = 3 x^2$.

-   Hence, at $x_0 = 1$, $f(x_0) = 1$ and $f'(x_0) = 3$.

-   Consider what happens when we approximate this with python, using finite values for $\mathrm{d}x$.

  dx        approx         abs error    rel error
  --------- -------------- ------------ ------------
  1.0e-04   3.0003000100   3.0001e-04   3.0001e-04
  1.0e-06   3.0000029998   2.9998e-06   2.9998e-06
  1.0e-08   3.0000000040   3.9720e-09   3.9720e-09
  1.0e-10   3.0000002482   2.4822e-07   2.4822e-07
  1.0e-12   3.0002667017   2.6670e-04   2.6670e-04
  1.0e-14   2.9976021665   2.3978e-03   2.3978e-03
  1.0e-16   0.0000000000   3.0000e+00   3.0000e+00

## python example

TODO how to generate this table

# Modified Newton's method

-   Recall the definition of machine precision/unit roundoff from Lecture 3.

-   The function [`modified_newton`](../code/numericalSolve.html#modified_newton) in [`numericalSolve.py`](../code/numericalSolve..html) implements the modified Newton algorithm without the need to know $f'(x)$.

-   The main loop is as follows:

``` python
eps = np.finfo(float).eps
dx = np.sqrt(eps)
x = x0
f = fnon(x)
while abs(f) > tol:
    x = x - (dx * f)/(fnon(x + dx) - f)
    f = fnon(x)
```

## Examples

1.  Use the modified Newton method to approximate the value of $\sqrt{2}$ by solving $x^2 - R = 0$.

    The function call ... gives TODO

# The secant method

-   Suppose we choose $\mathrm{d}x = x^{(i-1)} - x^{(i)}$, then we get $$
    f'(x^{(i)}) \approx \frac{f(x^{(i)} + \mathrm{d}x) - f(x^{(i)})}{\mathrm{d}x}
    = \frac{f(x^{(i)}) - f(x^{(i-1)})}{x^{(i)} - x^{(i-1)}}.
    $$

-   Newton's method then becomes $$
    x^{(i+1)} = x^{(i)} - f(x^{(i)}) \frac{x^{(i)} - x^{(i-1)}}{f(x^{i}) - f(x^{(i-1)})}
    \left(\approx x^{(i)} - \frac{f(x^{(i)})}{f'(x^{(i)})} \right).
    $$

-   Note that the main advantage of this approach over the previous modified Newton approximation is that only one new evaluation of $f(x)$ is required per iteration (apart from the very first iteration).

## Pros and cons

Advantages:

-   $f'(x)$ is not required;
-   only one new evaluation of $f(x)$ per iteration;
-   still converges almost as quickly as Newton's method.

Disadvantages:

-   *two* starting values, $x^{(0)}$ and $x^{(1)}$, are required;
-   may require one more iteration than exact Newton (but iterations are cheaper);
-   like Newton's method the iteration can fail to converge for some starting iterates.

## Examples

TODO
