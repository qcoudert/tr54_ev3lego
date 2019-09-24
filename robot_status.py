import time
class RobotStatus:

    def __init__(self, color, distance):
        self.color = color
        self.distance = distance

    def updateStatus(self, color, distance):
        self.color = color
        self.distance = distance

    def getColor(self):
        return self.color

    def getDistance(self):
        return self.distance

    def toString(self):
        return str(time.time()) + ";" + str(self.getDistance) + ";" + str(self.getColor) +"\n"