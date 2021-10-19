---
starttime: "Dec 1, 2021 16:05"
subtitle: More on nonlinear equations
title: Lecture 18
---

TODO double check formatting and numerical results

## Recap

-   In the previous lecture we consider a modified version of Newton's method in which $f'(x^{(i)})$ is approximated: $$
    f'(x^{(i)}) \approx \frac{f(x^{(i)} + \mathrm{d}x) - f(x^{(i)})}{\mathrm{d}x}.
    $$

-   For a suitable choice of $\mathrm{d}x$ this was shown to work very well, producing results of the same accuracy as Newton's method in almost the same number of iterations.

-   We then introduced another popular modification of Newton's method that also approximates $f'(x^{(i)})$ as above for a particular choice of $\mathrm{d}x = x^{(i-1)} - x^{(i)}$.

-   The resulting iteration is known as the **secant method**.

# Reliability

-   The Newton, modified Newton and secant methods may not always converge for a particular choice of $x^{(0)}$.

-   The secant method in particular will fail if $x^{(0)} = x^{(1)}$ or $f(x^{(0)}) = f(x^{(1)})$.

-   Each of these methods can break down when

    -   $f'(x^{(i)}) = 0$ for $x^{(i)} \neq x^*$;
    -   $f'(x^{(i)})$ is small but nonzero, in which case $x^{(i+1)}$ may be further away from $x^*$ than $x^{(i)}$.

-   These methods are guarenteed to converge when $x^{(0)}$ is "sufficiently close" to $x^*$.

-   In practice a good initial estimate $x^{(0)}$ may not be known in advance.

# A combined approach

In this algorithm we seek to combine the reliability of the bisection algorithm with the speed of the secant algorithm:

0.  Take a function $f(x)$ and initial estimate $x^{(0)}$.

1.  Search for an initial point $x^{(1)}$ such that $f(x^{(0)}) f(x^{(1)}) < 0$, i.e. an initial bracket $[x^{(0)}, x^{(1)}]$ for $x^*$.

2.  Take a single step with the secant method $$
    x^{(2)} = x^{(1)} - f(x^{(1)}) \frac{x^{(1)} - x^{(0)}}{f(x^{(1)}) - f(x^{(0)})}
    $$ to produce a new estimate.

## A combined approach (cont.)

3.  If $x^{(2)}$ is outside $[x^{(0)}, x^{(1)}]$ then reject it and apply a single bisection step, i.e. find $x^{(2)} = (x^{(0)} + x^{(1)}) / 2$.

4.  Update the bracket to $$
    \begin{cases}
    [x^{(0)}, x^{(2)}] & \mbox{ if } f(x^{(0)}) f(x^{(2)}) \le 0; \\
    [x^{(2)}, x^{(1)}] & \mbox{ if } f(x^{(2)}) f(x^{(1)}) \le 0.
    \end{cases}
    $$

5.  If the method has not yet converged return to step 2 with the new interval.

## Notes

-   When the secant iteration becomes unreliable the algorithm reverts to the bisection approach.

-   When the approximation is close to the root the secant method will usually be used and should converge (almost) as rapidly as Newton.

-   This is implemented in [`fzero`](../numericalSolve.html#fzero) in [`numericalSolve.py`](../numericalSolve.py).

-   The approach can easily be adapted to find all of the roots in a given interval.

-   Variations and other hybrid methods are implemented in `scipy` as [`scipy.optimize.root_scalar`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root_scalar.html?highlight=root_scalar#scipy.optimize.root_scalar).

## Stopping criteria

The algorithm stops if any of the following holds:

-   ${|x^{(i)} - x^{(i-1)}|}/{|x^{(i)}|} < \mbox{\texttt{tolx}}$;
-   $|f(x^{(i)})| < \mbox{\texttt{tolfun}}$;
-   the number of iterations exceeds a specified number `maxiter`.

Criticisms:

-   convergence criteria should ideally satisfy *both* ${|x^{(i)} - x^{(i-1)}|}/{|x^{(i)}|} < \mbox{\texttt{tolx}}$ and $|f(x^{(i)})| < \mbox{\texttt{tolfun}}$;
-   cannot find solutions which do not cross the $x$-axis.

## Using `fzero`

``` python
fzero(fnon, x0, x1=None, tolx=1e-4, tolfun=1e-4, maxiter=100, verbose=True)
```

-   `fnon` is the function handle for $f(x)$ (`Callable[[float], float]`);
-   `x0` is the initial guess;
-   `x1` is an optional parameter giving the other end of the bracket. If `x1` is not passed to the function, `x1` is found automatically;
-   `tolx`, `tolfun`, `maxiter` related to the stopping criteria. Each are optional with default values set;
-   `verbose` says whether to print out convergence information.

Some sample function calls are given in [`runFzero.py`](../code/lec18/runFzero.html).

## Examples

1.  Consider the example with $f(x) = x^2 - R$ and $R=2$. Take $x^{(0)} = 1$ and use the function call

    ``` python
    fzero(sqrt2, 1.0, tolx=1.0e-12, tolfun=1.0e-12)
    ```

    -   The algorithm gives $x^* = 1.414214$ after 10 iterations.
    -   `fzero` does not know where to position the initial bracket $[x^{(0)}, x^{(1)}]$.
    -   If $x^{(0)}$ is a poor estimate it takes some time, or fails altogether.

## Examples (cont.)

2.  Consider the example with $f(x) = x^2 - R$ with $R=2$, take $x^{(0)} = 1.0$ and use the function call

    ``` python
    eps = np.finfo(float).eps
    fzero(sqrt2, 1.0, tolx=eps, tolfun=eps)
    ```

    -   The algorithm gives $x^* = 1.414214$ after 12 iterations.
    -   Convergence is to *machine precision* - so it takes more iterations than previously - but not too many!

## Examples (cont.)

3.  Consider the compound interest example with $[x^{(0)}, x^{(1)}] = [200, 300]$, using the function call

    ``` python
    fzero(compound, 200, 300, tolx=1.0e-3, tolfun=1.0e-12)
    ```

    -   This converges to the root $x^* = 235.889095$ after 18 iterations (using quite a large stopping tolerance in this case).

## Examples (cont.)

4.  Consider the NACA0012 aerofoil example with $[x^{(0)}, x^{(1)}] = [0.5, 1]$ using the function call

    ``` python
    fzero(naca0012, 0.5, 1.0, tolx=1.0e-12, tolfun=1.0e-12)
    ```

    This converges to the root $x^* = 0.765249$ in 13 iterations.

5.  Consider the NACA0012 aerofoil example with $[x^{(0)}, x^{(1)}] = [0, 0.5]$ using the function call

    ``` python
    fzero(naca0012, 0.0, 0.5, tolx=1.0e-12, tolfun=1.0e-12)
    ```

    -   This converges to the other root $x^* = 0.33899$ after 44 iterations.

# Summary

-   Solving nonlinear equations is hard.

-   It is not always possible to guarantee an accurate solution.

-   However, it is possible to design a robust algorithm that will usually give a good answer.

-   Finding all possible solutions is particularly challenging since we may not know how many solutions there are in advance.
