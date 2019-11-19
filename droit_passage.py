#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import sys, brick_SL
import pilot, distance_sensor, color_sensor, robot_status, lcd_display, network
import os

class DPassage:
    def __init__(self):
        self.isAllowedToPass = False
        self.ip = "192.168.43.87"
        self.serv_sender = network.MessageSender(self.ip, serv_listener.sock)
        self.serv_listener = network.NetworkListener(self.ip)
        self.serv_listener.start

    #Assign the robot to the right way (green or orange) 
    #Color must be a dominantColor method return
    def addToWay(self, color):
        if (color == "RED" ):
            #Send the way and the ip to the server
            self.serv_sender.sendMessage("RED "+ self.ip)
            print("sent")
        elif (color == "GREEN"):
            #Send the way and the ip to the server
            self.serv_sender.sendMessage("GREEN "+ self.ip)
            print("sent")

    #The server give or not the right to pass (return true or false)
    def canPass(self):
        #The server return the IP and the message "YES"
        if (self.serv_listener.mailbox[0].split()[0] == self.ip and self.serv_listener.mailbox[0].split()[1] == "YES"):
            #Delete the message
            self.serv_listener.mailbox.pop(0)
            self.isAllowedToPass = True
            return self.isAllowedToPass
        else:
            self.isAllowedToPass = False
            return self.isAllowedToPass

    #Return true if the robot has passed the intersection and send it to the server
    def hasPassed(self, distReached, securityDistance):
        #distReached = Distance the robot reached since he started to pass through the conflict zone
        if(distReached >= securityDistance and self.isAllowedToPass == True):
            self.isAllowedToPass = False
            #send that the robot has passed to delete it in the way list on the server
            self.serv_sender.sendMessage(self.ip + " " + "GREEN " + "Passed")
            return True
        else:
            return False




