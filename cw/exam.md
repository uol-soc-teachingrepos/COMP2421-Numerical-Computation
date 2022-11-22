# Exam 2021/22

*This exam formed part of the assessment of this module that students took in 2021/22. You may wish to use it to help in your revision for the final exam.*

*Support is provided through the MS Class Team. [Solutions are available for checking answers](./solutions-exam.md).*

This exam is worth 60% of the credit of this module.

For each answer you should give the information required by the question. Questions marked **free response** require full sentences. Other questions only require a short answer (usually one number).

## Linear systems of equations \[13 marks\]

1.  Consider the system of linear equations

    $$
    \begin{aligned}
    2 x_1 - x_2 & = 1 \\
    - x_1 + x_2 + 3 x_3 & = 3 \\
    x_1 + x_3 & = 2.
    \end{aligned}
    $$

    a.  Apply one step of the Gauss-Seidel method from a starting guess of $(x_1^{(0)}, x_2^{(0)}, x_3^{(0)}) = (0, 0, 0)$. What is the third component of the solution, i.e. what is $x_3^{(1)}$? Give you answer to 3 decimal places. **\[3 marks\]**

    b.  What is the residual after one step of the Gauss-Seidel method? Give your answer to 3 decimal places. Is it larger, smaller or the same as the residual before the first iteration. **\[2 marks\]**

2.  a.  Find the line of best fit to the data set given by:

     $$
         \begin{array}{c|cccc}
         t & -1 & 0 & 1 \\
         \hline
         y & 0.5 & 1.2 & 1.5
         \end{array}
     $$

	 What value for $y$ does your line predict for $t = 2$? Give your answer to 3 decimal places. **\[5 marks\]**

    b.  What would happen to the system of equations if we tried to find a quadratic of best fit to this data set? Why? **\[3 marks, free response\]**

## Derivatives and differential equations \[20 marks\]

3.  Consider the differential equation

    $$
    y'(t) = \cos(2 \pi y(t)), y(0) = 0,
    $$

	where $\cos$ here takes an argument in radians.

    a.  Estimate $y(1)$ by taking 2 steps of Euler's method. What is your estimate? Give your answer to 3 decimal places. **\[5 marks\]**

    b.  Estimate $y(1)$ by taking 2 steps of the midpoint method. What is your estimate? Give your answer to 3 decimal places. **\[5 marks\]**

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

## Nonlinear solvers \[22 marks\]

5.  We want to solve the quadratic equation

    $$
	f(x) = x^2 -(m+\frac{1}{m}) x + 1 = 0
	$$

	for large values of $m$. The exact solutions are $m$ and $\frac{1}{m}$.

    a.  We can first try to solve this equation using the quadratic formula. For a quadratic $f(x) = a x^2 + b x + c$, the formula gives the roots as $$
         x^* = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.
         $$

       We implement this in python as:

       ``` python
       def quad(a, b, c):
           r = np.sqrt(b * b - 4 * a * c)
           return (- b + r) / (2 * a), (- b - r) / (2 * a)
       ```

       With $m = 10^8$ this gives the roots

       ```
       >>> quad(1.0, -1.0e8-1.0e-8, 1.0)
       (100000000.0, 1.4901161193847656e-08)
	   ```

       What is the relative error for the smaller root? Give your answer to 3 decimal places. **\[2 marks\]**

    b.  Use the bisection method starting from the bracket $[0, 0.1]$ to estimate the smaller root for $m = 10^8$. How many iterations are required to find the solution to a relative error of less than $0.5$? **\[5 marks\]**

    c.  Use Newton's method starting from the initial value $x^{(0)} = 0$ to estimate the smaller root for $m = 10^8$. How many iterations are required to find the solution to a relative error of less than $0.5$? Note that the derivative of $f(x)$ is

	   $$
       f'(x) = 2 x - (m+\frac{1}{m}).
       $$ **\[5 marks\]**

    d.  Which method is best for this problem? Why? You should comment on the accuracy and efficiency of each of the three approaches (from parts a-c). **\[7 marks, free response\]**

    e.  Suppose we repeated this analysis for $m = 1$. What would you expect to happen for each method? Why? **\[3 marks, free response\]**

## Summary \[5 marks\]

6.  Choose an algorithm from the course which you think is useful. Give an example of where you expect to use this algorithm in the future. Why is this method useful for this application? **\[5 marks, free response\]**
