from pybricks.ev3devices import ColorSensor
from pybricks.parameters import (Port, Color)
from pybricks.tools import print, wait
import time

COLOR_PROBABILITY_TIME_LIMIT = 1
COLOR_GREEN_PROBA_THRESH = 0.7
COLOR_RED_PROBA_THRESH = 0.8

class CSensor:
    

    def __init__(self):
        self.sensor = ColorSensor(Port.S3)

        self.dominantColorTab = []

        self.colorTab = []
        self.colorTab2 = []

        self.colorTab.append((0,0,0,0, Color.BLACK))
        self.colorTab.append((1,30,30,30, Color.BLACK))

        self.colorTab.append((0,51,60,80, Color.WHITE))
        self.colorTab.append((1,100,100,100, Color.WHITE))

        self.colorTab.append((0,55,0,3, Color.RED))
        self.colorTab.append((1,80,20,7, Color.RED))

        self.colorTab.append((0,30,55,20, Color.GREEN))
        self.colorTab.append((1,36,62,23, Color.GREEN))

        self.colorTab.append((0,7,30,63, Color.BLUE))
        self.colorTab.append((1,10,33,67, Color.BLUE))
# ---------------------
        self.colorTab2.append((1,1,40, Color.BLACK))

        self.colorTab2.append((1.2,1.6,100, Color.WHITE))

        self.colorTab2.append((0.25,0.1,80, Color.RED))

        self.colorTab2.append((2,0.66,60, Color.GREEN))

        self.colorTab2.append((3,6.5,70, Color.BLUE))

        #-- TEST PROBABILITY COLOR --#
        self.logColors = [[],[]]


    def color(self):
        return self.sensor.color()

    def color2(self):
        color = self.sensor.rgb()
        print(color)
        color_type = None
        for i in range (0, len(self.colorTab)/2) :
            test = True
            for j in range (0,3) :
                if(color[j] < self.colorTab[i*2][j+1] or color[j] > self.colorTab[i*2+1][j+1] ):
                    test = False
            if(test == True):
                return self.colorTab[i*2][4]
        return None

    def color3(self):
        color = self.sensor.rgb()
        color_type = None
        for i in range (0, len(self.colorTab2)) :
            test = True
            if(color[0] > self.colorTab2[i][2] or color[1] > self.colorTab2[i][2] or color[2] > self.colorTab2[i][2]):
                test = False
            for j in range (0,2) :
                if(color[1+j] * self.colorTab2[i][j]  < color[0] - self.colorTab2[i][j] * self.colorTab2[i][2]/10 or 
                color[1+j] * self.colorTab2[i][j]  > color[0] + self.colorTab2[i][j] * self.colorTab2[i][2]/10):
                    test = False
            if(test == True):   
                print(self.colorTab2[i][3])
                return self.colorTab2[i][3]
        print("None")
        return None

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
        TARGET_COLORS = {"BLUE": (23, 53, 210, 117), "BLACK": (9, 9, 7, 9), "WHITE": (167, 144, 255, 199)}
        SWITCHER_COLOR = {"BLUE": Color.BLUE, "BLACK": Color.BLACK, "WHITE": Color.WHITE}
        rgb_list = list(rgb)
        hsl_color = self.rgb_to_hls(rgb[0], rgb[1], rgb[2])
        rgb_list.append(hsl_color[1])
        my_color = tuple(rgb_list)
        #print(my_color)
        differences = [[self.color_difference(my_color, target_value), target_name] for target_name, target_value in TARGET_COLORS.items()]
        differences.sort() 
        my_color_name = differences[0][1]
        #print(hsl_color)
        return SWITCHER_COLOR.get(my_color_name, -1)

    def dominantColor4(self):
        rgb = self.rgb()
        #print(rgb)
        #TARGET_COLORS = {"RED": (255, 0, 0), "GREEN": (0, 215, 0), "BLUE": (0, 0, 255), "BLACK": (0, 0, 0), "WHITE": (255, 255, 255)}
        TARGET_COLORS = {"RED": (180, 40, 30, 109), "GREEN": (92, 154, 50, 102), "BLUE": (23, 53, 210, 117), "BLACK": (9, 9, 7, 9), "WHITE": (167, 144, 255, 199)}
        rgb_list = list(rgb)
        hsl_color = self.rgb_to_hls(rgb[0], rgb[1], rgb[2])
        rgb_list.append(hsl_color[1])
        my_color = tuple(rgb_list)
        print(my_color)
        differences = [[self.color_difference(my_color, target_value), target_name] for target_name, target_value in TARGET_COLORS.items()]
        #print(differences)
        differences.sort() 
        #print(differences)
        my_color_name = differences[0][1]
        print(hsl_color)
        print(my_color_name)
        return my_color_name


    def dominantSortingColor(self):
        my_color = self.dominantColor4()
        wait(15)
        self.dominantColorTab.append(my_color)
        if(len(self.dominantColorTab) == 5):
            setlist = set(sorted(self.dominantColorTab))
            b = [self.dominantColorTab.count(el) for el in setlist]
            pos = b.index(max(b))
            new_list = list(setlist)
            self.dominantColorTab.clear()
            return new_list[pos]
        else:
            return "N/A"

    def dominantSortingColor2(self):
        my_color = self.dominantColor4()
        self.dominantColorTab.append(my_color)
        SWITCHER_COLOR = {"RED": Color.RED, "GREEN": Color.GREEN, "BLUE": Color.BLUE, "BLACK": Color.BLACK, "WHITE": Color.WHITE}
        if(len(self.dominantColorTab) == 5):
            setlist = set(sorted(self.dominantColorTab))
            b = [self.dominantColorTab.count(el) for el in setlist]
            pos = b.index(max(b))
            new_list = list(setlist)
            self.dominantColorTab.clear()
            wait(10)
            return SWITCHER_COLOR.get(new_list[pos], -1)
        else:
            wait(10)
            return "N/A"
    

    def updateColorProbability(self):
        c = self.sensor.color()
        t = time.time()
        while(self.logColors[0] and (t-self.logColors[1][0])>COLOR_PROBABILITY_TIME_LIMIT):
            self.logColors[0][0]
            self.logColors[1][0]
        
        self.logColors[0].append(c)
        self.logColors[1].append(t)

    def greenColorProbability(self):
        return float(self.logColors.count(Color.GREEN))/float(len(self.logColors))

    def redColorProbability(self):
        return float(self.logColors.count(Color.RED))/float(len(self.logColors))

    def isRedOrGreen(self):
        c = self.sensor.color()
        if(c == Color.GREEN and self.greenColorProbability()>COLOR_GREEN_PROBA_THRESH):
            return Color.GREEN
        elif(c == Color.RED and self.redColorProbability()>COLOR_RED_PROBA_THRESH):
            return Color.RED
        else:
            return None

