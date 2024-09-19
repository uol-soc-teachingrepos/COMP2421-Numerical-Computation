---
title: COMP2421 Numerical computation
---
# Module information

**All dates below are subject to change.**

Module staff:

```{table}
||||
|-|-|-|
| Dr Thomas Ranner (Tom, he/him) | T.Ranner@leeds.ac.uk | Module leader |
| Dr Yongxing Wang (Yongxing, he/him) | Y.Wang3@leeds.ac.uk | Lecturer |
```

Support for the module is provided through MS Teams. The teams group for this module is: [24/25(1) COMP2421 Numerical Computation (32879)]( https://teams.microsoft.com/l/team/19%3AebIX8peFnpoOnsp7izNiFJpuIXCN_9tdr9SP6LcRlq01%40thread.tacv2/conversations?groupId=ee227b6d-4176-427d-a494-11d538f55a5a&tenantId=bdeaeda8-c81d-45ce-863e-5232a535b7cb)

## Course contents

-   **Vectors and matrices**: introduction and justification; vector and matrix operations; identity matrix; inverse of a matrix.

-   **Approximation and errors**: modelling and mathematical modelling; discrete and continuous models; floating point and rounding errors; balancing accuracy and efficiency.

-   **Static systems**: iterative methods for solving nonlinear scalar equations; methods for solving linear systems of equations; systems without unique solutions.

-   **Evolving systems**: derivatives and rates of change; initial value problems; stability and convergence of computer models.

## Module components

### Lectures

2 hours per week

```{table}
| Day | Time | Room |
|-|-|-|
| Mondays | 10:00-11:00 | Conference Auditorium 1 (GM.03) |
| Thursdays | 14:00-15:00 | Conference Auditorium 1 (GM.03) |
```

### Tutorials

1 hour per week face to face (see timetable)

Opportunity to get **feedback** on learning

### Worksheets

These will be provided *weekly* throughout the semester.

## Assessment

```{table} Assessment schedule 2024
| Title       | Release date | Due date             | Credit |
|-------------|--------------|----------------------|--------|
| Portfolio   | Mon 30 Sept  | weekly, Tuesday 2pm  | 20%    |
| Coursework  | Mon 2 Dec    | Wed 18 Dec, 2pm      | 80%    |
| Formative 1 | Mon 7 Oct    | Wed 23 Oct, 2pm      | 0%     |
| Formative 2 | Mon 4 Nov    | Wed 27 Nov, 2pm      | 0%     |
```

 The dates are tentative at this stage and are subject to change.

### Portfolio (20%)

- A question similar to each worksheet is available in minerva each week.
- You will have to submit your answer (and show your working) by the Tuesday 2pm deadline.
- You will receive two marks for giving the correct numerical and one mark for your working.
- The best 6 of 8 will count for your final mark.
- No late submission allowed.

```{table} Portfolio deadlines 2024

| Section | Deadline         |
|---------|------------------|
| 1       | Tue 15 Oct, 2pm  |
| 2       | Tue 22 Oct, 2pm  |
| 3       | Tue 5 Nov, 2pm   |
| 4       | Tue 12 Nov, 2pm  |
| 5       | Tue 19 Nov, 2pm  |
| 6       | Tue 26 Nov, 2pm  |
| 7       | Tue 3 Dec, 2pm   |
| 8       | Tue 10 Dec, 2pm  |
```

### Summative coursework (80%)

A single piece of summative coursework will count for the majority of the assessment of this module (80%).
You will be asked an open ended question which allows you to explore one of the topics from the module in detail.
The rubric that you will be marked against is available in minerva.
The coursework will be submitted via Gradescope.
Usual late submission rules apply.

### Formative coursework

There will be two additional formative courseworks which you can use to build skills related to the summative coursework.
Submission and feedback mechanism details to be confirmed.

## Syllabus

This is a rough breakdown of topics to be covered this semester. Please note that this is not entirely fixed and I cannot guarantee to follow this precise structure.

```{table} Teaching plan

| Lecture         | Topic                                        |
|-----------------|----------------------------------------------|
| 1 (week 1)      | Introduction                                 |
| 2               | Vectors and matrices                         |
| 3 (week 2)      | Floating point numbers                       |
| 4               | Introduction to systems of linear equations  |
| 5 (week 3)      | Solving triangular systems                   |
| 6               | Gaussian elimination                         |
| 7 (week 4)      | LU factorisation                             |
| 8               | The effects of finite precision              |
|                 | *reading week*                               |
| 9 (week 6)      | Iterative methods                            |
| 10              | Sparse matrices and stopping criteria        |
| 11 (week 7)     | Derivatives and rates of change              |
| 12              | Euler's method                               |
| 13 (week 8)     | Midpoint method                              |
| 14              | Systems of differential equations            |
| 15 (week 9)     | Introduction to nonlinear equations          |
| 16              | Newton's method                              |
| 17 (week 10)    | Quasi-Newton methods                         |
| 18              | Robust linear solvers                        |
| 19/20 (week 11) | Special topics/Formative coursework feedback |
```

### Tutorials plan

Weekly tutorials should will support you in your learning. See your timetable for when and where you should attend.

| Week | Topic                                       |
|------|---------------------------------------------|
| 1    | Maths preliminary                           |
| 2    | Introduction to python                      |
| 3    | Floating point number systems               |
| 4    | Triangular systems and Gaussian elimination |
|      | *reading week*                              |
| 6    | LU Factorisation and iterative methods      |
| 7    | Sparse systems/pivoting                     |
| 8    | Derivatives and Euler’s method              |
| 9    | Other time stepping                         |
| 10   | Bisection and Newton's method               |
| 11 | Other root finding |

## Contact

- Please contact me through MS Teams: [24/25(1) COMP2421 Numerical Computation (32879)]( https://teams.microsoft.com/l/team/19%3AebIX8peFnpoOnsp7izNiFJpuIXCN_9tdr9SP6LcRlq01%40thread.tacv2/conversations?groupId=ee227b6d-4176-427d-a494-11d538f55a5a&tenantId=bdeaeda8-c81d-45ce-863e-5232a535b7cb)
- Questions about content should go in the class team
- Responses in 48h (or out of office)
- No response out of working hours

## Reference materials

The programming for this module will be carried out using `python3`.

-   For general Python, refer to your first-year teaching materials.

-   For a refresher course in Python:

    - <https://developers.google.com/edu/python/?hl=en>
	- <https://learnxinyminutes.com/docs/python/>

-   For `numpy`, `scipy` etc:

    - <http://scipy-lectures.github.io>
    - <https://github.com/jrjohansson/scientific-python-lectures>

## Links

-   Module catalogue:

	- COMP2421 <https://webprod3.leeds.ac.uk/catalogue/dynmodules.asp?Y=202425&M=COMP-2421>\
    - XJCO2421 <https://webprod3.leeds.ac.uk/catalogue/dynmodules.asp?Y=202425&M=XJCO-2421>
