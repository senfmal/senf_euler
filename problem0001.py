# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time

limit = 1000
a, b = 3, 5

def main01():
    sum = 0
    for num in range(1, limit):
        if num % a == 0 or num % b == 0:
            sum += num
    print(sum)
    
def sumn(x, n):
    n //= x
    return n*x*(n+1) // 2
    
def main02():
    sum = sumn(a,limit-1) + sumn(b,limit-1) - sumn(a*b,limit-1)
    print(sum)


if __name__ == '__main__':
    start = time.time()
    main01()
    print("Time lapsed (1): ", str((time.time()-start)))
    start = time.time()
    main02()
    print("Time lapsed (2): ", str((time.time()-start)))