from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Stop)


class Pilot:

    def __init__(self):
        self.left_motor = Motor(Port.B)
        self.right_motor = Motor(Port.C)

    def forward(self, speed):
        self.left_motor.run(speed)
        self.right_motor.run(speed)

    def forwardTurn(self, speedPercentage, angle):
        s = 850 * (speedPercentage/100)
        if(angle>0):
            self.left_motor.run(s-angle)
            self.right_motor.run(s)
        else:
            self.left_motor.run(s)
            self.right_motor.run(s-angle)
        
    def forwardRelative(self, speedPercentage):
        s = 850 * (speedPercentage/100) #850 vitesse maximale du robot
        self.left_motor.run(s)
        self.right_motor.run(s)

    def rotate(self, angle, aSpeed):
        self.left_motor.run_target(aSpeed, angle, Stop.BRAKE, False)
        self.right_motor.run_target(aSpeed, -angle, Stop.BRAKE, True)

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()