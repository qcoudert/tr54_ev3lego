import csv

import sys

class Log :
    def __init__(self, robot_status) :
        self.file = open("logs.csv","w+")
        self.robot_status = robot
        
    def writeLog():
        self.file.write(self.robot_status.toString())
