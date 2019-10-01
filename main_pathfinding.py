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


pilote = pilot.Pilot()
pilote_cs = color_sensor.CSensor()

while(1):
    path_color = pilote_cs.color()
    if(path_color==Color.WHITE):
        pilote.forwardTurn(70, 250)
    elif(path_color==Color.BLUE):
        pilote.forwardRelative(70)
    elif(path_color==Color.BLACK):
        pilote.forwardTurn(70, -250)
