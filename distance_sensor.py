from pybricks.ev3devices import (InfraredSensor, UltrasonicSensor)
from pybricks.parameters import Port
from pybricks.tools import print

class DistanceSensor:

    def __init__(self):
        self.type = "none"
        try:
            self.sensor = InfraredSensor(Port.S2)
            self.type = "infra"
        except:
            try:
                self.sensor = UltrasonicSensor(Port.S2)
                self.type = "ultra"
            except:
                print("No distance sensor")
    
    
    def distance(self):
        #Infra
        if(self.type == "infra"):
            return self.sensor.distance()/2
        #Ultra
        if(self.type == "ultra"):
            return self.sensor.distance(False)