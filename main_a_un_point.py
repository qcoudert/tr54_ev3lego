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

pilote_suiveur = pilot.Pilot()
distance_suiveur = distance_sensor.DistanceSensor()

D = 5
Ts = 3000
a = 2


while 1 == 1 :
    dist = distance_suiveur.distance()
    vitesse = max(min(50, a*(dist-D)) , 0)
    #pilote_suiveur.forward(vitesse*10)
    print(dist)
    wait(Ts)
    #vitesse : %(𝑡 + 𝑇𝑠) = max(min(50, 𝑎 × (𝑑(𝑡) − 𝐷)) , 0)