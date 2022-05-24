"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import StopWatch as sw
import toolkit as tk

stopper = sw.StopWatch("Euler problem 0022 'Names scores' - Solution")

def solution01():
    sum = 0
    with open("p022_names.txt","r") as names_file:
        names = names_file.read().split(',')
    names = list(sorted(names))
    for i in range(len(names)):
        sum += (i+1) * tk.encodeStr2Int(names[i])
    print(sum)

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)