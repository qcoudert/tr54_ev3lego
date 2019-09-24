from pybricks.ev3devices import (InfraredSensor, UltrasonicSensor)
from pybricks.parameters import Port
from pybricks.tools import print

class DistanceSensor:

    def __init__(self):
        self.sensor = InfraredSensor(Port.S2)
    
    
    def distance(self):
        return self.sensor.distance()