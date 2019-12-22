#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import Color
from pybricks.tools import print
import sys, time
import pilot, color_sensor, robot_status, droit_passage, path_finding
from network import MessageSender, NetworkListener

"""This module is the main loop of the robot during its execution.

The main goal of this module is to manage the informations and possibilities of every class to implement the crossing policy.
The most important classes used are : NetworkListener, MessageSender, PathFinding and CSensor. We really encourage any user to take a look at them."""

brick.sound.beep(200, 100)

SWITCHER_WAY = {Color.RED: "ORANGE", Color.GREEN: "GREEN"}      #SWITCHER to get way from Color

dp= droit_passage.DPassage("192.168.137.57")                    #THIS IP ADDRESS MUST BE CHANGED BEFORE ANY EXECUTION AFTER BEING CONNECTED
colorS = color_sensor.CSensor()                                 
m_path_finding = path_finding.PathFinding()
m_distance_tracker = robot_status.DistanceTracker(m_path_finding.pilote)

#The robot is initialized to not start in an intersection 
keepGoing = True
intersection = False
currentWay = "OOC"
old = time.time()

while(1):
    delta = time.time() - old 
    old = time.time()
    colorS.updateColorProbability()                                     #Store the current color in a list to get a probability of the current color
    path_color = colorS.isRedOrGreen()                                  #Using a different method to get the color green and red and reduce the number of false positives

    #If the robot is not in any intersection's way and detect the beginning of another way
    if(currentWay == "OOC" and (path_color == Color.RED or path_color == Color.GREEN)):
        keepGoing = False                                               #The robot don't have the permission to cross
        intersection = True                                             #The robot is in an intersection
        currentWay = SWITCHER_WAY.get(path_color)                       #Current way the robot is
        m_distance_tracker.flush()                                      #Clear the distance tracker cache
        brick.display.text("COMING INTO " + currentWay)
    
    #Not in the the instersection and can freely follow the path
    if(not intersection and keepGoing):
        m_path_finding.keepGoing(delta)
        #If the robot is going out of an intersection's way
        if(currentWay != "OOC"):
            m_distance_tracker.update()
            dist_traveled, time_traveled = m_distance_tracker.distanceTraveled()
            #If the distance is great enough to consider the robot out of the intersection
            if(dp.hasPassed(dist_traveled)):
                brick.display.text("PASSED INTERSECTION")
                currentWay = "OOC"                                      #Setting current way to "out of intersection"
        else:
            dp.stateInWay(currentWay)
    #In the intersection and don't have permission to cross it
    elif(intersection and not keepGoing):

        #Make the robot move toward the intersection until it's not safe anymore
        m_distance_tracker.update()
        [dist_traveled, time_traveled] = m_distance_tracker.distanceTraveled()
        intersection = m_path_finding.stopIntersection(delta, dist_traveled)

        #When the permission to cross is given by the server
        if(dp.canPass()):
            keepGoing = True                                            #The robot is free to go but not yet considered out of the intersection
            intersection = False
            brick.display.text("GOT CROSSING PERMISSION")
        dp.stateInWay(currentWay)

    #Waiting without moving in the intersection to get permission
    elif(not intersection and not keepGoing):
        m_distance_tracker.update()
        if(dp.canPass()):
            keepGoing = True                                            #The robot is free to go but not yet considered out of the intersection
            brick.display.text("GOT CROSSING PERMISSION")
        dp.stateInWay(currentWay)