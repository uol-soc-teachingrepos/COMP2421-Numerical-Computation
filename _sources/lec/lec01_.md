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

## Question about assessments

vevox poll

# Module content

## Objectives

- Implement simple numerical algorithms accurately and present results in a variety of forms

- Understand how to assess/measure the error in a numerical algorithm and be familiar with how such errors are controlled

- Use, data-based arguments to justify choosing a computational algorithm appropriately, accounting for issues of accuracy, reliability and efficiency

## Syllabus

- **Vectors and matrices**: introduction and justification; vector and matrix operations; identity matrix; inverse of a matrix.

- **Approximation and errors**: modelling and mathematical modelling; discrete and continuous models; floating point and rounding errors; balancing accuracy and efficiency.

both with Yongxing Wang

---

- **Static systems**: iterative methods for solving nonlinear scalar equations; methods for solving linear systems of equations; systems without unique solutions.

- **Evolving systems**: derivatives and rates of change; initial value problems; stability and convergence of computer models.

both with me (Tom Ranner)

## Python

The programming for this module will be carried out using `python3`.

The latest available version of python is available via [Anaconda](https://www.anaconda.com/products/distribution).

Anaconda is available through the module system on School linux machines.

We have access to a university managed online notebook service called **Notable**. Access is via the minerva module page.

More help will be given with python programming throughout the course.

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

Additional reading list available through Minerva.

There are a lot of other online resources. Some are linked from the module book.

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

# See you Friday!

## { background-image=../_static/img/attendance.jpg data-background-size=contain }
