"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import StopWatch as sw
import toolkit as tk

stopper = sw.StopWatch("Euler problem 0021 'Amicable numbers' - Solution")
limit = 10000

def solution01():
    def isAmicable(a:int, b:int) -> bool:
        if tk.getSumOfDivisors(a) == b and tk.getSumOfDivisors(b) == a and a != b:
            return True
        return False

    sum = 0
    for i in range(2,limit):
        if isAmicable(i, tk.getSumOfDivisors(i)):
            print(i, tk.getSumOfDivisors(i))
            sum += i
    print(sum)

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)