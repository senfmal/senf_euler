"""
Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import StopWatch as sw

stopper = sw.StopWatch("Euler problem 0001 - Solution")
limit = 1000
a, b = 3, 5

def solution01():
    sum = 0
    for num in range(1, limit):
        if num % a == 0 or num % b == 0:
            sum += num
    print(sum)
    
def sumn(x, n):
    n //= x
    return n*x*(n+1) // 2
    
def solution02():
    sum = sumn(a,limit-1) + sumn(b,limit-1) - sumn(a*b,limit-1)
    print(sum)


if __name__ == '__main__':
    stopper.startNewStopper("Brute Force")
    solution01()
    stopper.startNewStopper("Sophisticated")
    solution02()
    stopper.stopCurrentWatch()
    print(stopper)