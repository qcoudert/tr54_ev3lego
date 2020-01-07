from network import NetworkListener, MessageSender
import utils
import time

listener = NetworkListener()    #NetworkListener used to listen to the robots' messages
listener.start()
sender = MessageSender()        #MessageSender used to send messages to robots
print(listener.ip)

greenWay = [[],[]]              #[[IP of the robot on the green way],[Date of entry on the green way]]
orangeWay = [[],[]]             #[[IP of the robot on the orange way],[Date of entry on the orange way]]
isRunning = False               #False if no permission is currently given, True if a permission is given to a specific way (GREEN or ORANGE)
greenIsRunning = False          #False if the robots on the green way don't have the permission to cross the intersection, else True
orangeIsRunning = False         #False if the robots on the don't way don't have the permission to cross the intersection, else True


while (1):
    #Every robot entering the entry zone send his way and his current time, we then check the ip to have only one instance of the robot in the list
    #The IP of the robot is then added to the list with the date of his entry so that list = [[ip1,ip2,...,ipn],[time1,time2,...,timen]] 
    if(listener.mailbox):    
        msg = listener.mailbox.pop(0).split()
        if (msg[0] == "RED" and msg[1] not in orangeWay[0]):
            orangeWay[0].append(msg[1])
            orangeWay[1].append(msg[2])
        elif (msg[0]== "GREEN" and msg[1] not in greenWay[0]):
            greenWay[0].append(msg[1])
            greenWay[1].append(msg[2])
        #If the robot is not anymore in an entry or conflict zone, we then delete it from the lists
        elif (msg[0]== "OOC"):
            utils.deleteColumnContainingIP(greenWay, msg[1])
            utils.deleteColumnContainingIP(orangeWay, msg[1])

    print(greenWay)
    print(orangeWay)

    #If we are currently giving permission to a way, we broadcast it to the corresponding robots
    if(isRunning == True):
        if(greenIsRunning == True):
            if(greenWay[0]):
                for elt in greenWay[0]:
                    sender.sendMessage(elt + " " + "YES")       #Broadcast the permission to every robot in the green way
            else:
                greenIsRunning = False
                isRunning = False
        elif(orangeIsRunning == True):
            if(orangeWay[0]):
                for elt in orangeWay[0]:
                    sender.sendMessage(elt + " " + "YES")       #Broadcast the permission to every robot in the orange way
            else:
                orangeIsRunning = False
                isRunning = False
        else:
            isRunning = False

    #If we haven't any permission currently given, we decide which way we'll give it to
    if (isRunning == False):
        #We compare the lists to give the permission to the first robots that arrived on his way
        if(greenWay[1] and orangeWay[1]):
            if (greenWay[1][0] < orangeWay[1][0] ):
                isRunning = True
                greenIsRunning = True
            elif ( greenWay[1][0] >= orangeWay[1][0] ):
                isRunning = True
                orangeIsRunning = True
        #If there is not any robots on any way we continue to loop until one of them come 
        elif(not(greenWay[0]) and not(orangeWay[0])):
            isRunning=False
            orangeIsRunning=False
            greenIsRunning=False
        elif(not(greenWay[0])):
            isRunning=True
            orangeIsRunning=True
        else:
            isRunning=True
            greenIsRunning=True