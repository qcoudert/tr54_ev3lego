import network
import time

SECURITY_DISTANCE = 100                                             #Distance to travel from the beginning of the way to the end of the intersection

class DPassage:
    """"""

    def __init__(self, ip):
        self.isAllowedToPass = False                                #False if the robot is not allowed to pass the intersection, else True
        self.ip = ip                                                #IP Address of the robot
        self.serv_listener = network.NetworkListener(self.ip)       #NetworkListener of the robot used to listen any message from the server
        self.serv_listener.start()                                  #Starting the NetworkListener
        self.serv_sender = network.MessageSender(self.ip)           #MessageSender used to send messages to the server
 
    def stateInWay(self, state):
        """Send the current status of the robot to the server"""

        if(state == "GREEN"):
            self.serv_sender.sendMessage("GREEN "+ self.ip + " " + str(time.time()))
        elif(state == "ORANGE"):
            self.serv_sender.sendMessage("RED "+ self.ip + " " + str(time.time()))
        elif(state == "OOC"):
            self.serv_sender.sendMessage("OOC "+ self.ip + " " + str(time.time()))
    
    def canPass(self):
        """Check if the permission to pass is given by the server
        
        Return True if so, else False."""

        self.isAllowedToPass = False
        if(self.serv_listener.mailbox):
            #The server return the IP and the message "YES"
            if (self.serv_listener.mailbox[0].split()[0] == self.ip and self.serv_listener.mailbox[0].split()[1] == "YES"):
                #Delete the message
                self.serv_listener.mailbox.pop(0)
                self.isAllowedToPass = True            
        
        return self.isAllowedToPass

    def hasPassed(self, distReached):
        """Return true if the robot has passed the intersection and send it to the server
        
        'distReached': Distance the robot reached since he started to go through the way
        """
        
        if(distReached >= SECURITY_DISTANCE and self.isAllowedToPass == True):
            self.isAllowedToPass = False
            self.serv_sender.sendMessage("OOC " + self.ip)      #Send that the robot has passed to delete it in the way list on the server
            self.serv_listener.mailbox = []                     #Delete any messages avoid storing previous permissions given
            return True
        else:
            return False

    




