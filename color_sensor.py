from pybricks.ev3devices import ColorSensor
from pybricks.parameters import (Port, Color)
from pybricks.tools import print

class CSensor:
    

    def __init__(self):
        self.sensor = ColorSensor(Port.S3)

        self.colorTab = []
        self.colorTab.append((0,90,0,0, Color.RED))
        self.colorTab.append((1,100,10,10, Color.RED))

        self.colorTab.append((0,0,90,0, Color.GREEN))
        self.colorTab.append((1,10,100,10, Color.GREEN))

        self.colorTab.append((0,0,0,0, Color.BLACK))
        self.colorTab.append((1,40,40,40, Color.BLACK))

        self.colorTab.append((1,60,60,60, Color.WHITE))
        self.colorTab.append((1,100,100,100, Color.WHITE))

    #def color(self):
    #    return self.sensor.color()

    def color(self):
        color = self.sensor.rgb()
        color_type = None
        for i in range (0, len(self.colorTab)/2) :
            test = True
            for j in range (0,3) :
                if(color[j] < self.colorTab[i*2][j+1] or color[j] > self.colorTab[i*2+1][j+1] ):
                    test = False
            if(test == True):
                color_type = self.colorTab[i*2][5]
                break
        return color_type