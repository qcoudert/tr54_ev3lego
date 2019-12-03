#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import sys, brick_SL
import pilot, distance_sensor, color_sensor, lcd_display, robot_status, droit_passage
import os

# Write your program here
brick.sound.beep(200, 100)
print(sys.version_info)

dp= droit_passage.DPassage()
colorS = color_sensor.CSensor()
pilote = pilot.Pilot()

while(1):
    rgbColor = colorS.rgb()
    if(colorS.dominantColor(rgbColor))
    

