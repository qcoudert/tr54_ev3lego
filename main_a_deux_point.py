#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import sys, brick_SL
import pilot, distance_sensor, color_sensor, robot_status, lcd_display, log

pilote_suiveur = pilot.Pilot()
distance_suiveur = distance_sensor.DistanceSensor()
robot_suiveur = robot_status.RobotStatus(color_suiveur.color(), distance_suiveur.distance())
log_suiveur = log.Log(robot_suiveur)

#D = 5
#a = 2
#vitesse = 0

Ts = 10
vitesse_old = 0
df = 5
da = 5
af = 2
aa = 2


while(1) :
    dist = distance_suiveur.distance()
    vitesse_freinage = min(max(af*(dist-df),0),50)
    vitesse_accel = min(max(aa*(dist-da),0,vitesse_old),50)
    vitesse = min(vitesse_freinage,vitesse_accel)
    #vitesse = min(   max(2.5*(dist-20),min(max(a*(dist-D),0),vitesse)),50   )
    pilote_suiveur.forwardRelative(vitesse)
    robot_suiveur.updateStatus(color_suiveur.color(), distance_suiveur.distance())
    log_suiveur.writeLog()
    #print(dist)
    wait(Ts)
    #vitesse : %(𝑡 + 𝑇𝑠) = max(min(50, 𝑎 × (𝑑(𝑡) − 𝐷)) , 0)
