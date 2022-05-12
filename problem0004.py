"""
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import StopWatch as sw

stopper = sw.StopWatch("Euler problem 0004 'Largest palindrome product' - Solution")

def isPalindrome(num):
    strNum = str(num)
    lenNum = len(strNum)
    if lenNum % 2 == 0:
        if strNum[0:lenNum//2] == strNum[-1:lenNum//2-1:-1]:
            return True
    if strNum[0:lenNum//2] == strNum[-1:lenNum//2:-1]:
        return True
    return False

def isPalindrome2(num):
    strNum = str(num)
    if strNum == strNum[::-1]:
        return True
    return False

def solution01():
    factor1 = 999
    factor2 = 999
    product = 0
    while True:
        if isPalindrome(factor1 * factor2):
            if factor1 * factor2 > product:
                product = factor1 * factor2
                break
        factor1 -= 1
    lowerBound1 = factor1
    for fact2 in range(factor2, lowerBound1, -1):
        for fact1 in range(lowerBound1, factor2):
            if isPalindrome(fact1*fact2):
                if fact1 * fact2 > product:
                    product, factor1, factor2 = fact1 * fact2, fact1, fact2
    print("Solution is: [product] -> {0}, [factors] -> {1} and {2}".format(product, factor1, factor2))

def solution02():
    factor1 = 999
    factor2 = 999
    product = 0
    while True:
        if isPalindrome2(factor1 * factor2):
            if factor1 * factor2 > product:
                product = factor1 * factor2
                break
        factor1 -= 1
    lowerBound1 = factor1
    for fact2 in range(factor2, lowerBound1, -1):
        for fact1 in range(lowerBound1, factor2):
            if isPalindrome2(fact1*fact2):
                if fact1 * fact2 > product:
                    product, factor1, factor2 = fact1 * fact2, fact1, fact2
    print("Solution is: [product] -> {0}, [factors] -> {1} and {2}".format(product, factor1, factor2))

if __name__ == "__main__":
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.startNewStopper("Solution 2 - alternate palindrome check")
    solution02()
    stopper.stopCurrentWatch()
    print(stopper)