from pybricks.ev3devices import (InfraredSensor, UltrasonicSensor)
from pybricks.parameters import Port
from pybricks.tools import print

class DistanceSensor:

    def __init__(self):
        try:
            self.sensor = InfraredSensor(Port.S2)
            self.type = "infra"
        
        try:
            self.sensor = UltrasonicSensor(Port.S2)
            self.type = "ultra"
    
    
    def distance(self):
        #Infra
        if(self.type = "infra"):
            return self.sensor.distance()/2
        #Ultra
        if(self.type = "ultra"):
            return self.sensor.distance(False)