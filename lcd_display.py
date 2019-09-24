from pybricks import ev3brick as brick
from pybricks.parameters import ImageFile

class LCDDisplay:

    def displayStatus(self, robotStatus):
        brick.display.clear()
        brick.display.text("Distance: "+str(robotStatus.getDistance()))

    def displayImage(self):
        brick.display.clear()
        brick.display.image(ImageFile.ANGRY)