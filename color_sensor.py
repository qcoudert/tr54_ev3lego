from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import print

class CSensor:

    def __init__(self):
        self.sensor = ColorSensor(Port.S3)

    def color(self):
        return self.sensor.color()