"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import StopWatch as sw

stopper = sw.StopWatch("Euler problem 0019 'Counting Sundays' - Solution")

def solution01():
    import datetime as dt

    delta, c, targetDOW, targetDate = dt.timedelta(days=1), 0, 6, 1
    yS, mS, dS,   yE, mE, dE = 1901,1,1,   2000,12,31
    yearDelta = yE-yS  # number of years
    yS = (yS%400) + 400  # normalized and non-zero

    a = dt.datetime(yS, mS, dS)
    b = dt.datetime(yS+yearDelta, mE, dE)
    while a <= b:
        if a.day==targetDate and a.weekday()==targetDOW: 
            c+= 1
            delta = dt.timedelta(days=7)
        a+= delta

    print (["Mon","Tue","Wed","Thu","Fri","Sat","Sun"][targetDOW],
        "on day", targetDate, "of the month:", c)

if __name__ == '__main__':
    stopper.startNewStopper("Solution 1")
    solution01()
    stopper.stopCurrentWatch()
    print(stopper)