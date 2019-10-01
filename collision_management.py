#!/usr/bin/env pybricks-micropython

import pilot, distance_sensor


class CollisionManagement :
    def __init__(self, distanceSensor):
        self.distanceSensor = distanceSensor
        self.Ts = 10
        self.vitesse_old = 0
        self.df = 5
        self.da = 5
        self.af = 2
        self.aa = 2


    def collisionSpeed(self, maxSpeed):
        dist = self.distanceSensor.distance()
        vitesse_freinage = min(max(self.af*(dist-self.df),0),maxSpeed)
        vitesse_accel = min(max(self.aa*(dist-self.da),0,self.vitesse_old),maxSpeed)
        vitesse = min(vitesse_freinage,vitesse_accel)
        self.vitesse_old = vitesse
        return vitesse