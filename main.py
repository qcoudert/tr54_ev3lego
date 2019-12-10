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
pilote = pilot.Pilot()



while(1):
    rgbColor = colorS.rgb()
    brick.display.text(colorS.dominantColor3(rgbColor))
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
"""

listener = NetworkListener("192.168.137.147")
listener.start()
sender = MessageSender("192.168.137.147")

while(1):
    sender.sendMessage("Hello")
    wait(500)
