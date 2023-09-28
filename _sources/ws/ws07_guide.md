# WS07 guide

KEY OBJECTIVES:

- Students should be able to compute using the midpoint method
- Students should understand that reducing the timestep should reduce (control) the error
- Advanced aim - deeper understanding of derivative geometrically

Worksheet:
<https://uol-soc-teachingrepos.github.io/COMP2421-Numerical-Computation/ws/ws03.html>

Partial solutions:
<https://uol-soc-teachingrepos.github.io/COMP2421-Numerical-Computation/ws/ws03_implemented.html>

Rough plan:

1. Ask how everyone is getting on with the course? Any problems?

Part a tutorial:

2. Work through the part a question. Encourage students to volunteer solutions
3. Talk about the errors in the method. How would students go about doing this?
4. More plotting if time too.

Part b tutorial:

2. Work through the part b implementations. Encourage students to volunteer solutions
3. Test solutions with part a answers. Show how to do this testing and plotting (again)

Part c tutorial:

2. Work through part c implementations. Encourage students to volunteer solutions
3. How else might we break the schemes?

    - also try d' = d^2 -> finite time blow up
    - d' = -2.3 * d for dt = 0.1 -> instability
