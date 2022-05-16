"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
import StopWatch as sw
import toolkit as tk

stopper = sw.StopWatch("Euler problem 0010 'Summation of primes' - Solution")
max = 2000000

def solution01():
    print(sum(list(tk.primeGenerator(max-1))))

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)