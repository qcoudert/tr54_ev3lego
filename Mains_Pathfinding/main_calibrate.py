#!/usr/bin/env pybricks-micropython

# /Mains_Pathfinding/main_pathfinding_time.py

# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../')

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
import color_sensor
import brick_SL, time
from pybricks.tools import print, wait, StopWatch

#Color : "WHITE = ", "BLACK", "BLUE", "RED", "GREEN"


#COLOR_BLACK = 1 Black color.
#COLOR_BLUE = 2 Blue color.
#COLOR_GREEN = 3 Green color.
#COLOR_YELLOW = 4 Yellow color.
#COLOR_RED = 5 Red color.
#COLOR_WHITE = 6 White color.
#COLOR_BROWN = 7 Brown color.

#COLORS = ["6", "1", "2", "5", "3"] # White, Black, Blue, Red, Green
COLORS = ["5", "3"] # Red, Green
KEY_ENTER = 28
color_cs = color_sensor.CSensor()

file = open("../color"+ ".csv","w")
file.write("")
file.close()
file = open("../color"+ ".csv","w+")
#file.write("Color,Type,R,G,B\n")

brick.sound.beep(200, 100)
# --------------------------- WHITE

for color in COLORS:
    wait(3000)
    brick.sound.beep(400, 100)
    mini = [255.0,255.0,255.0]
    maxi = [0.0,0.0,0.0]
    old = time.time()
    while(time.time()-old < 5):
        c = color_cs.rgb()
        for i in range(0, 2):
            mini[i] = min(mini[i], c[i])
            maxi[i] = max(maxi[i], c[i])

    white = color_cs.rgb()
    file.write(str(color)+",MIN,"+str(mini[0]-3)+","+str(mini[1]-3)+","+str(mini[2]-3)+"\n")
    file.write(str(color)+",MAX,"+str(maxi[0]+3)+","+str(maxi[1]+3)+","+str(maxi[2]+3)+"\n")
    brick.sound.beep(200, 100)


brick.sound.beep(100, 50)
file.close()


