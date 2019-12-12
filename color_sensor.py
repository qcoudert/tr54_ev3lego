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
        rgb = self.sensor.rgb()
        r = (rgb[0]/100)*255
        g = (rgb[1]/100)*255
        b = (rgb[2]/100)*255
        return r,g,b

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
        elif(rgb[0] + rgb[1] + rgb[2] > 510):
            return Color.WHITE  
        elif(rgb[1] > rgb[0] and rgb[1] > rgb[2]):
            return Color.GREEN
        elif(rgb[0] > rgb[1] and rgb[0] > rgb[2]):
               return Color.RED
        elif(rgb[2] > rgb[1] and rgb[2] > rgb[0]):
               return Color.BLUE

    def dominantColor(self):
        rgb = self.rgb()
        if(rgb[0] <30 and rgb[1] < 30 and rgb[2] <30):
            return "BLACK"
        elif(rgb[0] + rgb[1] + rgb[2] > 510):
            return "WHITE"   
        elif(rgb[1] > rgb[0] and rgb[1] > rgb[2]):
            return "GREEN"
        elif(rgb[0] > rgb[1] and rgb[0] > rgb[2]):
               return "RED"
        elif(rgb[2] > rgb[1] and rgb[2] > rgb[0]):
               return "BLUE"

    def color_difference (self, color1, color2):
        return sum([abs(component1-component2) for component1, component2 in zip(color1, color2)])


    def rgb_to_hls(self, r, g, b):
        if (max(r, g, b) == 0):
            maxc = 0.002
        else:
            maxc = max(r, g, b)
        if(min(r, g, b) == 0):
            minc = 0.001
        else:
            minc = min(r, g, b)
        # XXX Can optimize (maxc+minc) and (maxc-minc)
        l = (minc+maxc)/2.0
        if minc == maxc:
            return 0.0, l, 0.0
        if l <= 0.5:
            s = (maxc-minc) / (maxc+minc)
        else:
            s = (maxc-minc) / (2.0-maxc-minc)
        rc = (maxc-r) / (maxc-minc)
        gc = (maxc-g) / (maxc-minc)
        bc = (maxc-b) / (maxc-minc)
        if r == maxc:
            h = bc-gc
        elif g == maxc:
            h = 2.0+rc-bc
        else:
            h = 4.0+gc-rc
        h = (h/6.0) % 1.0
        return h, l, s

    def dominantColor3(self):
        rgb = self.rgb()
        #print(rgb)
        #TARGET_COLORS = {"RED": (255, 0, 0), "GREEN": (0, 215, 0), "BLUE": (0, 0, 255), "BLACK": (0, 0, 0), "WHITE": (255, 255, 255)}
        TARGET_COLORS = {"RED": (180, 40, 30, 109), "GREEN": (97, 103, 67, 85), "BLUE": (23, 53, 210, 117), "BLACK": (9, 9, 7, 9), "WHITE": (167, 144, 255, 199)}
        rgb_list = list(rgb)
        hsl_color = self.rgb_to_hls(rgb[0], rgb[1], rgb[2])
        rgb_list.append(hsl_color[1])
        my_color = tuple(rgb_list)
        print(my_color)
        differences = [[self.color_difference(my_color, target_value), target_name] for target_name, target_value in TARGET_COLORS.items()]
        differences.sort() 
        my_color_name = differences[0][1]
        #print(hsl_color)
        if(my_color_name == "BLUE"):
            return Color.BLUE
        elif(my_color_name == "GREEN"):
            return Color.GREEN
        elif(my_color_name == "RED"):
            return Color.RED
        elif(my_color_name == "BLACK"):
            return Color.BLACK
        elif(my_color_name == "WHITE"):
            return Color.WHITE
        else:
            return None
