"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import StopWatch as sw
import toolkit as tk
from itertools import permutations

stopper = sw.StopWatch("Euler problem 0024 'Lexicographic permutations' - Solution")
req_pos = 1000000

elements = []
for i in range(10):
    elements.append(str(i))

def solution01():
    print(elements)
    perms = sorted(permutations(elements, len(elements)))
    solution = list(perms)[req_pos-1]
    print(''.join(str(x) for x in solution))

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)