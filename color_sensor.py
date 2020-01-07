from pybricks.ev3devices import ColorSensor
from pybricks.parameters import (Port, Color)
from pybricks.tools import print, wait
import time
import csv

COLOR_PROBABILITY_TIME_LIMIT = 3
COLOR_GREEN_PROBA_THRESH = 0.6
COLOR_RED_PROBA_THRESH = 0.6

class CSensor:
    

    def __init__(self):

        self.sensor = ColorSensor(Port.S3)

        self.dominantColorTab = []                  #List used for dominantSortingColor
            
        self.logColors = []                         #List used to store recently found colors 


    def color(self):
        """Return the color detected by the native function of the sensor"""
        return self.sensor.color()
   
    def rgb(self):
        """Return the sensor RGB values"""
        rgb = self.sensor.rgb()
        r = (rgb[0]/100)*255
        g = (rgb[1]/100)*255
        b = (rgb[2]/100)*255
        return r,g,b

    #Convert RGB values into HSV values
    def hsv(self):
        """Convert RGB values into HSV values"""
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

    def rgb_to_hls(self, r, g, b):
        """Convert rgb values to hsl values"""
        if (max(r, g, b) == 0):
            maxc = 0.002
        else:
            maxc = max(r, g, b)
        if(min(r, g, b) == 0):
            minc = 0.001
        else:
            minc = min(r, g, b)
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

    def color_difference (self, color1, color2):
        """Return a list of all the differences of colors in other lists ([diff,diff2,diff3,etc])"""
        return sum([abs(component1-component2) for component1, component2 in zip(color1, color2)])

    def dominantColor3(self):
        """Return the number value of BLUE, BLACK or WHITE > This function is used for following the path
        
        This function compare and take the nearest color
        """
        rgb = self.rgb()
        #Color references
        TARGET_COLORS = {"BLUE": (23, 53, 210, 117), "BLACK": (9, 9, 7, 9), "WHITE": (167, 144, 255, 199)}
        SWITCHER_COLOR = {"BLUE": Color.BLUE, "BLACK": Color.BLACK, "WHITE": Color.WHITE}
        rgb_list = list(rgb)
        hsl_color = self.rgb_to_hls(rgb[0], rgb[1], rgb[2])
        rgb_list.append(hsl_color[1])
        my_color = tuple(rgb_list)
        differences = [[self.color_difference(my_color, target_value), target_name] for target_name, target_value in TARGET_COLORS.items()]
        differences.sort() 
        my_color_name = differences[0][1]
        return SWITCHER_COLOR.get(my_color_name, -1)

    #Same function as dominantColor3 but white red and green
    def dominantColor4(self):
        """Same function as dominantColor3 but white red and green"""
        rgb = self.rgb()
        TARGET_COLORS = {"RED": (180, 40, 30, 109), "GREEN": (92, 154, 50, 102), "BLUE": (23, 53, 210, 117), "BLACK": (9, 9, 7, 9), "WHITE": (167, 144, 255, 199)}
        rgb_list = list(rgb)
        hsl_color = self.rgb_to_hls(rgb[0], rgb[1], rgb[2])
        rgb_list.append(hsl_color[1])
        my_color = tuple(rgb_list)
        differences = [[self.color_difference(my_color, target_value), target_name] for target_name, target_value in TARGET_COLORS.items()]
        differences.sort() 
        my_color_name = differences[0][1]
        return my_color_name

    def dominantSortingColor(self):
        """Use dominantColor4 to take a list of 5 colors and choose the most viewed color in this list"""
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

    #Same as dominantSortingColor but return the number of the color
    def dominantSortingColor2(self):
        """Same as dominantSortingColor but return the number of the color"""
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
    

    #-- COLOR FINDING WITH PROBABILITIES --#

    def updateColorProbability(self):
        """Update the list of recently found colors
        
        There may be COLOR_PROBABILITY_TIME_LIMIT colors in the log list at the same time."""

        c = self.dominantColor3()
        
        while(self.logColors and (len(self.logColors)>COLOR_PROBABILITY_TIME_LIMIT)):
            self.logColors.pop(0)
        
        self.logColors.append(c)

    def greenColorProbability(self):
        """Return the percentage of green colors stored in the log list"""
        return float(self.logColors.count(Color.GREEN))/float(len(self.logColors))

    def redColorProbability(self):
        """Return the percentage of red colors stored in the log list"""
        return float(self.logColors.count(Color.RED))/float(len(self.logColors))

    def isRedOrGreen(self):
        """Find if the current color is Red, Green or none of them.

        The Green or Red color are confirmed only if the current probability is above, respectively, COLOR_GREEN_PROBA_THRESH and COLOR_RED_PROBA_THRESH"""
        
        c = self.dominantColor3()
        if(c == Color.GREEN and self.greenColorProbability()>COLOR_GREEN_PROBA_THRESH):
            return Color.GREEN
        elif(c == Color.RED and self.redColorProbability()>COLOR_RED_PROBA_THRESH):
            return Color.RED
        else:
            return None


