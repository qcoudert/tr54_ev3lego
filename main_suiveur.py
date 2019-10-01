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

pilote_suiveur_run = pilot.Pilot()
pilote_suiveur_distance = distance_sensor.DistanceSensor()
color_suiveur = color_sensor.CSensor()
robot_suiveur = robot_status.RobotStatus(color_suiveur.color(), pilote_suiveur_distance.distance(), 0)
log_suiveur = log.Log(robot_suiveur)

pilote_suiveur_run = pilot.Pilot()
pilote_suiveur_distance = distance_sensor.DistanceSensor()

while(1):
    dist = pilote_suiveur_distance.distance()
    vitesse = 50
    pilote_suiveur_run.forwardRelative(vitesse)
    if(dist<=15):
        vitesse = 0
        pilote_suiveur_run.stop()
    robot_suiveur.updateStatus(color_suiveur.color(), pilote_suiveur_distance.distance(), vitesse)
    log_suiveur.writeLog()
    wait(100)