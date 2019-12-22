from pybricks.ev3devices import (InfraredSensor, UltrasonicSensor)
from pybricks.parameters import Port
from pybricks.tools import print

class DistanceSensor:
    """Interact with the distance sensor hardware to get the distance to the nearest obstacle in front of the robot"""

    def __init__(self):
        """The type of sensor is determined during the initialization."""

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
        """Get the distance between the robot and the nearest obstacle in front of it"""
        
        #Infra
        if(self.type == "infra"):
            return self.sensor.distance()/2
        #Ultra
        if(self.type == "ultra"):
            return self.sensor.distance(False)