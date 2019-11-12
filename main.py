#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import sys, brick_SL
import pilot, distance_sensor, color_sensor, robot_status, lcd_display, network
import os

# Write your program here
brick.sound.beep(200, 100)
print(sys.version_info)
serv_listener = network.NetworkListener("192.168.43.27")
serv_sender = network.MessageSender("192.168.43.27", serv_listener.sock)
serv_listener.start()
i=0
while(1):
    i+=1
    serv_sender.sendMessage("poulet" + str(i))
    if(serv_listener.mailbox):
        brick.display.text(serv_listener.mailbox.pop(0))
    wait(1000)


