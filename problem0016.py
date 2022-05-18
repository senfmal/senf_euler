"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""
import StopWatch as sw
import toolkit as tk

potency = 1000

stopper = sw.StopWatch("Euler problem 0016 'Power digit sum' - Solution")

def solution01():
    num = 2**potency
    digitSum = tk.getDigitSum(num)
    print("2**{0} = {1} ==> {2}".format(potency, num, digitSum))

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)