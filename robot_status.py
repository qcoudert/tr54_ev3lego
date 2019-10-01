import time
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
