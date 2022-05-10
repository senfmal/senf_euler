import StopWatch as sw

stopper = sw.StopWatch("Euler problem 0002 - Solution")

def fibo(limit):
    n1, n2 = 1, 2
    while n1 + n2 < limit:
        yield n1 + n2
        n1, n2 = n2, n1 + n2
    print("n1 = {0}, n2 = {1}".format(n1, n2))

def solution01():
    limit = 4000000
    sum = 2
    for x in fibo(limit):
        if x % 2 == 0:
            sum += x
    print(sum)

def solution02():
    a, b, c, accum = 0, 1, 0, 0
    while True:
        c = a + b
        if c > 4_000_000:
            break
        a = b
        b = c

        if c % 2 == 0:
            accum += c
    print(accum)


if __name__ == '__main__':
    stopper = sw.StopWatch("Euler problem 0002 - Solution")
    stopper.startNewStopper("Yield function")
    solution01()
    stopper.startNewStopper("Simple")
    solution02()
    stopper.stopCurrentWatch()
    print(stopper)
