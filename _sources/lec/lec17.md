---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Lecture 17: Quasi-Newton methods

## Approximation of the derivative

-   The formula $x^{(i+1)} = x^{(i)} - \frac{f(x^{(i)})}{f'(x^{(i)})}$ requires that we are able to compute an expression for the derivative of $f(x)$.

-   This may not always be possible:

    -   the function $f(x)$ may be a "black box";
    -   the formula for $f(x)$ may be known but may be difficult for us to differentiate.

-   We can modify Newton's method by simply approximating $f'(x^{(i)})$, rather like we approximated $y'(t)$ when solving a differential equation.

### Approximation of $f'(x)$

-   Recall that $f'(x) = \lim_{\mathrm{d}x \to 0} \frac{f(x + \mathrm{d}x) - f(x)}{\mathrm{d}x}$.

-   Hence we can choose a small value for $\mathrm{d}x$ (how small?) and approximate:

    $$
    f'(x) \approx \frac{f(x + \mathrm{d}x) - f(x)}{\mathrm{d}x}.
    $$

-   This modified-Newton method then becomes

    $$
    x^{(i+1)} = x^{(i)} - \frac{\mathrm{d}x \times f(x^{(i)})}{f(x^{(i)} + \mathrm{d}x) - f(x^{(i)})}.
    $$

### The choice of $\mathrm{d}x$

-   Note that the computational cost of calculating each iterate is about the same as for Newton's method.

-   What is not obvious however is what choice should be made for the value of $\mathrm{d}x$.

-   In theory (exact arithmetic) the smaller the choice of $\mathrm{d}x$ the better the approximation of the derivative.

-   In practice, however, we know that the operation of subtracting two very similar values from each other can lead to significant rounding errors when using floating point arithmetic.

-   Consider the following example...

## Problems with floating point arithmetic

-   When $f(x) = x^3$ then $f'(x) = 3 x^2$.

-   Hence, at $x_0 = 1$, $f(x_0) = 1$ and $f'(x_0) = 3$.

-   Consider what happens when we approximate this with python, using finite values for $\mathrm{d}x$.

```{code-cell} ipython3
:tags: [remove-input]
def f(x):
    return x**3
def df(x):
    return 3*x**2

x = 1

headers = ["dx", "approx", "abs error", "rel error"]
data = []

for e in range(4, 18, 2):
    dx = 10 ** -e
    approx = (f(x + dx) - f(x)) / dx
    exact = df(x)
    abs_error = abs(exact - approx)
    rel_error = abs(exact - approx) / exact

    new_data = [dx, approx, abs_error, rel_error]
    data.append(new_data)

import pandas as pd

df = pd.DataFrame(data, columns=headers)
df.style.format(formatter={"dx": "{:e}", "approx": "{:f}", "abs error": "{:e}", "rel error": "{:e}"}).hide_index().set_caption("Simple approximation of a derivative using floating point arithmetic")
```

## Modified Newton's method

-   Recall the definition of machine precision/unit roundoff from Lecture 3.

-   The modified Newton method uses $\mathrm{d}x = \sqrt{eps}$.

- For double precision we have

```{code-cell} ipython3
import numpy as np
eps = np.finfo(float).eps
dx = np.sqrt(eps)

x0 = 1.0
df_approx = ((x0+dx)**3 - x0**3) / dx
abs_error = abs(df_approx - 3)
rel_error = abs_error / 3

print(f"{dx=}\n{df_approx=}\n{abs_error=}\n{rel_error=}")
```

### Examples

- The example to compute the square root of 2 to a tolerance of $10^{-12}$ with starting value $1$ gives $x^* \approx 1.4142135623731$ after 5 iterations.

- The naca0012 example starting at 1 with tolerance $10^{-4}$ gives $x^* \approx 0.76579$ after 2 iterations.

- The naca0012 example starting at 1 with tolerance $10^{-5}$ gives $x^* \approx 0.765239$ after 3 iterations.

- The naca0012 example starting at 0.1 with tolerance $10^{-4}$ gives $x^* \approx 0.03386$ after 5 iterations.

In each case the performance is almost identical to the Newton method.

## The secant method

-   Suppose we choose $\mathrm{d}x = x^{(i-1)} - x^{(i)}$, then we get

    $$
    f'(x^{(i)}) \approx \frac{f(x^{(i)} + \mathrm{d}x) - f(x^{(i)})}{\mathrm{d}x}
    = \frac{f(x^{(i)}) - f(x^{(i-1)})}{x^{(i)} - x^{(i-1)}}.
    $$

-   Newton's method then becomes

    $$
    x^{(i+1)} = x^{(i)} - f(x^{(i)}) \frac{x^{(i)} - x^{(i-1)}}{f(x^{i}) - f(x^{(i-1)})}
    \left(\approx x^{(i)} - \frac{f(x^{(i)})}{f'(x^{(i)})} \right).
    $$

-   Note that the main advantage of this approach over the previous modified Newton approximation is that only one new evaluation of $f(x)$ is required per iteration (apart from the very first iteration).

### Pros and cons

Advantages:

-   $f'(x)$ is not required;
-   only one new evaluation of $f(x)$ per iteration;
-   still converges almost as quickly as Newton's method.

Disadvantages:

-   *two* starting values, $x^{(0)}$ and $x^{(1)}$, are required;
-   may require one more iteration than exact Newton (but iterations are cheaper);
-   like Newton's method the iteration can fail to converge for some starting iterates.

### Examples

- The example to compute the square root of 2 starting from 1 and 1.5 to a tolerance of $10^{-4}$ gives the solution as $x^* \approx 1.4142$ after 3 iterations.

- The example to computation compound interest start from 100 and 120 to a tolerance of 0.1 gives the solution as $x^* \approx 235.9$ after 6 iterations.

- The naca0012 example starting from 1 and 0.9 to a tolerance of $10^{-4}$ gives the solution as $x^* \approx 0.7653$ after 3 iterations.

- The naca0012 example starting from 0 and 0.1 to a tolerance of $10^{-4}$ gives the solution as $x^* \approx 0.0339$ after 5 iterations.

## Further reading

- Wikipedia: [Quasi-Newton method](https://en.wikipedia.org/wiki/Quasi-Newton_method)
- Wikipedia: [Secant method](https://en.wikipedia.org/wiki/Secant_method)
- `scipy`: Optimization and root finding [`scipy.optimize`](https://docs.scipy.org/doc/scipy/reference/optimize.html)

The [slides used in the lecture](./lec17_.ipynb) are also available
