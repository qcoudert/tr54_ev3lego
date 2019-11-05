import time

class timeSync:
    """Class used to get a synchronized time when the robot is in a network"""
    def __init__(self, mode, number_robot):
        """Init the synchronized time class with a mode
        mode : String which contains the mode : ["CENTRALISED", "DECENTRALISED"]
        number_robot : number of robots in connection"""

        self.times = []
        self.delta_time = 0
        self.mode = mode
        self.number_robot = number_robot

    

    def addTime(self, robot_name, robot_time):
        self.times.append((robot_name, robot_time-time.tim()))

    def masterTime(self, master_time):
        self.delta_time = master_time - time.time()

    def getTimeSync(self):
        """Calculate and return the time synchrinized which the mode pass in initialisation.
        """
        if self.mode == "CENTRALISED" :
            return time.time() + self.delta_time
        else :
            if len(self.times) == number_robot-1:
                sum = 0
                for i in self.times:
                    sum = sum + i[1]
                average = sum / (number_robot - 1)
                self.delta_time = average - time.time()
                self.times = []
            return time.time() + self.delta_time
                    