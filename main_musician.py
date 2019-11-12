#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import sys, brick_SL, time
import pilot, distance_sensor, color_sensor, robot_status, lcd_display, collision_management, log, music, time_sync, network


pilote = pilot.Pilot()
pilote_cs = color_sensor.CSensor()
distance_sensor = distance_sensor.DistanceSensor()
collision_management = collision_management.CollisionManagement(distance_sensor)
status = robot_status.RobotStatus(pilote_cs.color(), distance_sensor.distance(), 0)
journal = log.Log(status)
m_time_sync = time_sync.timeSync("CENTRALISED", 3)

com_network = network.NetworkListener("192.168.43.178")


#Note, NoteFactory, Track, TrackPlayer, TimeUtils, TrackReader
music_reader = music.TrackReader()
music_track = music_reader.read('musics/score01/violin1.txt') 
#'musics/score02/track03.txt')
music_player = music.TrackPlayer(music_track, 90, m_time_sync)


index = 0

com_network.start()


isStart = False
while(1):
    if (isStart == False and com_network.mailbox.pop(0) == "start"):
        music_player.start()
        isStart = True

    if (isStart):
        master_time = com_network.mailbox.pop(0)
        if(master_time != None):
            m_time_sync.masterTime(float(master_time))
            
