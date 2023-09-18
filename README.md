# ComputationalGeometry
Projects in C++ and Mathematica regarding numerical modeling of geometrical objects

The first two programs, 'Circle-Segment_Intersection.cpp' and 'Circle-Segment_Intersect.py' calculate the number of points of intersection for a circle and a segment on a plane. It takes an input from file, which consists of 7 real numbers (type double): coordinates of the circle centre (2 numbers), radius of the circle and coordinates of the left and right ends of the segment (2 pairs of numbers, respectively). Python version handles the exceptions with potential overflow and underflow issues.

Mathematica program called 'Desargues_blank.nb' represents a numerical modeling of Desargues's theorem (https://en.wikipedia.org/wiki/Desargues%27s_theorem), a statement in projective (as well as Euclidean) geometry: 'Two triangles are in perspective axially if and only if they are in perspective centrally'. The output is dynamically interactive: user can slide the vertices of both triangles across the pane canvas, and also move the centre of perspective by a slider.
