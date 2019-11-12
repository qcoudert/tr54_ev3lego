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

m_time_sync = time_sync.timeSync("CENTRALISED", 3)

com_network = network.NetworkListener("192.168.43.87")


#Note, NoteFactory, Track, TrackPlayer, TimeUtils, TrackReader
music_reader = music.TrackReader()
music_track = music_reader.read('musics/score01/violin1.txt') 
#music_track = music_reader.read('musics/score01/violin2.txt') 
<<<<<<< HEAD
music_track = music_reader.read('musics/score01/contrabass.txt') 
=======
#music_track = music_reader.read('musics/score01/contrabass.txt') 
>>>>>>> 4e379067354932fd6d469f928467bde360667c14
#'musics/score02/track03.txt')
music_player = music.TrackPlayer(music_track, 50, m_time_sync)


index = 0

com_network.start()


isStart = False
bipped = False
start_time = time.time()
while(1):
    if (isStart == False and com_network.mailbox):
        master_time = com_network.mailbox.pop()
        if(master_time != None):
            m_time_sync.masterTime(float(master_time))
            music_player.start()
            start_time = m_time_sync.getTimeSync()
            isStart = True

    if (isStart and com_network.mailbox):
        master_time = com_network.mailbox.pop()
        if(master_time != None):
            print(m_time_sync.getTimeSync())
            m_time_sync.masterTime(float(master_time))

    if(isStart and bipped == False and m_time_sync.getTimeSync() - start_time > 40):
        music_player.join()
        brick.sound.beep(500, 1000, 3)
        bipped = True

    
    

            
