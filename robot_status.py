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
    """This class is used to track the distance that have been covered by the robot since its instanciation
    
    You must instanciate this class using a Pilot object that is used to control the robot.
    Once instanciate, the object must be updated every iteration with DistanceTracker.update()
    To find the distance travelled by the robot, call DistanceTracker.distanceTraveled()"""

    def __init__(self, pilot):
        self.pilot = pilot
        self.lastRegisteredSpeed = pilot.speed
        self.timeBegin = time.time()
        self.log = []

    def update(self):
        if(self.lastRegisteredSpeed!= self.pilot.speed * self.pilot.dist_proportion):
            self.timeEnd = time.time()
            tp = TimedPosition(self.timeBegin, self.timeEnd, self.lastRegisteredSpeed)
            self.log.append(tp)
            self.lastRegisteredSpeed = self.pilot.speed * self.pilot.dist_proportion
            self.timeBegin = self.timeEnd

    """Time to travel to the end at 850: 5.3"""
    """Time to travel to the end at 425: 8.80"""
    #10cm par tour de roue soit 10cm/360 soit 0.0277
    #La zone fait 120cm
    def distanceTraveled(self):
        totaltime = 0
        totaldist = 0

        lastp = TimedPosition(self.timeBegin, time.time(), self.lastRegisteredSpeed)
        self.log.append(lastp)      #The non complete TimedPostion that could miss in the distance assertion is added to the array

        for tp in self.log:
            timeElpased = tp.timeEnd - tp.timeBegin
            totaltime += timeElpased
            totaldist += (tp.speed * 0.0277) * timeElpased
        
        self.log.pop()              #The non complete TimedPosition is deleted from the array

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