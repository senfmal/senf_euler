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
