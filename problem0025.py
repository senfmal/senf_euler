"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

import StopWatch as sw
import toolkit as tk

stopper = sw.StopWatch("Euler problem 0025 '1000-digit Fibonacci number' - Solution")
max_digits = 1000

def solution01():
    fibo_row = tk.fibo()
    i = 3
    while True:
        fibo_next = next(fibo_row)
        i += 1
        if len(str(fibo_next)) == max_digits:
            break
    print("{0} is the first fibonacci num with 1000 digits, index is: {1}".format(fibo_next, i))

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)