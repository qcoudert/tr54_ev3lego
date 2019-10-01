import csv, time

import sys

class Log :
    def __init__(self, robot_status) :
        self.file = open("logs"+ str(time.time()) + ".csv","w+")
        self.file.write("Time;Distance;Couleur;Vitesse\n")
        self.robot_status = robot_status
        
    def writeLog(self):
        self.file.write(self.robot_status.toString())
