import time
from pybricks.tools import print

class RobotStatus:
    """Object used to gather the different informations of the robot status

    Have only been used to get logs during the TPs. Sorry RobotStatus..."""

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
        self.pilot = pilot                          #We need the current Pilot for the robot to get the current speed of the robot
        self.lastRegisteredSpeed = pilot.speed      #Last known speed of the robot
        self.timeBegin = time.time()                #The date where the robot started to go at lastRegisteredSpeed
        self.log = []                               #List of the different TimedPositions the robot had from the initialization of this object

    def flush(self):
        """Reinitialize the object to track a new distance"""
        self.lastRegisteredSpeed = self.pilot.speed
        self.timeBegin = time.time()
        self.log = []

    def update(self):
        """Get the current speed of the robot and add it as a TimedPosition"""
        if(self.lastRegisteredSpeed!= self.pilot.speed * self.pilot.dist_proportion):
            self.timeEnd = time.time()
            tp = TimedPosition(self.timeBegin, self.timeEnd, self.lastRegisteredSpeed)
            self.log.append(tp)
            self.lastRegisteredSpeed = self.pilot.speed * self.pilot.dist_proportion
            self.timeBegin = self.timeEnd

    def distanceTraveled(self):
        """Compute the current distance traveled from the log list of TimedPosition
        
        We used the assomption that a complete turn from the wheel made the robot move for 10cm."""
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

class TimedPosition:
    """Object containing the speed of the robot between timeBegin and timeEnd
    
    This object is only used in DistanceTracker to fill the log list"""

    def __init__(self, timeBegin, timeEnd, speed):
        self.timeBegin = timeBegin
        self.timeEnd = timeEnd
        self.speed = speed