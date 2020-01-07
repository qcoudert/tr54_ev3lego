#!/usr/bin/env pybricks-micropython

import distance_sensor


class CollisionManagement :
    """Collision Management class use to adapt the speed if something is in front of the robot."""
    def __init__(self, distanceSensor):
        self.distanceSensor = distanceSensor
        self.speed_old = 0
        self.df = 15        # The maximum distance the robot have to start breaking
        self.da = 16        # The distance the robot can accelerate to his maximum
        self.af = 2         # The minimum distance the robot can be of the object in front of him
        self.aa = 3         # The distance the robot can start to accelerate


    def collisionSpeed(self, maxSpeed):
        """Call to now the speed the robot should go to follow the thing in front of him.
        
        maxSpeed : the maximum speed the robot can go
        
        return the speed the robot should go"""
        dist = self.distanceSensor.distance()
        speed_break = min(max(self.af*(dist-self.df),0),maxSpeed)
        speed_accel = min(max(self.aa*(dist-self.da),0,self.speed_old),maxSpeed)
        speed = min(speed_break,speed_accel)
        self.speed_old = speed
        return speed