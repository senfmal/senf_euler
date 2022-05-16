"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
import StopWatch as sw
import toolkit as tk

stopper = sw.StopWatch("Euler problem 0007 '10001st prime' - Solution")
max = 10001

def solution01():
    print(tk.nthPrime(max))

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)