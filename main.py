#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import sys, brick_SL
import pilot, distance_sensor, color_sensor, robot_status, lcd_display, communication_serv
import os

# Write your program here
brick.sound.beep(200, 100)
print(sys.version_info)
i = 0
serv = communication_serv.Server("192.168.43.27")

while(1):
    serv.start()
    serv.queueMsg("poulet")
    
    if(serv.receivedMutex):
        serv.receivedMutex = False
        if(serv.peekStack(serv.receivedMsg)):
            data = serv.receivedMsg.pop()
            brick.display.text(data)
        serv.receivedMutex = True

    
    print(str(serv.receivedMutex))
    print(str(serv.toSendMutex))
    wait(500)


