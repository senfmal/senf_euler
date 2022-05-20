"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""
import StopWatch as sw

stopper = sw.StopWatch("Euler problem 0067 'Maximum path sum II' - Solution")

def solution01():
    table = [list(map(int, s.split())) for s in open('p067_triangle.txt').readlines()]

    for row in range(len(table)-1, 0, -1):
        for col in range(0, row):
            table[row-1][col]+= max(table[row][col], table[row][col+1])

    print ("Maximum top-bottom total in triangle", table[0][0])
if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)