import time

class StopWatch:
    def __init__(self, name):
        self.name = name
        self.saved_times = {}
        self.resetCurrentWatch()

    def resetCurrentWatch(self):
        self.current_stopper = None
        self.current_start = None
        self.current_stop = None

    def startNewStopper(self, id):
        if self.current_stopper is not None:
            self.stopCurrentWatch()
        self.current_stopper = id
        print("{0} stopper started".format(self.current_stopper))
        self.current_start = time.time()
        self.current_stop = None
    
    def stopCurrentWatch(self):
        if self.current_stop is None:
            self.current_stop = time.time()
            print("{0} stopper stopped".format(self.current_stopper))
        self.saved_times[self.current_stopper] = self.current_stop - self.current_start
        self.resetCurrentWatch()

    def displayTime(self, id):
        print("Time lapsed for {0}: {1} ms".format(id, StopWatch.mSec(self.saved_times[id])))

    def __str__(self):
        heading = "Result for stop watch '{0}'".format(self.name)
        print('-'.join('' for x in range(len(heading)+1)))
        print(heading)
        print('-'.join('' for x in range(len(heading)+1)))
        for watch in self.saved_times.keys():
            self.displayTime(watch)
        return ""

    @classmethod
    def mSec(Class,secs):
        return secs * 1000
