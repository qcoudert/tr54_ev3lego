from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Stop)
import math

MAX_ANGLE_SPEED = 350
MAX_SPEED = 800

class Pilot:
    """Pilot class allowing user to drive the robot"""
    
    def __init__(self):
        self.speed = 0
        self.angleSpeed = 0
        self.turnItRight = 0
        self.turnItLeft = 0
        self.left_motor = Motor(Port.B)
        self.right_motor = Motor(Port.C)

    def forward(self, speed):
        self.speed = speed
        self.angleSpeed = 0
        self.left_motor.run(speed)
        self.right_motor.run(speed)

    def forwardTurnRightLog(self, speedPercentage, angleAcc):
        """Make the robot turns right using a logaritmic function.

        The longer the robot turns, the more it will turn right until the robot reaches MAX_ANGLE_SPEED.
        This function use a logarimtic function to increase the angle speed.

        speedPercentage: relative speed the robot should be using while turning
        angleAcc: relative acceleration of the turn (from 0 to 1)
        """

        self.speed = round(MAX_SPEED * (speedPercentage/100))
        self.turnItLeft = 0
        self.turnItRight = self.turnItRight + angleAcc
        self.angleSpeed = min(MAX_ANGLE_SPEED, round(((math.log(self.turnItRight)+3)/4)*MAX_ANGLE_SPEED))
        self.left_motor.run(self.speed)
        self.right_motor.run(self.speed-self.angleSpeed)
        return self

    def forwardTurnLeftLog(self, speedPercentage, angleAcc):
        """Make the robot turns left using a logaritmic function.

        The longer the robot turns, the more it will turn left until the robot reaches MAX_ANGLE_SPEED.
        This function use a logarimtic function to increase the angle speed.

        speedPercentage: relative speed the robot should be using while turning
        angleAcc: relative acceleration of the turn (from 0 to 1)
        """

        self.speed = round(MAX_SPEED * (speedPercentage/100))
        self.turnItRight = 0
        self.turnItLeft = self.turnItRight + angleAcc
        self.angleSpeed = min(MAX_ANGLE_SPEED, round(((math.log(self.turnItRight)+3)/4)*MAX_ANGLE_SPEED))
        self.left_motor.run(self.speed)
        self.right_motor.run(self.speed-self.angleSpeed)
        return self
    
    def forwardTurnLeftExp(self, speedPercentage, angleAcc):
        """Make the robot turns left using a reverse exponential function.

        The longer the robot turns, the more it will turn left until the robot reaches MAX_ANGLE_SPEED.
        This function use a reverse exponential function to increase the angle speed.

        speedPercentage: relative speed the robot should be using while turning
        angleAcc: relative acceleration of the turn (from 0 to 1)
        """
        self.speed = round(MAX_SPEED * (speedPercentage/100))
        self.turnItRight = 0
        self.turnItLeft = self.turnItRight + angleAcc
        self.angleSpeed = min(MAX_ANGLE_SPEED, round((1/math.exp(self.turnItRight*(-2)))*MAX_ANGLE_SPEED))
        self.left_motor.run(self.speed)
        self.right_motor.run(self.speed-self.angleSpeed)
        return self

    def forwardTurnRightExp(self, speedPercentage, angleAcc):
        """Make the robot turns right using a reverse exponential function.

        The longer the robot turns, the more it will turn right until the robot reaches MAX_ANGLE_SPEED.
        This function use a reverse exponential function to increase the angle speed.

        speedPercentage: relative speed the robot should be using while turning
        angleAcc: relative acceleration of the turn (from 0 to 1)
        """

        self.speed = round(MAX_SPEED * (speedPercentage/100))
        self.turnItLeft = 0
        self.turnItRight = self.turnItRight + angleAcc
        self.angleSpeed = min(MAX_ANGLE_SPEED, round((1/math.exp(self.turnItRight*(-2)))*MAX_ANGLE_SPEED))
        self.left_motor.run(self.speed)
        self.right_motor.run(self.speed-self.angleSpeed)
        return self

    def forwardTurn2(self, speedPercentage, angle):
        # angle -100 to 100
<<<<<<< HEAD
        speed = MAX_SPEED * (speedPercentage/100)
        relativeAngle = (speed * angle) / 100
=======
        self.speed = 850 * (speedPercentage/100)
        relativeAngle = (self.speed * angle) / 100
>>>>>>> 4dc67ac4f065505e9de14b576a56b2d833fb407e
        if(angle<0):
            self.left_motor.run(self.speed+2*relativeAngle)
            self.right_motor.run(self.speed)
        elif(angle>0):
            self.left_motor.run(self.speed)
            self.right_motor.run(self.speed-2*relativeAngle)
        
    def forwardRelative(self, speedPercentage):
        """Make the robot move forward using relative speed (0 to 100)."""
        
<<<<<<< HEAD
        s = MAX_SPEED * (speedPercentage/100) #MAX_SPEED vitesse maximale du robot
=======
        self.speed = 850 * (speedPercentage/100) #850 vitesse maximale du robot
>>>>>>> 4dc67ac4f065505e9de14b576a56b2d833fb407e
        self.angleSpeed = 0
        self.left_motor.run(self.speed)
        self.right_motor.run(self.speed)

    def rotate(self, angle, aSpeed):
        self.left_motor.run_target(aSpeed, angle, Stop.BRAKE, False)
        self.right_motor.run_target(aSpeed, -angle, Stop.BRAKE, True)

    def rotateR(self, speed):
        s = MAX_SPEED * (speed/100)
        self.right_motor.run(s)

    def rotateL(self, speed):
        s = MAX_SPEED * (speed/100)
        self.left_motor.run(s)

    
    def stop(self):
        """Make the robot stop mooving by stoping all the motors."""

        self.left_motor.stop()
        self.right_motor.stop()