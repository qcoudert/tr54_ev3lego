#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import sys, brick_SL
import pilot, color_sensor, lcd_display, robot_status, droit_passage
from network import MessageSender, NetworkListener
import os

# Write your program here
brick.sound.beep(200, 100)
print(sys.version_info)


dp= droit_passage.DPassage("192.168.137.147")
colorS = color_sensor.CSensor()
#pilote = pilot.Pilot()



while(1):
    h = colorS.dominantSortingColor()
    if(h != "N/A"):
        #print(h)
        brick.display.text(h)
    
        
    
    """if(colorS.dominantColor4() == "GREEN"):
        brick.sound.beep(100, 200)"""
    """if(colorS.dominantColor(rgbColor) == "RED"):
        if(dp.canPass()):
            while(1):
                brick.display.text("ROUGE PEUT PASSER")
        dp.stateInWay("ORANGE")
    if(colorS.dominantColor(rgbColor) == "GREEN"):
        if(dp.canPass()):
            while(1):
                brick.display.text("VERT PEUT PASSER")
        dp.stateInWay("GREEN")
    if(colorS.dominantColor(rgbColor) == "BLUE"):
        dp.canPass()
        dp.stateInWay("OOC")

    wait(1000)"""
