#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import sys, brick_SL
import pilot, distance_sensor, color_sensor, robot_status, lcd_display, collision_management
import time

pilote = pilot.Pilot()
rSpeed = 50
angleSpeed = 0
pilote_cs = color_sensor.CSensor()
distance_sensor = distance_sensor.DistanceSensor()
collision_management = collision_management.CollisionManagement(distance_sensor)

color = []
timeur1= []
timeur2= []
temoin1 = 1
temoin2 = 1
path_color = pilote_cs.color()
rgb_color = pilote_cs.rgb()
dominantColor = pilote_cs.dominantColor(rgb_color)
test1 = 0
test2 = 0
brick.display.text(str(rgb_color))
brick.display.text(str(dominantColor))
while(1):

    path_color = pilote_cs.color()
    rgb_color = pilote_cs.rgb()
    dominantColor = pilote_cs.dominantColor(rgb_color)
    """brick.display.text(str("----- "))
    brick.display.text(str(rgb_color))
    
    brick.display.text(str(dominantColor))
    wait(2000)"""


    while(dominantColor != "RED"):
        if(dominantColor == "RED"):
            test1 = test1+1
        vitesseMax = 100
        vitesse = collision_management.collisionSpeed(vitesseMax)
        path_color = pilote_cs.color()
        rgb_color = pilote_cs.rgb()
        dominantColor = pilote_cs.dominantColor(rgb_color)
        if(path_color==Color.WHITE):
           pilote.rotateR(0.2*vitesse)
           pilote.rotateL(vitesse)
           #pilote.forwardTurn(vitesse, 1.25*vitesse)
        elif(path_color==Color.BLUE):
            pilote.forwardRelative(vitesse)
        elif(path_color==Color.BLACK):
           #pilote.forwardTurn(vitesse, -1.25*vitesse)
            pilote.rotateL(0.2*vitesse)
            pilote.rotateR(vitesse)
    brick.sound.beep(500, 200)
    test1 = 0


    while(dominantColor != "GREEN"):
        vitesseMax = 60
        vitesse = collision_management.collisionSpeed(vitesseMax)
        path_color = pilote_cs.color()
        rgb_color = pilote_cs.rgb()
        dominantColor = pilote_cs.dominantColor(rgb_color)
        if(path_color==Color.WHITE):
            timeur1.append(time.time())
            if(timeur1[-1]-timeur1[0]>0.5):
                temoin2 = temoin2+0.3
                if(temoin2>3):
                    temoin2=3
                pilote.forwardTurn(vitesse*(1/temoin2), 1.25*vitesse)
                timeur1.clear
            pilote.forwardTurn(vitesse, 1.25*vitesse)
            color.append(1)
        elif(path_color==Color.BLUE):
            pilote.forwardRelative(vitesse)
            color.append(2)
        elif(path_color==Color.BLACK):
            timeur2.append(time.time())
            if(timeur2[-1]-timeur2[0]>0.5):
                temoin1 = temoin1+0.3 
                if(temoin1>3):
                    temoin1=3
                pilote.forwardTurn(vitesse*(1/temoin1), -1.25*vitesse)
                timeur2.clear
            pilote.forwardTurn(vitesse, -1.25*vitesse)
            color.append(3)

    brick.sound.beep(1000, 200)
    