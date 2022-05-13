"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import StopWatch as sw
import toolkit as tk

stopper = sw.StopWatch("Euler problem 0005 'Smallest multiple' - Solution")
upperLimit = 20

def solution01():
    concerned_primes = tuple(tk.primeGenerator(upperLimit))
    primeCollection = {}
    for num in range(1, upperLimit+1):
        if num not in concerned_primes:
            primeCollection[num] = tk.getMultiples(num)
    print(concerned_primes)
    for key in primeCollection.keys():
        print("Key {0} -> ({1})".format(key, ','.join(str(x) for x in primeCollection[key])))
    solution = 1
    term = ""
    for prime in concerned_primes:
        max = 1
        for key in primeCollection.keys():
            max_check = tk.count(prime, primeCollection[key])
            if max_check > max:
                max = max_check
        solution *= prime**max
        term += str(prime**max)+" * "
    print("Solution is: {0} == {1}".format(solution, term[:-3]))


if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)