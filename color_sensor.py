from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import print


class CSensor:

    def __init__(self):
        self.sensor = ColorSensor(Port.S3)

    def color(self):
        return self.sensor.color()

    def rgb(self):
        return self.sensor.rgb()

    def hsv(self, rgb):
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

