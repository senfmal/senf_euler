"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""
import StopWatch as sw
import toolkit as tk

stopper = sw.StopWatch("Euler problem 0013 'Large sum' - Solution")

def solution01():
    sum = 0
    with open("input_0013.txt", "r") as input_file:
        for row in input_file:
            sum += int(row)
    print(sum)
    print(str(sum)[0:10])

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)