#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import sys, brick_SL
import pilot, distance_sensor, color_sensor, lcd_display, robot_status
import os

# Write your program here
brick.sound.beep(200, 100)
print(sys.version_info)

pilote = pilot.Pilot()

pilote.forward(200)
tracker = robot_status.DistanceTracker(pilote)
tracker.update()
wait(2000)
pilote.forward(0)
tracker.update()

brick.display.text(str(tracker.distanceTraveled()))
while(1):
    None

