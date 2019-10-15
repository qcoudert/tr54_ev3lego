from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Stop)

MAX_ANGLE_SPEED = 350

class Pilot:

    def __init__(self):
        self.speed = 0
        self.angleSpeed = 0
        self.left_motor = Motor(Port.B)
        self.right_motor = Motor(Port.C)

    def forward(self, speed):
        self.speed = speed
        self.angleSpeed = 0
        self.left_motor.run(speed)
        self.right_motor.run(speed)

    def forwardTurn(self, speedPercentage, angle):
        s = 850 * (speedPercentage/100)
        if(angle<0):
            if(self.angleSpeed > 0):
                self.angleSpeed = 0
            if(-self.angleSpeed<MAX_ANGLE_SPEED):
                self.angleSpeed = self.angleSpeed + angle
            self.left_motor.run(s+self.angleSpeed)
            self.right_motor.run(s)
        elif(angle>0):
            if(self.angleSpeed < 0):
                self.angleSpeed = 0
            if(self.angleSpeed<MAX_ANGLE_SPEED):
                self.angleSpeed = self.angleSpeed + angle
            self.left_motor.run(s)
            self.right_motor.run(s-self.angleSpeed)

    def forwardTurn2(self, speedPercentage, angle):
        # angle -100 to 100
        speed = 850 * (speedPercentage/100)
        relativeAngle = (speed * angle) / 100
        if(angle<0):
            self.left_motor.run(speed+2*relativeAngle)
            self.right_motor.run(speed)
        elif(angle>0):
            self.left_motor.run(speed)
            self.right_motor.run(speed-2*relativeAngle)
        
    def forwardRelative(self, speedPercentage):
        s = 850 * (speedPercentage/100) #850 vitesse maximale du robot
        self.angleSpeed = 0
        self.left_motor.run(s)
        self.right_motor.run(s)

    def rotate(self, angle, aSpeed):
        self.left_motor.run_target(aSpeed, angle, Stop.BRAKE, False)
        self.right_motor.run_target(aSpeed, -angle, Stop.BRAKE, True)

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()