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
<<<<<<< HEAD
        return str(time.time()) + ";" + str(self.getDistance) + ";" + str(self.getColor) +"\n"
=======
        return str(time.time()) + ";" + str(self.getDistance()) + ";" + str(self.getColor()) +"\n"
>>>>>>> 96a4105095321b440a9cac9b443d4326eb61aad2
