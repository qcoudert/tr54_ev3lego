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
Ts = 10
a = 2
vitesse = 0

while(1) :
    dist = distance_suiveur.distance()
    vitesse = min(   max(2.5*(dist-20),min(max(a*(dist-D),0),vitesse)),50   )
    pilote_suiveur.forwardRelative(vitesse)
    #print(dist)
    wait(Ts)
    #vitesse : %(𝑡 + 𝑇𝑠) = max(min(50, 𝑎 × (𝑑(𝑡) − 𝐷)) , 0)
