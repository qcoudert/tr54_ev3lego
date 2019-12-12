#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import sys, brick_SL
import pilot, color_sensor, robot_status, lcd_display, network
import os, time

SECURITY_DISTANCE = 100                         #Distance to travel from the beginning of the way to the end of the intersection

class DPassage:
    def __init__(self, ip):
        self.isAllowedToPass = False
        self.ip = ip
        self.serv_listener = network.NetworkListener(self.ip)
        self.serv_listener.start()
        self.serv_sender = network.MessageSender(self.ip)

    #Send the state of the robot to the server 
    def stateInWay(self, state):
        if(state == "GREEN"):
            self.serv_sender.sendMessage("GREEN "+ self.ip + " " + str(time.time()))
        elif(state == "ORANGE"):
            self.serv_sender.sendMessage("RED "+ self.ip + " " + str(time.time()))
        elif(state == "OOC"):
            self.serv_sender.sendMessage("OOC "+ self.ip + " " + str(time.time()))
    
    #The server give or not the right to pass (return true or false)
    def canPass(self):
        self.isAllowedToPass = False
        if(self.serv_listener.mailbox):
            #The server return the IP and the message "YES"
            if (self.serv_listener.mailbox[0].split()[0] == self.ip and self.serv_listener.mailbox[0].split()[1] == "YES"):
                #Delete the message
                self.serv_listener.mailbox.pop(0)
                self.isAllowedToPass = True            
        
        return self.isAllowedToPass

    #Return true if the robot has passed the intersection and send it to the server
    def hasPassed(self, distReached):
        #distReached = Distance the robot reached since he started to pass through the conflict zone
        if(distReached >= SECURITY_DISTANCE and self.isAllowedToPass == True):
            self.isAllowedToPass = False
            #send that the robot has passed to delete it in the way list on the server
            self.serv_sender.sendMessage(self.ip + " " + "GREEN " + "Passed")
            return True
        else:
            return False

    




