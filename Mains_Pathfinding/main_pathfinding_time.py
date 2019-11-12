#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import sys, brick_SL, time
import pilot, distance_sensor, color_sensor, robot_status, lcd_display, log, collision_management

pilote_suiveur = pilot.Pilot()
distance_suiveur = distance_sensor.DistanceSensor()
color_suiveur = color_sensor.CSensor()
robot_suiveur = robot_status.RobotStatus(color_suiveur.color(), distance_suiveur.distance(), 0)
log_suiveur = log.Log(robot_suiveur)


pilote = pilot.Pilot()
vitesseMax = 50
angleMax = 100
angleMin = 10
turningMaxTime = 1 # Time after what the turn will be at its maximum (in sec).
pilote_cs = color_sensor.CSensor()
distance_sensor = distance_sensor.DistanceSensor()
collision_management = collision_management.CollisionManagement(distance_sensor)

delta = 0
startTime = time.time()
phase = pilote_cs.color()
phaseTime = 0
phaseVirage = 1

old = time.time()
while(1):
    delta = time.time() - old 
    old = time.time()

    
    vitesseCollision = collision_management.collisionSpeed(vitesseMax)
    vitesse = min(vitesseCollision, vitesseMax*(0.5*phaseVirage+0.5))
    path_color = pilote_cs.color()
    if(path_color==Color.WHITE):
        pilote.forwardTurn2(vitesse, angleMin + (angleMax-angleMin) - angleMax * phaseVirage * phaseVirage)
    elif(path_color==Color.BLUE or path_color==Color.GREEN or path_color==Color.ORANGE):
        pilote.forwardRelative(vitesseCollision)
    elif(path_color==Color.BLACK):
        pilote.forwardTurn2(vitesse, -angleMax + (angleMax-angleMin) * phaseVirage * phaseVirage)

    if(phaseVirage - (1/turningMaxTime)*delta > 0):
        phaseVirage = phaseVirage - (1/turningMaxTime)*delta

    if(path_color != phase):
        phase = path_color
        phaseVirage = 1
    
    robot_suiveur.updateStatus(color_suiveur.color(), distance_suiveur.distance(), vitesse)
    log_suiveur.writeLog()

    print(vitesse)
