# Lecture 03: Floating point number systems

## Finite precision number systems

-   Computers store numbers with **finite precision**, i.e. using a finite set of bits (binary digits), typically 32 or 64 of them.

-   Many numbers cannot be stored exactly

    -   Some numbers cannot be represented precisely using **any** finite set of digits:\
        e.g. $\sqrt{2} = 1.141 42\ldots$, $\pi = 3.141 59\ldots$, etc.
    -   Some cannot be represented precisely in a given number base:\
        e.g. $\frac{1}{9} = 0.111\ldots$ (decimal), $\frac{1}{5} = 0.0011 0011 \ldots$ (binary).
    -   Others can be represented by a finite number of digits but only using more than are available: e.g. $1.526 374 856 437$ cannot be stored exactly using 10 decimal digits.

### Issues

The inaccuracies inherent in finite precision arithmetic must be modelled in order to understand:

-   how the numbers are represented (and the nature of associated limitations);

-   the errors in their representation;

-   the errors which occur when arithmetic operations are applied to them.

The examples shown here will be in **decimal** by the issues apply to any base, *e.g.* **binary**.

## Normalised systems

### A general representation

Any finite precision number can be written using the floating point representation

$$
 x = \pm 0.b_1 b_2 b_3 \ldots b_{t-1} b_t \times \beta^e.
$$

-   The digits $b_i$ are integers satisfying $0 \le b_i \le \beta - 1$.
-   The **mantissa**, $b_1 b_2 b_3 \ldots b_{t-1} b_t$, contains $t$ digits.
-   $\beta$ is the **base** (always a positive integer).
-   $e$ is the integer **exponent** and is bounded ($L \le e \le U$).

$(\beta, t, L, U)$ fully defines a finite precision number system.

### Normalisation

**Normalised** finite precision systems will be considered here for which

$$
b_1 \neq 0 \quad (0 < b_1 \le \beta -1).
$$

Examples:

1.  In the case $(\beta, t, L, U) = (10, 4, -49, 50)$ (base 10), $$
    10 000 = .1000 \times 10^5, \quad
    22.64 = .2264 \times 10^2, \quad
    0.000 056 7 = .5670 \times 10^{-4}
    $$
2.  In the case $(\beta, t, L, U) = (2, 6, -7, 8)$ (binary), $$
    1 0000 = .1000 00 \times 2^5, \quad
    1011.11 = .1011 11 \times 2^4,$$ $$
    0.0000 11 = .1100 00 \times 2^{-4}.
    $$
3.  **Zero** is always taken to be a special case e.g., $0 = \pm .00\ldots 0 \times \beta^0$.

### Standards

1.  The [IEEE single precision standard](https://doi.org/10.1109/IEEESTD.2019.8766229) is $(\beta, t, L, U) = (2, 23, -127, 128)$. This is available via `numpy.single`.

2.  The [IEEE double precision standard](https://doi.org/10.1109/IEEESTD.2019.8766229) is $(\beta, t, L, U) = (2, 52, -1023, 1024)$. This is available via `numpy.double`.

### Example 1

Consider the number system given by $(\beta, t, L, U) = (10, 2, -1, 2)$ which gives

$$
 x = \pm .b_1 b_2 \times 10^e \text{ where } -1 \le e \le 2.
$$

a.  How many numbers can be represented by this normalised system?

b.  What are the two largest positive numbers in this system?

c.  What are the two smallest positive numbers?

d.  What is the smallest possible difference between two numbers in this system?

### Example 2 (homework)

Consider the number system given by $(\beta, t, L, U) = (10, 3, -3, 3)$ which gives $$
 x = \pm .b_1 b_2 b_3 \times 10^e \text{ where } -3 \le e \le 3.
$$

a.  How many numbers can be represented by this normalised system?

b.  What are the two largest positive numbers in this system?

c.  What are the two smallest positive numbers?

d.  What is the smallest possible difference between two numbers in this system?

e.  What is the smallest possible difference in this system, $x$ and $y$, for which $x < 100 < y$?

## Errors and their representations

From now on $fl(x)$ will be used to represent the (approximate) stored value of $x$. The error in this representation can be expressed in two ways.

$$
\begin{aligned}
 \text{Absolute error} &= | fl(x) - x | \\
 \text{Relative error} &= \frac{| fl(x) - x |}{|x|}.
\end{aligned}
$$

The number $fl(x)$ is said to approximate $x$ to $t$ **significant digits** (or figures) if $t$ is the largest non-negative integer for which

$$
 \text{Relative error} < 0.5 \times \beta^{1-t}.
$$

It can be proved that if the relative error is equal to $\beta^{-d}$ then $fl(x)$ has $d$ correct significant digits. -->

### Bounding the errors

In the number system given by $(\beta, t, L, U)$, the nearest (larger) representable number to $x = 0.b_1 b_2 b_3 \ldots b_{t-1} b_t \times \beta^e$ is

$$
 \tilde{x} = x + .\underbrace{000\ldots01}_{t \text{ digits}} \times \beta^e = x + \beta^{e-t}
$$

Any number $y \in (x, \tilde{x})$ is stored as either $x$ or $\tilde{x}$ by **rounding** to the nearest representable number, so

-   the largest possible error is $\frac{1}{2} \beta^{e-t}$,
-   which means that $| y - fl(y) | \le \frac{1}{2} \beta^{e-t}$.

## Machine precision

It follow from $y > x \ge .100 \ldots 00 \times \beta^e = \beta^{e-1}$ that

$$
 \frac{|y - fl(y)|}{|y|} < \frac{1}{2} \frac{\beta^{e-t}}{\beta^{e-1}} = \frac{1}{2} \beta^{1-t},
$$

and this provides a bound on the **relative error**: for any $y$

$$
 \frac{|y - fl(y)|}{|y|} < \frac{1}{2} \beta^{1-t}.
$$

The last term is known as **machine precision** or **unit roundoff** and is often called $eps$. This is obtained in Python with

```python
np.finfo(np.double).eps
```

### Examples

1.  The number system $(\beta, t, L, U) = (10, 2, -1, 2)$ gives

    $$
    eps = \frac{1}{2} \beta^{1-t} = \frac{1}{2} 10^{1-2} = 0.05.
    $$
2.  The number system $(\beta, t, L, U) = (10, 3, -3, 3)$ gives

    $$
    eps = \frac{1}{2} \beta^{1-t} =
    $$
3.  The number system $(\beta, t, L, U) = (10, 7, 2, 10)$ gives

    $$
    eps = \frac{1}{2} \beta^{1-t} =
    $$

### Why is this important?

Arithmetic operations are usually carried out as though infinite precision is available, after which the result is rounded to the nearest representable number.

This means that arithmetic cannot be completely trusted\
e.g. $x + y = ?$,

and the usual rules don't necessarily apply\
e.g. $x + (y+z) = (x+y) + z$?

### Example 1

Consider the number system $(\beta, t, L, U) = (10, 2, -1, 2)$ and take

$$
 x = .10 \times 10^2, \quad
 y = .49 \times 10^0, \quad
 z = .51 \times 10^0.
$$

-  In exact arithmetic $x + y = 10 + 0.49 = 10.49$ and $x + z = 10 + 0.51 = 10.51$.

-  In this number system rounding gives

    $$
    fl(x+y) = .10 \times 10^2 = x, \qquad
    fl(x+z) = .11 \times 10^2 \neq x.
    $$

(Note that $\frac{y}{x} < eps$ but $\frac{z}{x} > eps$.)

Evaluate the following expression in this number system.

$$
x+(y+y), \quad
(x+y)+y, \quad
x+(z+z), \quad
(x+z) +z.
$$

(Also note the benefits of adding the *smallest* terms first!)

### More examples (homework)

1.  Verify that a similar problem arises for the numbers

    $$
     x = .85 \times 10^0, \quad
     y = .3 \times 10^{-2}, \quad
     z = .6 \times 10^{-2},
    $$

	in the system $(\beta, t, L, U) = (10, 2, -3, 3)$.

2.  Given the number system $(\beta, t, L, U) = (10, 3, -3, 3)$ and $x = .100\times 10^3$, find nonzero numbers $y$ and $z$ from this system for which $fl(x+y) = x$ and $fl(x+z) > x$.

### An alternative definition of $eps$

**Machine precision** is the smallest positive number $eps$ such that $1 + eps > 1$, i.e. it is half the difference between $1$ and the next largest representable number.

Examples:

1.  For the number system $(\beta, t, L, U) = (10, 2, -1, 2)$,

    $$
     \begin{array}{ccl}
        & .11 \times 10^1 & \qquad \leftarrow {\text{next number}} \\
      - & .10 \times 10^1 & \qquad \leftarrow 1   \\ \hline
        & .01 \times 10^1 & \qquad \leftarrow 0.1
    \end{array}
    $$

	so $eps = \frac{1}{2}(0.1) = 0.05$.

2.  Verify that this approaches gives the previously calculated value for $eps$ in the number system given by $(\beta, t, L, U) = (10, 3, -3, 3)$.

## "Features" of finite precision

Overflow
:   the number is too large to be represented, e.g. multiply the largest representable number by 10. This gives `inf` (infinity) with `numpy.double`s and is usually "fatal".

Underflow
:   the number is too small to be reprsented, e.g. divide the smallest representable number by 10. This gives $0$ and may not be immediately obvious.

Divide by zero
:   gives a result of `inf`, but $\frac{0}{0}$ gives `nan` (not a number)

Divide by `inf`
:   gives $0.0$ with no warning

### Is this all academic?

**No!** There are many examples of major software errors that have occurred due to programmers not understanding the issues associated with computer arithmetic...

-   In February 1991, a [basic rounding error](https://www-users.cse.umn.edu/~arnold/disasters/patriot.html) within software for the US Patriot missile system caused it to fail, contributing to the loss of 28 lives.

-   In June 1996, the European Space Agency's Ariane Rocket exploded shortly after take-off: the error was due to failing to [handle overflow correctly](https://www.bbc.com/future/article/20150505-the-numbers-that-lead-to-disaster).

-   In October 2020, a driverless car drove straight into a wall due to [faulty handling of a floating point error](https://sinews.siam.org/Details-Page/a-new-ieee-754-standard-for-floating-point-arithmetic-in-an-ever-changing-world).

## Summary

-   There is inaccuracy in almost all computer arithmetic.

-   Care must be taken to minimise its effects, for example:

    -   add the smallest terms in an expression first;
    -   avoid taking the difference of two very similar terms;
    -   even checking whether $a = b$ is dangerous!

-   The usual mathematical rules no longer apply.

-   There is no point in trying to compute a solution to a problem to a greater accuracy than can be stored by the computer.

### Further reading

- Wikipedia: [Floating-point arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic)
- David Goldberg, [What every computer scientist should know about floating-point arithmetic](https://doi.org/10.1145/103162.103163), ACM Computing Surverys, Volume 23, Issue 1, March 1991.
- John D Cook, [Floating point error is the least of my worries](https://www.johndcook.com/blog/2011/11/01/floating-point-worries/), *online*, November 2011.
