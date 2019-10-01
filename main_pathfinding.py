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


pilote = pilot.Pilot()
rSpeed = 50
angleSpeed = 0
pilote_cs = color_sensor.CSensor()
distance_sensor = distance_sensor.DistanceSensor()
collision_management = collision_management.CollisionManagement(distance_sensor)

while(1):
    vitesseMax = 70
    vitesse = collision_management.collisionSpeed(vitesseMax)
    path_color = pilote_cs.color()
    if(path_color==Color.WHITE):
        pilote.forwardTurn(vitesse, 100)
    elif(path_color==Color.BLUE):
        pilote.forwardRelative(vitesse)
    elif(path_color==Color.BLACK):
        pilote.forwardTurn(vitesse, -100)
