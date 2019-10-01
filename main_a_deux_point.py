#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import sys, brick_SL
import pilot, distance_sensor, color_sensor, robot_status, lcd_display, log

pilote_suiveur = pilot.Pilot()
distance_suiveur = distance_sensor.DistanceSensor()
color_suiveur = color_sensor.CSensor()
robot_suiveur = robot_status.RobotStatus(color_suiveur.color(), distance_suiveur.distance())
log_suiveur = log.Log(robot_suiveur)

D = 5
Ts = 100
a = 2
vitesse = 0

while(1) :
    dist = distance_suiveur.distance()
    vitesse = min(   max(2.5*(dist-20),min(max(a*(dist-D),0),vitesse)),50   )
    pilote_suiveur.forwardRelative(vitesse)
    robot_suiveur.updateStatus(color_suiveur.color(), distance_suiveur.distance())
    log_suiveur.writeLog()
    wait(Ts)