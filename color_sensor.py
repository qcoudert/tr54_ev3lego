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

    def color(self):
        return self.sensor.color()

    def color2(self):
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

    def rgb(self):
        return self.sensor.rgb()

    def hsv(self):
        r, g, b = rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0
        mx = max(r, g, b)
        mn = min(r, g, b)
        df = mx-mn
        if mx == mn:
            h = 0
        elif mx == r:
            h = (60 * ((g-b)/df) + 360) % 360
        elif mx == g:
            h = (60 * ((b-r)/df) + 120) % 360
        elif mx == b:
            h = (60 * ((r-g)/df) + 240) % 360
        if mx == 0:
            s = 0
        else:
            s = df/mx
        v = mx
        return h, s, v

    def dominantColor2(self):
        rgb = self.rgb()
        if(rgb[0] <30 and rgb[1] < 30 and rgb[2] <30):
            return Color.BLACK
        elif(rgb[0] + rgb[1] + rgb[2] > 180):
            return Color.WHITE  
        elif(rgb[1] > rgb[0] and rgb[1] > rgb[2]):
            return Color.GREEN
        elif(rgb[0] > rgb[1] and rgb[0] > rgb[2]):
               return Color.RED
        elif(rgb[2] > rgb[1] and rgb[2] > rgb[0]):
               return Color.BLUE

    def dominantColor(self, rgb):
        if(rgb[0] <30 and rgb[1] < 30 and rgb[2] <30):
            return "BLACK"
        elif(rgb[0] + rgb[1] + rgb[2] > 180):
            return "WHITE"   
        elif(rgb[1] > rgb[0] and rgb[1] > rgb[2]):
            return "GREEN"
        elif(rgb[0] > rgb[1] and rgb[0] > rgb[2]):
               return "RED"
        elif(rgb[2] > rgb[1] and rgb[2] > rgb[0]):
               return "BLUE"
