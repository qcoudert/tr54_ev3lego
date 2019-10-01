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
import os

# Write your program here
brick.sound.beep(200, 100)
print(sys.version)

pilote_suiveur_run = pilot.Pilot()
pilote_suiveur_color = color_sensor.CSensor()
pilote_suiveur_distance = distance_sensor.DistanceSensor()
pilote_suiveur_status = robot_status.RobotStatus(pilote_suiveur_color.color(), pilote_suiveur_distance.distance(), 0)

while(1):
    dist = pilote_suiveur_distance.distance()
    vitesse = 50
    pilote_suiveur_run.forwardRelative(50)
    print(dist)
    if(dist<=29):
        vitesse = 0
        pilote_suiveur_run.stop()
    pilote_suiveur_status.updateStatus(pilote_suiveur_color.color(), pilote_suiveur_distance.distance(), vitesse)


