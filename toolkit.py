char2int = {
    'A':  1, 'B':  2, 'C':  3, 'D':  4, 'E':  5, 'F':  6, 'G':  7, 'H':  8, 'I':  9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 
    'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

def encodeStr2Int(src:str) -> int:
    sum = 0
    for c in src:
        sum += char2int.get(c, 0)
    return sum

def isPalindrome(num:int) -> bool:
    strNum = str(num)
    if strNum == strNum[::-1]:
        return True
    return False

def isPrime(num:int) -> bool:
    if num in (0,1): 
        return False
    if num == 2:
        return True
    if num % 2 == 0: 
        return False
    for div in range(3, int((num**0.5))+1,2):
        if num % div == 0: 
            return False
    return True

def fibo(limit:int):
    n1, n2 = 1, 2
    while n1 + n2 < limit:
        yield n1 + n2
        n1, n2 = n2, n1 + n2
    print("n1 = {0}, n2 = {1}".format(n1, n2))

def primeGenerator(anchor:int):
    for num in range(2,anchor+1):
        if isPrime(num):
            yield num

def getMultiples(num:int) -> list:
    tempList = []
    if num in (0,1,2):
        tempList.append(num)
        return tempList
    div = 2
    while True:
        if num % div == 0:
            tempList.append(div)
            num /= div
        else:
            div += 1
        if num == 1: 
            break 
    return tempList

def count(item, lst:list) -> int:
    count = 0
    for elem in lst:
        if item == elem:
            count += 1
    return count

def sumOfSquaresGenerator(max:int):
    num = 1
    while True:
        yield num*num
        num += 1
        if num > max:
            break

def squareOfSum(max:int):
    return sum(list(range(1,max+1)))**2


def nthPrime(n:int,limit=10000000000) -> int:
    count = 0
    for prime in primeGenerator(limit):
        searched_prime = prime
        count += 1
        #print(count, prime)
        if count == n:
            return searched_prime

def isEven(num:int) -> bool:
    return num % 2 == 0

def collatzGenerator(num:int):
    while True:
        yield int(num)
        if num == 1:
            break
        if isEven(num):
            num /= 2
        else:
            num = 3 * num + 1

def fac(num:int) -> int:
    result = 1
    for x in range(1, num+1):
        result *= x 
    return result

def getDigitProduct(num) -> int:
    if type(num) == int:
        num = str(num)
    product = 1
    for digit in num:
        product *= int(digit)
    return product

def isPythTriplet(a:int, b:int, c:int) -> bool:
    return c**2 == a**2 + b**2

def triangleGenerator():
    num = 0
    x = 1
    while True:
        num += x
        x += 1
        yield num

def getDigitSum(num) -> int:
    if type(num) == int:
        num = str(num)
    sum = 0
    for digit in num:
        sum += int(digit)
    return sum

def isLeapYear(year:int) -> bool:
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            False
    if year % 4 == 0:
        return True
    return False

def getDivisors(num:int) -> list:
    divisors = []
    for div in range(num, 0, -1):
        if num % div == 0:
            divisors.append(int(num / div))
    return list(divisors)