"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
                                    a2 + b2 = c2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import StopWatch as sw
import toolkit as tk

stopper = sw.StopWatch("Euler problem 0009 'Special Pythagorean triplet' - Solution")
wanted_sum_abc = 1000

def isPythTriplet(a:int, b:int, c:int) -> bool:
    return c**2 == a**2 + b**2

def isWantedSum(a:int, b:int, c:int) -> bool:
    return wanted_sum_abc == a + b + c

def solution01():
    for a in range(1,wanted_sum_abc // 2):
        for b in range(1,wanted_sum_abc // 3):
            for c in range(1, wanted_sum_abc // 2):
                if isWantedSum(a, b, c) and isPythTriplet(a, b, c):
                    print("Solution: {0} --> a: {1}, b: {2}, c: {3}".format(a*b*c, a, b, c))

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)