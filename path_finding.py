import pilot, distance_sensor, color_sensor, robot_status, lcd_display, log, collision_management
from pybricks.parameters import Color
import droit_passage

ACCELERATION = 20
MAX_SPEED = 60
ANGLE_MAX = 60
ANGLE_MIN = 40
TURNING_TIME_MAX = 1.5
DISTANCE_INTERSECTION = 45 

class PathFinding :
    def __init__(self):
        self.phaseTime = 0
        self.phaseVirage = 1
        self.vitesse = 0
        self.path_color = None
        self.phase = None
        self.speed = 0
        self.pilote = pilot.Pilot()
        self.color_cs = color_sensor.CSensor()
        self.m_distance_sensor = distance_sensor.DistanceSensor()
        self.m_collision_management = collision_management.CollisionManagement(self.m_distance_sensor)

    
    def keepGoing(self, delta):
        """Method to call to tell the robot to continue the pathfinding
        delta : the delta time """

        speedCollision = self.m_collision_management.collisionSpeed(MAX_SPEED)
        old_speed = self.speed
        self.speed = min(speedCollision, self.speed + delta*ACCELERATION) #MAX_SPEED*(0.5*self.phaseVirage+0.5),

        self.path_color = self.color_cs.dominantColor3()

        self.pathfindingStrategy(delta)
    

    def stopIntersection(self, delta, distance):
        """Method to call when the robot enter in the intersection area
        delta : the delta time
        distance : the distance traveled after the intersection start"""

        if(distance>45):
            distance = 45
        speedCollision = self.m_collision_management.collisionSpeed(MAX_SPEED - MAX_SPEED * (distance/DISTANCE_INTERSECTION))
        old_speed = self.speed
        self.speed = min(speedCollision, self.speed + delta*ACCELERATION) #MAX_SPEED*(0.5*self.phaseVirage+0.5),

        self.path_color = self.color_cs.dominantColor3()

        self.pathfindingStrategy(delta)

        return (distance < DISTANCE_INTERSECTION)

    
    def pathfindingStrategy(self, delta):
        """Method which contains the pathfinding strategy
        delta : the delta time"""

        #The strategy used here is : the more the robot is in one area, the more the angle of turning will be high
        if(self.path_color==Color.WHITE or self.path_color==Color.GREEN or self.path_color==Color.ORANGE):
            self.pilote.forwardTurn2(self.speed, ANGLE_MIN + (ANGLE_MAX-ANGLE_MIN) - ANGLE_MAX * self.phaseVirage * self.phaseVirage)
        elif(self.path_color==Color.BLUE):
            self.pilote.forwardRelative(self.speed)
        elif(self.path_color==Color.BLACK):
            self.pilote.forwardTurn2(self.speed, -ANGLE_MAX + (ANGLE_MAX-ANGLE_MIN) * self.phaseVirage * self.phaseVirage)

        if(self.phaseVirage - (1/TURNING_TIME_MAX)*delta > 0):
            self.phaseVirage = self.phaseVirage - (1/TURNING_TIME_MAX)*delta

        if(self.path_color != self.phase):
            self.phase = self.path_color
            self.phaseVirage = 1