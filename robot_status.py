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
        return "Distance: " + str(self.distance) + "\nCouleur: " + str(self.color)