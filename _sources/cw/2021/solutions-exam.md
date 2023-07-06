# Exam 2021/22 - Solutions

# Linear systems of equations \[13 marks\]

1.  Consider the system of linear equations

    $$
    \begin{aligned}
    2 x_1 - x_2 & = 1 \\
    - x_1 + x_2 + 3 x_3 & = 3 \\
    x_1 + x_3 & = 2.
    \end{aligned}
    $$

    a.  Apply one step of the Gauss-Seidel method from a starting guess of $(x_1^{(0)}, x_2^{(0)}, x_3^{(0)}) = (0, 0, 0)$. What is the third component of the solution, i.e. what is $x_3^{(1)}$? Give you answer to 3 decimal places. **\[3 marks\]**

       --> 1.500

       We compute that
       
       $$
        \begin{aligned}
        x_1^{(1)} & = x_1^{(0)} - \frac{1}{A_{11}} (b_1 - A_{11} x_1^{(0)} - A_{12} x_2^{(0)} - A_{13} x_3^{(0)}) \\
        & = 0 - \frac{1}{2} (1 - 2 \times 0 - (-1) \times 0 + 0 \times 0) = \frac{1}{2}. \\
        x_2^{(1)} & = x_2^{(0)} - \frac{1}{A_{22}} (b_2 - A_{21} x_1^{(1)} - A_{22} x_2^{(0)} - A_{23} x_3^{(0)}) \\
        & = 0 - \frac{1}{1} (3 - (-1) \times \frac{1}{2} - 1 \times 0 + 3 \times 0) = \frac{7}{2}. \\
        x_3^{(1)} & =  x_3^{(0)} - \frac{1}{A_{33}} (b_3 - A_{31} x_1^{(1)} - A_{32} x_2^{1} - A_{33} x_3^{(0)}) \\
        & = 0 - \frac{1}{1} (2 - 1 \times \frac{1}{2} - 0 \times \frac{7}{2} - 1 \times 0) = \frac{3}{2}.
        \end{aligned}
       $$

       So our solution is $\vec{x}^{(1)} = (\frac{1}{2}, \frac{7}{2}, \frac{3}{2})$.

    b.  What is the residual after one step of the Gauss-Seidel method? Give your answer to 5 significant figures. Is it larger, smaller or the same as the residual before the first iteration. **\[2 marks\]**

       --> The residual after one iteration is
       
       $$
        \| b - A (\frac{1}{2}, \frac{7}{2}, \frac{3}{2})^T \| = \| (\frac{7}{2}, - \frac{9}{2}, 0)^T \| = \sqrt{(\frac{7}{2})^2 + (-\frac{9}{2})^2 + 0^2} = \sqrt{130/4} = 5.701 (\text{to 3 d.p.}).
       $$
       
       \[1 mark\]

       The initial residual is
       
       $$
        \| b - A (0, 0, 0)^T \| = \| (1, 3, 2)^T \| = \sqrt{1 + 3^2 + 2^2} = \sqrt{14} = 3.7417 (\text{to 5 s.f.}).
       $$

       The residual is larger than the initial residual. \[1 mark\]

2.  a.  Find the line of best fit to the data set given by:

       $$
         \begin{array}{c|cccc}
         t & -1 & 0 & 1 \\
         \hline
         y & 0.5 & 1.2 & 1.5
         \end{array}
       $$
        
      What value for $y$ does your line predict for $t = 2$? Give your answer to 3 decimal places. **\[5 marks\]**

       -\> 2.067 \[5 marks\]

       We can formulate the problem trying to a straight line $y = m t + c$. At each point we have
       
       $$
         \begin{aligned}
         0.5 & = m \times 1 + c \\
         1.2 & = m \times 0 + c \\
         1.5 & = m \times 1 + c.
         \end{aligned}
       $$

       Let $\vec{x} = (m, c)^T$ then we can write this system as
       
       $$
         A \vec{x} = \vec{b}
       $$
       
       where
       
       $$
         A = \begin{pmatrix}
         -1 & 1 \\ 0 & 1 \\ 1 & 1
         \end{pmatrix}
         \quad
         \text{ and }
         \quad
         \vec{b} = \begin{pmatrix}
         0.5 \\ 1.2 \\ 1.0.
         \end{pmatrix}
       $$

       hen we can form the normal equations in order to find the best fit solution:
       
       $$
         A^T A \vec{x} = A^T \vec{b},
       $$
       
       with
       
       $$
         A^T A = \begin{pmatrix}
         2 & 0 \\ 0 & 3
         \end{pmatrix}
         \quad
         \text{ and }
         \quad
         A^T \vec{b} = \begin{pmatrix}
         1 \\ 3.2
         \end{pmatrix}.
       $$

       We can directly read off the solution as $(m, c) = (0.5, 1.066...)$. That is the line of best fit is $y = 0.5 t + 1.066....$.

       Evaluating at $t = 2$ give $y = 0.5 \times 2 + 1.066 = 2.066..$. To 3 decimal places, this is $2.067$.

    b.  What would happen to the system of equations if we tried to find a quadratic of best fit to this data set? Why? **\[3 marks, free response\]**

      --> Since the number of unknowns is equal to the number of data points, the system of equations is no longer singular and an exact solution may be found. \[2 marks for saying equations give unique solution (or equivalent), 1 mark for number of unknowns matches the number of data points (or equivalent)\]

# Derivatives and differential equations \[20 marks\]

3.  Consider the differential equation

    $$
    y'(t) = \cos(2 \pi y(t)), y(0) = 0,
    $$
    
    where $\cos$ here takes an argument in radians.

    a.  Estimate $y(1)$ by taking 2 steps of Euler's method. What is your estimate? Give your answer to 3 decimal places. **\[5 marks\]**

       --> 0.000 \[5 marks\]

       The update formula is
       
       $$
        y^{(i+1)} = y^{(i)} + \mathrm{d}t \cos(2 \pi y^{(i)}).
       $$

       Here we need $\mathrm{d}t = 1/2 = 0.5$. So we see that
       
       $$
        \begin{aligned}
        y^{(0)} & = 0 \\
        y^{(1)} & = 0 + 0.5 \times \cos(0) = 0.5 \\
        y^{(2)} & = 0.5 + 0.5 \times \cos(\pi) = 0.5 - 0.5 = 0.0.
        \end{aligned}
       $$

    b.  Estimate $y(1)$ by taking 2 steps of the midpoint method. What is your estimate? Give your answer to 3 decimal places **\[5 marks\]**

       --> 0.000

       The update formula is
       
       $$
        \begin{aligned}
        k^{(i+1)} & = y^{(i)} + 0.5 \mathrm{d}t \cos(2 \pi y^{(i)}) \\
        y^{(i+1)} & = y^{(i)} + \mathrm{d}t \cos(2 \pi k^{(i+1)}).
        \end{aligned}
       $$

       Here we need $\mathrm{d}t = 1/2 = 0.5$. So we see that
       
       $$
        \begin{aligned}
        k^{(1)} & = 0 + 0.5 \times 0.5 \times \cos(0) = 0 + 0.25 \times 1 = 0.25 \\
        y^{(1)} & = 0 + 0.5 \times \cos(\pi/2) = 0 + 0.5 \times 0 = 0 \\
        k^{(2)} & = 0 + 0.5 \times 0.5 \times \cos(0) = 0.25 \\
        y^{(2)} & = 0 + 0.5 \times \cos(\pi/2) = 0.
        \end{aligned}
       $$

4.  The following table shows results from using three different methods to solve a differential equation. The table headings are: `n` the number of time steps, `solution` the solution at the final time, `error` the error in the solution at the final time, `feval` the total number of right hand side evaluations. Comment on which is the best method and why by considering the accuracy and efficiency of each method. **\[10 marks, free response\]**

    **Method 1**

     | n   | solution   | error        | feval |
     |-----|------------|--------------|-------|
     | 10  | 1.84329291 | 1.193005e+00 | 10    |
     | 20  | 1.27939891 | 6.291111e-01 | 20    |
     | 40  | 0.97259084 | 3.223030e-01 | 40    |
     | 80  | 0.81335232 | 1.630645e-01 | 80    |
     | 160 | 0.73229686 | 8.200902e-02 | 160   |
     | 320 | 0.69141145 | 4.112361e-02 | 320   |

    **Method 2**

	| n   | solution   | error        | feval |
	|-----|------------|--------------|-------|
	| 10  | 0.71550491 | 6.521707e-02 | 20    |
	| 20  | 0.66578277 | 1.549493e-02 | 40    |
	| 40  | 0.65411381 | 3.825967e-03 | 80    |
	| 80  | 0.65124139 | 9.535477e-04 | 160   |
	| 160 | 0.65052604 | 2.382036e-04 | 320   |
	| 320 | 0.65034738 | 5.953945e-05 | 640   |

    **Method 3**

	| n   | solution   | error        | feval |
	|-----|------------|--------------|-------|
	| 10  | 0.65151227 | 1.224427e-03 | 40    |
	| 20  | 0.65036050 | 7.265670e-05 | 80    |
	| 40  | 0.65029232 | 4.483929e-06 | 160   |
	| 80  | 0.65028812 | 2.793655e-07 | 320   |
	| 160 | 0.65028786 | 1.744664e-08 | 640   |
	| 320 | 0.65028784 | 1.090202e-09 | 1280  |

    --> For method 1, we see that the error reduces by a factor of 2 each time we double the number of time steps (i.e. the error is $O(\mathrm{d}t)$) and we do one rhs evaluation per time step. \[2 marks\]

    For method 2, we see that the error reduces by a factor of 4 each time we double the number of time steps (i.e. the error is $O(\mathrm{d}t^2)$) and we do two rhs evaluations per time step. \[2 marks\]

    For method 3, we see that the error reduces by a factor of 16 each time we double the number of time steps (i.e. the error is $O(\mathrm{d}t^4)$) and we do four rhs evaluations per time step. \[2 marks\]

    We see that method 3 is the best method \[1 mark\] since this requires the fewest rhs evaluations for the smallest error \[3 marks (or equivalent)\].

# Nonlinear solvers \[22 marks\]

5.  We want to solve the quadratic equation

    $$
    f(x) = x^2 -(m+\frac{1}{m}) x + 1 = 0
    $$
    
    for large values of $m$. The exact solutions are $m$ and $\frac{1}{m}$.

    a.  We can first try to solve this equation using the quadratic formula. For a quadratic $f(x) = a x^2 + b x + c$, the formula gives the roots as
    
       $$
         x^* = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.
       $$

       We implement this in python as:

       ``` python
       def quad(a, b, c):
           r = np.sqrt(b * b - 4 * a * c)
           return (- b + r) / (2 * a), (- b - r) / (2 * a)
       ```

       With $m = 10^8$ this gives the roots

        >>> quad(1.0, -1.0e8-1.0e-8, 1.0)
        (100000000.0, 1.4901161193847656e-08)

       What is the relative error for the smaller root? Give your answer to 3 decimal places. **\[2 marks\]**

       -\> Relative error is
       
       $$
        \frac{|1.4901161193847656 \times 10^{-8} - 10^{-8}|}{10^{-8}}
        = 0.4901161193847656  = 0.490 \text{to 3 d.p.}
       $$

    b.  Use the bisection method starting from the bracket $[0, 0.1]$ to estimate the smaller root for $m = 10^8$. How many iterations are required to find the solution to a relative error of less than $0.5$? **\[5 marks\]**

       --> 22 iterations \[5 marks\]

       The bisection method will return bracket $[0, 0.1/2^{j}]$ at iteration stage $j$ until $0.1/2^j < 10^{-8}$. So the right hand end of the bracket is:

	   | $j$ | $0.1/2^{j}$    |
	   |-----|----------------|
	   | 0   | 1.00000000e-01 |
	   | 1   | 5.00000000e-02 |
	   | 2   | 2.50000000e-02 |
	   | 3   | 1.25000000e-02 |
	   | 4   | 6.25000000e-03 |
	   | 5   | 3.12500000e-03 |
	   | 6   | 1.56250000e-03 |
	   | 7   | 7.81250000e-04 |
	   | 8   | 3.90625000e-04 |
	   | 9   | 1.95312500e-04 |
	   | 10  | 9.76562500e-05 |
	   | 11  | 4.88281250e-05 |
	   | 12  | 2.44140625e-05 |
	   | 13  | 1.22070313e-05 |
	   | 14  | 6.10351563e-06 |
	   | 15  | 3.05175781e-06 |
	   | 16  | 1.52587891e-06 |
	   | 17  | 7.62939453e-07 |
	   | 18  | 3.81469727e-07 |
	   | 19  | 1.90734863e-07 |
	   | 20  | 9.53674316e-08 |
	   | 21  | 4.76837158e-08 |
	   | 22  | 2.38418579e-08 |
	   | 23  | 1.19209290e-08 |
	   | 24  | 5.96046448e-09 |

       Using $x_C = 0.1/2^{j+1}$, for $j \le 23$ as the estimate, we see the relative error is less than $0.490...$ if

       $$
        \frac{| 10^{-8} - 0.1/2^{j+1} |}{10^{-8}} < 0.490...
       $$

       Which happens for $j = 22$.

       We can confirm this by doing the iteration:

	   | it | xC             | rel error      |
	   |----|----------------|----------------|
	   | 0  | 5.00000000e-02 | 4.99999900e+06 |
	   | 1  | 2.50000000e-02 | 2.49999900e+06 |
	   | 2  | 1.25000000e-02 | 1.24999900e+06 |
	   | 3  | 6.25000000e-03 | 6.24999000e+05 |
	   | 4  | 3.12500000e-03 | 3.12499000e+05 |
	   | 5  | 1.56250000e-03 | 1.56249000e+05 |
	   | 6  | 7.81250000e-04 | 7.81240000e+04 |
	   | 7  | 3.90625000e-04 | 3.90615000e+04 |
	   | 8  | 1.95312500e-04 | 1.95302500e+04 |
	   | 9  | 9.76562500e-05 | 9.76462500e+03 |
	   | 10 | 4.88281250e-05 | 4.88181250e+03 |
	   | 11 | 2.44140625e-05 | 2.44040625e+03 |
	   | 12 | 1.22070313e-05 | 1.21970312e+03 |
	   | 13 | 6.10351563e-06 | 6.09351562e+02 |
	   | 14 | 3.05175781e-06 | 3.04175781e+02 |
	   | 15 | 1.52587891e-06 | 1.51587891e+02 |
	   | 16 | 7.62939453e-07 | 7.52939453e+01 |
	   | 17 | 3.81469727e-07 | 3.71469727e+01 |
	   | 18 | 1.90734863e-07 | 1.80734863e+01 |
	   | 19 | 9.53674316e-08 | 8.53674316e+00 |
	   | 20 | 4.76837158e-08 | 3.76837158e+00 |
	   | 21 | 2.38418579e-08 | 1.38418579e+00 |
	   | 22 | 1.19209290e-08 | 1.92092896e-01 |

    c.  Use Newton's method starting from the initial value $x^{(0)} = 0$ to estimate the smaller root for $m = 10^8$. How many iterations are required to find the solution to a relative error of less than $0.5$? Note that the derivative of $f(x)$ is
    
       $$
        f'(x) = 2 x - (m+\frac{1}{m}).
       $$
        
       **\[5 marks\]**

       --> 1 iteration \[5 marks\]

       The update formula is
       
       $$
        x^{(i+1)} = x^{(i)} - \frac{f(x^{(i)})}{f'(x^{(i)})}
        = x^{(i)} - \frac{(x^{(i)})^2 - (m+1/m) x^{(i)} + 1}{2 x^{(i)} - (m+1/m)}.
       $$

       So starting from $x^{(0)} = 0$, we have
       
       $$
        x^{(1)} = 0 - \frac{0^2 - (m+1/m) \times 0 + 1}{2 \times 0 -  (m+1/m)} = \frac{1}{m+1/m}.
       $$
       
       For $m = 10^8$, we have $x^{(1)} = \frac{1}{10^8+10^{-8}}$.

       The relative error after one iteration is
       
       $$
        \frac{| \frac{1}{10^8 + 10^{-8}} - 10^{-8} | }{10^{-8}} \approx 10^{-16} < 0.490...
       $$

    d.  Which method is best for this problem? Why? You should comment on the accuracy and efficiency of each of the three approaches (from parts a-c). **\[7 marks, free response\]**

       -\>

       Using the method from part a, the exact formula, gives a highly inaccurate answer quite cheaply - the cost is similar to one evaluation of $f(x)$. \[1 mark for comment on accuracy, 1 mark for cost\]

       Using the method from part b, the bisection method, gives an accurate answer (and we could increase this accuracy by taking more iterations) but it takes a lot of iterations to get there. This requires 22 iterations which equates to 23 evaluations of $f(x)$. \[1 mark for comment on accuracy, 1 mark for cost\]

       Using the method for part c, Newton's method, gives a very accurate answer very quickly. This is because we start very close to the true root. This requires $1$ evaluation of $f(x)$ and $1$ evaluation of $f'(x)$. \[1 mark for comment on accuracy, 1 mark for cost\]

       The best method is Newton's method since it is both most accurate and most efficient. \[1 mark for Newton with reason\]

    e.  Suppose we repeated this analysis for $m = 1$. What would you expect to happen for each method? Why? **\[3 marks, free response\]**

       --> The same rounding errors would not happen for the quadratic formula since we no longer have the difference of similar numbers. \[1 mark\]

       The bisection method would not converge since we cannot find a starting bracket. \[1 mark\]

       Newton's method will converge but much slower. We won't be able to achieve a relative error the same as the exact formula since similar size rounding errors will start to take place of Newton's method too. Furthermore, the method will converge more slowly since we don't have a simple root. \[1 mark for converge but slower with reason\]

# Summary \[5 marks\]

6.  Choose an algorithm from the course which you think is useful. Give an example of where you expect to use this algorithm in the future. Why is this method useful for this application? **\[5 marks, free response\]**

    --> \[1 mark for any algorithm from the course. 2 marks for any relevant application 2 marks for why suitable.\]
