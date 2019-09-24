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

<<<<<<< HEAD
pilote_leader = pilot.Pilot()
isMoving = False
while True:
    if isMoving:
        pilote_leader.stop()
        isMoving = False
    else:
        pilote_leader.forwardRelative(40)
        isMoving = True
    wait(3000)
=======
pilote_suiveur_run = pilot.Pilot()
pilote_suiveur_distance = distance_sensor.DistanceSensor()

while(1):
    dist = pilote_suiveur_distance.distance()
    pilote_suiveur_run.forwardRelative(50)
    print(dist)
    if(dist<=29):
        pilote_suiveur_run.stop()


>>>>>>> 291bf0cdc0848e139ca8253cde1e27e8ff6267e2
