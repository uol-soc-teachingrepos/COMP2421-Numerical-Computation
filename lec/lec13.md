---
subtitle: Exact solutions and errors
title: Lecture 13
---

# Exact derivatives and exact solutions

-   In some special cases it is possible to evaluate the derivative of a function exactly.

-   Similarly, in some special cases it is possible to solve a differential equation exactly.

-   In general, however, this is not the case and so numerical methods are required - this is what this module is concerned with.

-   The special, exact, cases are not what this module is about, however it is helpful to consider one or two examples.

## Example 1

-   Consider the function $y(t) = t^2$.

-   We can plot an estimate of the graph of $y'(t)$ quite easily in this case:

G`{=html} <!-- ![]() TODO -->` ## Example 1 (cont.)

## Example 1 (cont.)

-   In fact we may use the definition of $y'(t)$ to evaluate this function at any point: $$
    y'(t) = \lim_{\mathrm{d}t \to 0} \frac{y(t + \mathrm{d}t) - y(t)}{\mathrm{d}t}.
    $$

-   When $y(t) = t^2$ we know that $$
    \begin{aligned}
    \frac{y(t + \mathrm{d}t) - y(t)}{\mathrm{d}t}
    & = \frac{(t + \mathrm{d}t)^2 - t^2}{\mathrm{d}t} \\
    & = \frac{t^2 + 2 \times t \times \mathrm{d}t + ( \mathrm{d}t )^2 - t^2}{\mathrm{d}t} \\
    & = 2 t + \mathrm{d}t.
    \end{aligned}
    $$

-   Taking the limit $\mathrm{d}t \to 0$, we see that $y'(t) = 2t$.

## Example 2

-   Similarly, when $y(t) = t^3$ we have $$
    \begin{aligned}
    \frac{y(t + \mathrm{d}t) - y(t)}{\mathrm{d}t}
    & = \frac{(t + \mathrm{d}t)^3 - t^3}{\mathrm{d}t} \\
    & = \frac{t^3 + 3 \times t^2 \times \mathrm{d}t + 3 \times t \times (\mathrm{d}t)^2 + (\mathrm{d}t)^2 - t^3}{\mathrm{d}t} \\
    & = 3 \times t^2 + 3 \times t \times \mathrm{d}t + (\mathrm{d}t)^2.
    \end{aligned}
    $$

-   Now taking the limit as $\mathrm{d}t \to 0$ we see that, in this case $y'(t) = 3t^2$.

-   In general, we may show that when $y(t) = t^m$, then $y'(t) = m t^{m-1}$.

## Example 3

-   By working backwards from a known expression for $y(t)$ and $y'(t)$ we can make up our own differential equation that has $y(t)$ as a known solution.

-   e.g., when $y(t) = t^3$: $$
    y'(t) = 3 t^2 = 3y(t) / t.
    $$

-   Hence we know the solution to the following equation: $$
    y'(t) = 3 y(t) / t \mbox{ subject to } y(1) = 1.
    $$

-   If we solve this for values of $t$ between $1.0$ and $2.0$, say, then we know that exact answer when $t = 2.0$ is $y(2) = 8$.

# Errors in Euler's method

-   We can solve this problem using Euler's method and then look at the errors when $t = 2.0$.

-   The following table shows computed results for the final solution, at $t = 2.0$, collected using the python function [`runEuler`](../code/lec13/runNumerical.html#runEuler) in [`runNumerical.py`](../code/lec13/runNumerical.html).

## Euler's method -- results

  $n$   $\mathrm{d}t$   solution   abs. error   ratio
  ----- --------------- ---------- ------------ --------
  10    0.1000          7.0000     1.0000       0.0000
  20    0.0500          7.4545     0.5455       0.5455
  40    0.0250          7.7143     0.2857       0.5238
  80    0.0125          7.8537     0.1463       0.5122
  160   0.0063          7.9259     0.0741       0.5062
  320   0.0031          7.9627     0.0373       0.5031
  640   0.0016          7.9813     0.0187       0.5016

## Euler's method -- results (cont.)

-   What is happening to the error as $\mathrm{d}t \to 0$?

    -   It is decreasing
    -   Each time $\mathrm{d}t$ is halved the error is halved.
    -   The error is proportional to $\mathrm{d}t$.

-   What might we expect the computed solution to be if we halved $\mathrm{d}t$ one more time?

## Big O Notation

-   In considering algorithm complexity you have already seen this notation. For example:

    -   Gaussian elimination requires $O(n^3)$ operations when $n$ is large.
    -   Backward substitution requires $O(n^2)$ operations when $n$ is large.

-   For large values of $n$ the *highest* powers of $n$ are the most significant.

-   For smaller values of $\mathrm{d}t$, it is the *lowest* powers of $\mathrm{d}t$ that are the most significant:

    -   when $\mathrm{d}t = 0.001$, $\mathrm{d}t$ is much bigger than $(\mathrm{d}t)^2$ for example.

## Big O Notation (cont.)

-   We can make use of the "big O" notation in either case.

-   For example, suppose $$
      f(x) = 2 x^2 + 4 x^3 + x^5 + 2 x^6$,
      $$

    -   then $f(x) = O(x^6)$ as $x \to \infty$
    -   and $f(x) = O(x^2)$ as $x \to 0$.

-   In this notation, we can say that **the error in Euler's method is $O(\mathrm{d}t)$**.

# Improving upon Euler's method

# The midpoint scheme
