"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
import StopWatch as sw

numDict = {
    1   : 'one', 2   : 'two', 3   : 'three', 4   : 'four', 5   : 'five', 6   : 'six', 7   : 'seven', 8   : 'eight', 9   : 'nine', 10  : 'ten',
    11  : 'eleven', 12  : 'twelve', 13  : 'thirteen', 14  : 'fourteen', 15  : 'fifteen', 16  : 'sixteen', 17  : 'seventeen', 18  : 'eighteen', 19  : 'nineteen',
    20  : 'twenty', 30  : 'thirty', 40  : 'forty', 50  : 'fifty', 60  : 'sixty', 70  : 'seventy', 80  : 'eighty', 90  : 'ninety'
}

stopper = sw.StopWatch("Euler problem 0017 'Number letter counts' - Solution")

def getFirstTwenty(num:int, printout=True) -> int:
    length = len(numDict.get(num,''))
    if printout:
        print(numDict.get(num,''))
    return length

def getTens(num:int, printout=True) -> int:
    length = 0
    tens = int(str(num)[0]+"0")
    ones = int(str(num)[1])
    length += len(numDict.get(tens,''))
    length += getFirstTwenty(ones,False)
    if printout:
        print("{0}-{1}".format(numDict.get(tens,''),numDict.get(ones,'')))
    return length

def solution01():
    length = 0
    #1 - 99
    for num in range(1,100):
        if num <= 20:
            length += getFirstTwenty(num, False)
        if len(str(num)) == 2 and num > 20:
            length += getTens(num, False)
    # 10 times range 1 - 99
    length *= 10
    # hundreds 1 - 9 minus one for each without an and, i.e. 100, 200, ..., 900
    for num in range(1, 10):
        length += (getFirstTwenty(num, False) + len("hundred") + len("and")) * 100 - len("and")
    # additional one thousand length
    length += len("one") + len("thousand")
    print(length)

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)