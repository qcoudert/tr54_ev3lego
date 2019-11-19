import pilot, distance_sensor, color_sensor, robot_status, lcd_display, log, collision_management

MAX_SPEED = 50
ANGLE_MAX = 100
ANGLE_MIN = 10
TURNING_TIME_MAX = 2

class PathFinding :
    def __init__(self):
        self.phaseTime = 0
        self.phaseVirage = 1
        self.vitesse = 0
        self.path_color = None
        self.speed = 0
        self.pilote = pilot.Pilot()
        self.color_cs = color_sensor.CSensor()
        self.distance_sensor = distance_sensor.DistanceSensor()
        self.collision_management = collision_management.CollisionManagement(distance_sensor)

    
    def keepGoing(self, delta):
        """Method to call to tell the robot to continue the pathfinding
        delta : the delta time """

        speedCollision = self.collision_management.collisionSpeed(MAX_SPEED)
        old_speed = self.speed
        self.speed = min(self.speedCollision, self.speedMax*(0.5*phaseVirage+0.5))

        self.path_color = self.pilote_cs.color()
        if(path_color==Color.WHITE):
            pilote.forwardTurn2(self.speed, ANGLE_MIN + (ANGLE_MAX-ANGLE_MIN) - ANGLE_MAX * phaseVirage * phaseVirage)
        elif(path_color==Color.BLUE or path_color==Color.GREEN or path_color==Color.ORANGE):
            pilote.forwardRelative(speedCollision)
        elif(path_color==Color.BLACK):
            pilote.forwardTurn2(self.speed, -ANGLE_MAX + (ANGLE_MAX-ANGLE_MIN) * phaseVirage * phaseVirage)

        if(phaseVirage - (1/turningMaxTime)*delta > 0):
            phaseVirage = phaseVirage - (1/turningMaxTime)*delta

        if(path_color != phase):
            phase = path_color
            phaseVirage = 1