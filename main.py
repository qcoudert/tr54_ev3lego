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
