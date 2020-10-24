John Conway's Game of Life
==========================

This game is a cellular automaton based on the rules of Conway's Game of Life. It is intended to act as a very simple simulation of a real population.
It consists of a grid of "cells", each of which has 8 neighbors. 

*Rules and Explanation*
1. If a cell has fewer than 2 live neighbors, it dies.  
This simulates underpopulation.   
2. If a cell has 4 or more live neighbors, it dies.  
This simulates overpopulation.  
3. If a dead cell has exactly 3 live neighbors, it becomes alive.  
This simulates reproduction.  
4. Any cell that does not fall under any of these rules remains in its current state (alive or dead) until the next generation.  
  
*Turing Completeness*
The Game of Life is said to be Turing-complete, which means that it can be used to create a simulation of any Turing machine.  
That's a bit circular, but we can break it down further. A Turing machine is a computational model which can be used to manipulate symbols on an imaginary length of tape according to a simple algorithm.
The grid represents the tape, and the rules represent the algorithm. In order to prove that a system is Turing-complete, it only need to be able to simulate an arbitrary Turning-complete system; a Turing-complete system requires NOT and AND or OR gates, and access to memory.
In the case of the Game of Life, the various patterns and their interactions can be used to represent the logic gates and the cells represent memory access.  
More about logic gates in the Game of Life can be found in this publication: https://www.rennard.org/alife/CollisionBasedRennard.pdf

*My Code*
My version of the Game of Life works slightly differently others, because the grid wraps around, rather than having the edges as dead cells. Some well-known patterns will therefore produce the same results.  
This application is written in Python3 using the PyGame library (https://www.pygame.org/docs/) and converted to an executable using cx_Freeze (https://cx-freeze.readthedocs.io/en/latest/index.html).
