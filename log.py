import csv, time

import sys

class Log :
    """Class used to print the RobotStatus into a csv file

    Have not been used for anything else than TPs. Sorry Log...
    """
    
    def __init__(self, robot_status) :
        self.file = open("logs"+ str(time.time()) + ".csv","w+")
        self.file.write("Time;Distance;Couleur;Vitesse\n")
        self.robot_status = robot_status
        
    def writeLog(self):
        self.file.write(self.robot_status.toString())
