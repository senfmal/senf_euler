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
    def d(n:int) -> int:
        try:
            result = 0
            divs = list(tk.getDivisors(n))
            if type(divs) == int:
                return divs
            else:
                if len(divs) > 2:
                    for x in divs[:-1]:
                        result += x
                else:
                    result = divs[0]
                #result = sum(divs[0:-1]) if len(divs) > 2 else divs[0]
                return result
        except TypeError as e:
            print("Type Error occurred: {0} [Circumstance: n={1}]".format(e,n))

    def isAmicable(a:int, b:int) -> bool:
        if d(a) == b and d(b) == a and a != b:
            return True
        return False

    sum = 0
    for i in range(2,limit):
        if isAmicable(i, d(i)):
            print(i, d(i))
            sum += i
    print(sum)

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)