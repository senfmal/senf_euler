"""
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import StopWatch as sw
import toolkit as tk

stopper = sw.StopWatch("Euler problem 0006 'Sum square difference' - Solution")
max = 100



def solution01():
    squares = sum(list(tk.sumOfSquaresGenerator(max)))
    print(squares)
    sum_sq = tk.squareOfSum(max)
    print(sum_sq)
    print(sum_sq-squares)

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)