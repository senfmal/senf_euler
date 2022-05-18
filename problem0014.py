"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import StopWatch as sw
import toolkit as tk

stopper = sw.StopWatch("Euler problem 0014 'Longest Collatz sequence - Solution")
limit = 1000000 

def solution01():
    max_num, max_length = 0, 0
    for num in range(int(limit/2-1),2,-2):
        temp_length = len(list(tk.collatzGenerator(num)))
        if temp_length > max_length:
            max_length = temp_length
            max_num = num
    print(" → ".join(str(num) for num in list(tk.collatzGenerator(max_num))))

def experiment01():
    for num in range(1,14):
        print(" → ".join(str(x) for x in list(tk.collatzGenerator(num))[::-1]))

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.startNewStopper("Solution 2")
    experiment01()
    stopper.stopCurrentWatch()
    print(stopper)