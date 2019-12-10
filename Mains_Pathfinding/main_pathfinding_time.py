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
import path_finding, robot_status

m_path_finding = path_finding.PathFinding()
m_distance_tracker = robot_status.DistanceTracker(m_path_finding.pilote)

keepGoing = True
intersection = False
old = time.time()
while(1):
    delta = time.time() - old 
    old = time.time()

    if(m_path_finding.path_color == Color.RED or m_path_finding.path_color == Color.GREEN):
        keepGoing = False
        intersection = True
    
    if(not intersection and keepGoing):
        m_path_finding.keepGoing(delta)
    elif(intersection and not keepGoing):
        m_distance_tracker.update()
        [dist_traveled, time_traveled] = m_distance_tracker.distanceTraveled()
        intersection = m_path_finding.stopIntersection(delta, dist_traveled)

    
    #robot_suiveur.updateStatus(color_suiveur.color(), distance_suiveur.distance(), vitesse)
    #log_suiveur.writeLog()

