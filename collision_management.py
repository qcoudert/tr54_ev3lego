#!/usr/bin/env pybricks-micropython

import pilot, distance_sensor


class CollisionManagement :
    def __init__(self, distanceSensor):
        self.distanceSensor = distanceSensor
        self.Ts = 10
        self.speed_old = 0
        self.df = 15
        self.da = 15
        self.af = 2
        self.aa = 2


    def collisionSpeed(self, maxSpeed):
        dist = self.distanceSensor.distance()
        speed_break = min(max(self.af*(dist-self.df),0),maxSpeed)
        speed_accel = min(max(self.aa*(dist-self.da),0,self.speed_old),maxSpeed)
        speed = min(speed_break,speed_accel)
        self.speed_old = speed
        return speed