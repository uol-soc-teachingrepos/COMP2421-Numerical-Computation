---
title: "Lecture 01: Module introduction"
---


# Administration

All administration details in the [module handbook](https://uol-soc-teachingrepos.github.io/COMP2421-Numerical-Computation/)

<https://uol-soc-teachingrepos.github.io/COMP2421-Numerical-Computation>

## Contact

- Please contact me through MS Teams [24/25(1) COMP2421 Numerical Computation (32879)](https://teams.microsoft.com/l/team/19%3AebIX8peFnpoOnsp7izNiFJpuIXCN_9tdr9SP6LcRlq01%40thread.tacv2/conversations?groupId=ee227b6d-4176-427d-a494-11d538f55a5a&tenantId=bdeaeda8-c81d-45ce-863e-5232a535b7cb) - you will get a faster response there rather than email!
- Questions about content should go in the class team
- Responses in 48h (or out of office)
- No response out of working hours

## How to succeed?

- Read lecture notes **before lectures** -- [all available](https://uol-soc-teachingrepos.github.io/COMP2421-Numerical-Computation)
- Turn up to lectures with **pen and paper**
- Attempt **worksheet** before tutorial
- Let tutorial leader know where you are having problems before the session
- Attend tutorial every week - ask questions

## Marking expectations

| Mark   | Demonstrate                                    |
|--------|------------------------------------------------|
| 40-50% | Apply all algorithms                           |
| 50-60% | Apply modifications of algorithms              |
| 60-70% | Know how to explore algorithms computationally |
| 70%+   | Understand why algorithms are good/bad         |
| 95%+   | Read and write research papers in this area    |

## Lectures

2 hours per week in this room.

| Day | Time | Room |
|-|-|-|
| Mondays | 10:00-11:00 | Conference Auditorium 1 (GM.03) |
| Thursdays | 14:00-15:00 | Conference Auditorium 1 (GM.03) |

Leeds content delivered by Tom Ranner and Yongxing Wang.

*Please read the lecture content before the lecture*

<https://uol-soc-teachingrepos.github.io/COMP2421-Numerical-Computation>

## Tutorials and worksheets

These will be provided *weekly* throughout the semester.

1 hour per week (see timetable for your session)

Please attempt the worksheet before the session and bring your attempts with you!

Opportunity for **feedback** on learning.

<https://uol-soc-teachingrepos.github.io/COMP2421-Numerical-Computation>

## Virtual learning environment

As with all SoC  modules COMP2421 will make substantial use of the VLE:
[minerva.leeds.ac.uk](https://minerva.leeds.ac.uk)

This will include all:

- links to lecture notes and announcements
- all assessment information and feedback

[24/25(1) COMP2421 Numerical Computation (32879)](https://teams.microsoft.com/l/team/19%3AebIX8peFnpoOnsp7izNiFJpuIXCN_9tdr9SP6LcRlq01%40thread.tacv2/conversations?groupId=ee227b6d-4176-427d-a494-11d538f55a5a&tenantId=bdeaeda8-c81d-45ce-863e-5232a535b7cb)

(not email or personal teams message)

Please use this forum for all questions about content

# Assessment

| Title       | Release date | Due date             | Credit |
|-------------|--------------|----------------------|--------|
| Portfolio   | Mon 30 Sept  | weekly, Tuesday 2pm  | 20%    |
| Coursework  | Mon 2 Dec    | Wed 18 Dec, 2pm      | 80%    |
| Formative 1 | Mon 7 Oct    | Wed 23 Oct, 2pm      | 0%     |
| Formative 2 | Mon 4 Nov    | Wed 27 Nov, 2pm      | 0%     |

The dates are tentative at this stage and are subject to change.

## Portfolio (20%)

::: columns
::: column
- A question similar to each worksheet is available in minerva each week.
- You will have to submit your answer (and show your working) by the Tuesday 2pm deadline.
- You will receive two mark for giving the correct numerical and one mark for your working.
- The best 6 of 8 will count for your final mark.
- No late submission allowed.
:::

::: column
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
:::
:::

## Summative coursework (80%)

- A single piece of summative coursework will count for the majority of the assessment of this module (80%).
- You will be asked an open ended question which allows you to explore one of the topics from the module in detail.
- The rubric that you will be marked against is available in minerva.
- The coursework will be submitted via Gradescope.
- Usual late submission rules apply.

## Formative coursework

- There will be two additional formative courseworks which you can use to build skills related to the summative coursework.
- Submission will be through Feedback Fruits (via Minerva)
- We will use a combination of peer feedback and tutor feedback on both assignments

# Module content

## Objectives

- Understand how to compute with vectors and matrices.
- Appreciate the role numerical computation plays in CS.
- Choose a computational model appropriately, accounting for issues of accuracy, reliability and efficiency.
- Understand how to assess or measure the error in a numerical algorithm and be familiar with how such errors are controlled.

---

- Understand the fundamental techniques for the design of efficiency numerical algorithms.
- Demonstrate how these algorithms are analysed.
- Understand several advanced data structures, their efficient implementation and applications.
- Understand how these algorithms and data structures relate to the central practical problems of modern computer science.

## Syllabus

- **Vectors and matrices**: introduction and justification; vector and matrix operations; identity matrix; inverse of a matrix.

- **Approximation and errors**: modelling and mathematical modelling; discrete and continuous models; floating point and rounding errors; balancing accuracy and efficiency.

---

- **Static systems**: iterative methods for solving nonlinear scalar equations; methods for solving linear systems of equations; systems without unique solutions.

- **Evolving systems**: derivatives and rates of change; initial value problems; stability and convergence of computer models.

## Python

The programming for this module will be carried out using `python3`.

The latest available version of python is available via [Anaconda](https://www.anaconda.com/products/distribution).

Anaconda provides a full scientific Python distribution, including as standard tools for numerical analysis, data visualisation, image processing, and much more!

---

This scientific Python distribution is available on all School of Computer Science machines, specifically all SoCS Linux computers.

On a SoC Linux computer, you can run
```sh
> module add anaconda3
```
and you can test your python version with
```sh
> python --version
Python 3.12.4
```
<revealjs>
---
</revealjs>

We have access to a university managed online notebook service called Notable. Access is via the minerva module page.

<revealjs>
---
</revealjs>

Alternatively, you can install anaconda python on your own machine.

> Try this yourself! Make sure you can access a working version of python (version >= 3.10) and can import `numpy` and `scipy`.

More help will be given with python programming throughout the course.

## Relevance to Level 1 modules

This module builds upon material that you have already met in your first year. Prerequisites include:

- **COMP1421** Fundamental mathematical concepts
- **COMP1721** Object oriented programming

We also add to some of the material from:

- **COMP1212** Computer processors

## Relevance to Level 2 and 3 modules

The material covered here is important for a large number of subject areas including Scientific Computation, Computational Modelling, Machine Learning/AI, Computer Graphics, Quantum Computing.

This module is a pre-requisite for later modules in:

- **COMP3811** Computer graphics
- **COMP3910** Combinatorial optimisation
- **COMP3221** Parallel computation

<revealjs>
---
</revealjs>

Other modules that will benefit from material covered here:

- **COMP2721** Algorithms and data structures II (level 2)
- **COMP2611** Artificial intelligence (level 2)
- **COMP3631** Intelligent systems and robotics
- **COMP3611** Machine learning
- **COMP3940** Graph algorithms and approximation

## Books

Additional useful texts

- [Introduction to Linear Algebra](https://leeds.primo.exlibrisgroup.com/permalink/44LEE_INST/13rlbcs/alma991011421399705181) (Fifth Edition), Gilbert Strang, Wellesley-Cambridge Press, 2016. \
  with [MIT course material](https://web.mit.edu/18.06/www)

- [Scientific Computing: An Introductory Survey](https://leeds.primo.exlibrisgroup.com/permalink/44LEE_INST/13rlbcs/alma991009203099705181), T.M. Heath, McGraw-Hill, 2002. \
  some [lecture notes based on the book](http://heath.cs.illinois.edu/scicomp/notes/index.html)

<revealjs>
---
</revealjs>

- [Numerical Recipes in C++/C/FORTRAN](https://leeds.primo.exlibrisgroup.com/permalink/44LEE_INST/13rlbcs/alma991010465229705181): The Art of Scientific Computing, W.H. Press, S.A. Teukolsky, W.T. Vetterling and B.P. Flannery, Cambridge University Press, 2002/1993/1993.

- [Engineering Mathematics](https://leeds.primo.exlibrisgroup.com/permalink/44LEE_INST/13rlbcs/alma991019677711205181), K.A. Stroud, Macmillan, 2001. *available online*

Further more specific references will be given in each section of the notes.


# Numerical algorithms

- Numerical algorithms are those which operate on *floating point numbers*.

- They are used to provide solutions (or approximations to solutions) of mathematical models of "real world" problems.

<revealjs>
---
</revealjs>

- Such problems arise in a very wide range of applications (a few examples to follow).

- An important feature of these algorithms is that they need to account for the fact that arithmetic with floating point numbers is not exact!

## Applications I: Scientific and engineering computing

- Physical simulations are used for prediction in many different scientific and engineering areas.

- These models are hugely complex but also hugely important!

- Typically large physical domains are split up into small physical pieces which can be modelled more simply using techniques such as conservation laws.

## Airflow simulations

Car manufacturer and motor spots teams often perform computer simulations to test and optimise new designs.

<video width="100%" controls autoplay muted>
	<source src="../_static/video/lec01/LES.mp4" type="video/mp4">
	<a href="https://www.nektar.info/industry-relevant-implicit-les-via-spectral-hp-element-methods/"><img width="50%" alt="Airflow simulation example" src="https://www.nektar.info/wp-content/uploads/2021/05/D1-1-811x1024.jpg"></a>
</video>

*Video source: <https://youtu.be/-4gSS-UHWcc>*

## Economics

Most modern day economic forecasting involves performing numerical simulations.

<a title="Negative Space - Pexels account, CC0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Blur-chart-data-69760.jpg"><img width="100%" alt="Blur-chart-data-69760" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Blur-chart-data-69760.jpg/512px-Blur-chart-data-69760.jpg"></a>

## Weather forecasting

One of the most popular applications of numerical simulation in the UK today is in predicting tomorrow's weather.

<video width="100%" controls autoplay muted>
	<source src="../_static/video/lec01/weather.mp4" type="video/mp4">
	<a title="Mathias Krumbholz, CC BY-SA 3.0 &lt;https://creativecommons.org/licenses/by-sa/3.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Lightning_Pritzerbe_01_(MK).jpg"> <img width="100%" alt="Lightning Pritzerbe 01 (MK)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Lightning_Pritzerbe_01_%28MK%29.jpg/512px-Lightning_Pritzerbe_01_%28MK%29.jpg"></a>
</video>

<small>
	Video source: <https://youtu.be/5kpw5WeR5V4>
</small>

## Health care

Numerical simulation can be used both as an earlier step in clinical trials in order to reduce harm to animal or human participants or to predict how medical interventions will work in practice.

<video width="100%" controls autoplay muted>
	<source src="../_static/video/lec01/in-silico.mp4" type="video/mp4">
	<img width="100%" alt="Workflow of the FD-PASS in-silico trial" src="https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41467-021-23998-w/MediaObjects/41467_2021_23998_Fig1_HTML.png">
</video>

## Applications II: High performance graphics

- Realistic behaviour within games requires an accurate and efficient *physics engine*.

- Uses *Newton's laws of motion* to predict motion (e.g. projectiles, vehicles, etc) and impacts (e.g. crashes, collisions, etc).

- These are examples of dynamic models which must be solved and then rendered in "real time".

<revealjs>
---
</revealjs>

<video width="100%" controls autoplay muted>
  <source src="../_static/video/lec01/HPG.mp4" type="video/mp4" >
  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/YLsFN1mp2V8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen data-external="1"></iframe>
</video>

<small>
Student Showcase, High Performance Graphics and Game Engineering 2021, University of Leeds
</small>

## Applications III: Artificial intelligence

- Data mining requires complex models of very large data sets in order to extract useful information from them (e.g. Google PageRank)

- Self-driving cars, robotics and more rely on quick, accurate image processing and vision

- Much of AI boils down to *optimisation* which requires special numerical methods

[Unlock the Secrets of Machine Learning with Linear Algebra](https://www.univ.ai/blog/studying-linear-algebra)

## Robotics at Leeds

Many tasks in robotics are tested first in simulated environments where simulation plays a key role.

[![Robotics at Leeds](https://eps.leeds.ac.uk/images/Computing_postgraduate_researcher_Wisdom.JPG)](https://robotics.leeds.ac.uk/)

## Pipebots

<video width="100%" controls autoplay muted>
	<source src="../_static/video/lec01/pipebots.mp4" type="video/mp4">
</video>

<small>
Video source: <https://youtu.be/pppxa9MpoeY>
</small>

# See you Friday!

## { background-image=../_static/img/attendance.jpg data-background-size=contain }
