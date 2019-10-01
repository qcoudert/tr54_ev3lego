#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import sys, brick_SL
import pilot, distance_sensor, color_sensor, robot_status, lcd_display
import time

pilote = pilot.Pilot()
rSpeed = 50
angleSpeed = 0
pilote_cs = color_sensor.CSensor()
temoin = 0
chemin = []


while(temoin<2):
    if(path_color==Color.GREEN):
        temoin = temoin + 1
    path_color = pilote_cs.color()
    if(path_color==Color.WHITE):
        pilote.forwardTurn(80, 50)
    elif(path_color==Color.BLUE):
        pilote.forwardRelative(90)
        chemin.append(2)
    elif(path_color==Color.BLACK):
        pilote.forwardTurn(80, -70)
