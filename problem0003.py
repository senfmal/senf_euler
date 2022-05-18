"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import StopWatch as sw
import toolkit as tk

stopper = sw.StopWatch("Euler problem 0003 'Largest prime factor' - Solution")
number = 600851475143

def solution01():
    upperBound = (int(number**0.5) // 2 * 2) + 1
    for div in range(upperBound,3,-2):
        if tk.isPrime(div): 
            if number % div == 0: 
                print("Solution is {0}".format(div))
                break

if __name__ == '__main__':
    stopper.startNewStopper("Standard solution")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)