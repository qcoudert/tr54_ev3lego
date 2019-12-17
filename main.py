#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import sys, time
import pilot, color_sensor, lcd_display, robot_status, droit_passage, path_finding
from network import MessageSender, NetworkListener
import os

# Write your program here
brick.sound.beep(200, 100)
print(sys.version_info)

SWITCHER_WAY = {Color.RED: "ORANGE", Color.GREEN: "GREEN"}    #SWITCHER to get way from Color

dp= droit_passage.DPassage("192.168.43.178")                    #CHANGER L'IP AVANT LE LANCEMENT DU ROBOT
colorS = color_sensor.CSensor()                                 #Initialize the color sensor

m_path_finding = path_finding.PathFinding()
m_distance_tracker = robot_status.DistanceTracker(m_path_finding.pilote)

keepGoing = True
intersection = False
currentWay = "OOC"
old = time.time()

while(1):
    delta = time.time() - old 
    old = time.time()
    colorS.updateColorProbability()
    path_color = colorS.isRedOrGreen()

    if(currentWay == "OOC" and (path_color == Color.RED or path_color == Color.GREEN)):
        keepGoing = False                                               #The robot don't have the permission to cross
        intersection = True                                             #The robot is in an intersection
        currentWay = SWITCHER_WAY.get(path_color)                       #Current way the robot is
        m_distance_tracker.log = []                                     #Clear the distance tracker cache
        brick.display.text("COMING INTO " + currentWay)
    
    #Pas dans l'intersection et peut avancer
    if(not intersection and keepGoing):
        m_path_finding.keepGoing(delta)
        if(currentWay != "OOC"):
            m_distance_tracker.update()
            dist_traveled, time_traveled = m_distance_tracker.distanceTraveled()
            if(dp.hasPassed(dist_traveled)):
                brick.display.text("PASSED INTERSECTION")
                currentWay = "OOC"
        else:
            dp.stateInWay(currentWay)
    #Dans l'intersection et doit s'arrêter
    elif(intersection and not keepGoing):
        m_distance_tracker.update()
        [dist_traveled, time_traveled] = m_distance_tracker.distanceTraveled()
        intersection = m_path_finding.stopIntersection(delta, dist_traveled)

        if(dp.canPass()):
            keepGoing = True
            intersection = False
            brick.display.text("GOT CROSSING PERMISSION")
        dp.stateInWay(currentWay)

    #Dans l'intersectio et est arrêté
    elif(not intersection and not keepGoing):
        m_distance_tracker.update()
        if(dp.canPass()):
            keepGoing = True
            brick.display.text("GOT CROSSING PERMISSION")
        dp.stateInWay(currentWay)


"""while(1):
    
    if(colorS.dominantColor4() == "RED"):
        if(dp.canPass()):
            while(1):
                brick.display.text("ROUGE PEUT PASSER")
        brick.display.text("ORANGE")
        dp.stateInWay("ORANGE")
    if(colorS.dominantColor4() == "GREEN"):
        if(dp.canPass()):
            while(1):
                brick.display.text("VERT PEUT PASSER")
        dp.stateInWay("GREEN")
        brick.display.text("VERT")
    if(colorS.dominantColor4() == "BLUE"):
        dp.canPass()
        dp.stateInWay("OOC")
        brick.display.text("SORTIE")

    wait(1000)"""