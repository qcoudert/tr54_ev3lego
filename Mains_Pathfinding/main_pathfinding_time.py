#!/usr/bin/env pybricks-micropython

# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../')

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import brick_SL, time
import path_finding

m_path_finding = path_finding.PathFinding()

old = time.time()
while(1):
    delta = time.time() - old 
    old = time.time()
    m_path_finding.keepGoing(delta)
    
    #robot_suiveur.updateStatus(color_suiveur.color(), distance_suiveur.distance(), vitesse)
    #log_suiveur.writeLog()

