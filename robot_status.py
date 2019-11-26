import time
from pybricks.tools import print
class RobotStatus:

    def __init__(self, color, distance, speed):
        self.color = color
        self.distance = distance
        self.speed = speed

    def updateStatus(self, color, distance, speed):
        self.color = color
        self.distance = distance
        self.speed = speed

    def getColor(self):
        return self.color

    def getDistance(self):
        return self.distance

    def getSpeed(self):
        return self.speed

    def toString(self):
        return str(time.time()) + ";" + str(self.getDistance()) + ";" + str(self.getColor()) + ";" + str(self.getSpeed())+"\n"


class DistanceTracker:

    def __init__(self, pilot):
        self.pilot = pilot
        self.lastRegisteredSpeed = pilot.speed
        self.timeBegin = time.time()
        self.log = []
        self.registeredChanges = []

    def update(self):
        if(self.lastRegisteredSpeed!= self.pilot.speed):
            self.timeEnd = time.time()
            if(self.timeEnd - self.timeBegin >= 1):                                             #If the speed changed and the time spent is higher than 1s we register a new timed position
                if(self.registeredChanges):                                                     #The speed may have changed during 1s, so we use the mean of all the registered values as the lastRegisterSpeed for this period
                    self.registeredChanges.append(self.lastRegisteredSpeed)
                    self.lastRegisteredSpeed = self.__arrayMean(self.registeredChanges)
                    self.registeredChanges = []
                tp = TimedPosition(self.timeBegin, self.timeEnd, self.lastRegisteredSpeed)
                self.log.append(tp)
                self.lastRegisteredSpeed = self.pilot.speed
                self.timeBegin = self.timeEnd
            else:
                self.registeredChanges.append(self.lastRegisteredSpeed)
                self.lastRegisteredSpeed = self.pilot.speed

    """Time to travel to the end at 850: 5.3"""
    """Time to travel to the end at 425: 8.80"""
    #10cm par tour de roue soit 10cm/360 soit 0.0277
    #La zone fait 120cm
    def distanceTraveled(self):
        totaltime = 0
        totaldist = 0
        for tp in self.log:
            timeElpased = tp.timeEnd - tp.timeBegin
            totaltime += timeElpased
            totaldist += (tp.speed * 0.0277) * timeElpased
            print("TP: " + str(timeElpased) + "s at " + str(tp.speed) + "for a total of " + str(totaldist))
        return [totaldist, totaltime]

    def __arrayMean(self, arr):
        size = len(arr)
        total = 0
        for a in arr:
            total += a
        return total/size

class TimedPosition:

    def __init__(self, timeBegin, timeEnd, speed):
        self.timeBegin = timeBegin
        self.timeEnd = timeEnd
        self.speed = speed