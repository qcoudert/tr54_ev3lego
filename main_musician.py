#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import sys, brick_SL, time
import pilot, distance_sensor, color_sensor, robot_status, lcd_display, collision_management, log, communication_serv, music


pilote = pilot.Pilot()
pilote_cs = color_sensor.CSensor()
distance_sensor = distance_sensor.DistanceSensor()
collision_management = collision_management.CollisionManagement(distance_sensor)
status = robot_status.RobotStatus(pilote_cs.color(), distance_sensor.distance(), 0)
journal = log.Log(status)

com_network = communication_serv.Server("192.168.43.178")


#Note, NoteFactory, Track, TrackPlayer, TimeUtils, TrackReader
music_reader = music.TrackReader()
music_track = music_reader.read('musics/score02/track01.txt')
music_player = music.TrackPlayer(music_track, 120)


index = 0

com_network.start()

while(1):
    music_player.play(1,time.time())
    if (len(com_network.listen()) > index+1):
        index = index + 1
        brick.display.text(str(com_network.listen()[index]))