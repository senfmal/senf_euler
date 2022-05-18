"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
import StopWatch as sw
import toolkit as tk

stopper = sw.StopWatch("Euler problem 0015 'Lattice paths' - Solution")
grid = 20

def solution01():
    n, m = grid, grid
    print ("Routes through a", n, "x", m, "grid", tk.fac(n+m) // tk.fac(n) // tk.fac(m))

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)