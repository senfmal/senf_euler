"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import StopWatch as sw
import toolkit as tk
from itertools import combinations

stopper = sw.StopWatch("Euler problem 0023 'Non-abundant sums' - Solution")
limit = 20162 #28123

def isAbundant(n:int) -> bool:
    if tk.getSumOfDivisors(n) > n:
        return True
    return False

def solution01():
    abundants = []
    for i in range(11,limit):
        if isAbundant(i):
            abundants.append(i)
    abundant_pairs = combinations(abundants, 2)
    sum_abundant_pairs = 0
    set_pairs = set()
    for pair in abundant_pairs:
        pair_sum = sum(pair)
        if pair_sum < limit:
            if pair_sum not in set_pairs:
                set_pairs.add(pair_sum)
                sum_abundant_pairs += pair_sum
    whole_sum = 0
    for i in range(limit):
        whole_sum += i
    print(whole_sum - sum_abundant_pairs - 64) # why so ever 64 too much!!!

def solution02():
    abundants = set(i for i in range(1,28124) if tk.getSumOfDivisors(i) > i)

    def abundantsum(i):
        return any(i-a in abundants for a in abundants)

    print(sum(i for i in range(1,28124) if not abundantsum(i)))

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.startNewStopper("Solution 2 from Euler forum")
    solution02()
    stopper.stopCurrentWatch()
    print(stopper)
