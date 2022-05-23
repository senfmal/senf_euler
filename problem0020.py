"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import StopWatch as sw
import toolkit as tk

factorial = 100

stopper = sw.StopWatch("Euler problem 0020 'Factorial digit sum' - Solution")

def solution01():
    num = tk.fac(factorial)
    digitSum = tk.getDigitSum(num)
    print("{0}! = {1} ==> {2}".format(factorial, num, digitSum))

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)