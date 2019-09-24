from pybricks import ev3brick as brick
from ev3dev2.led import Leds
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch

class BrickSL:

    def __init__(self):
        self.leds = Leds()

    def lightShow(self):
        self.leds.all_off()
        wait(10)
        self.leds.set_color('LEFT', 'RED')
        brick.sound.beep(500, 200)
        wait(200)
        self.leds.set_color('RIGHT', 'ORANGE')
        brick.sound.beep(600, 200)
        wait(200)
        self.leds.set_color('LEFT', 'YELLOW')
        brick.sound.beep(400, 200)
        wait(200)
        self.leds.set_color('RIGHT', 'AMBER')
        brick.sound.beep(500, 200)