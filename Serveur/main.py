from communication import Server
import time

server = Server()
server.start()
print(server.ip)
print(server.broadcastAdd)


greenWay = []
orangeWay = []
isRunning = False
greenIsRunning = False
orangeIsRunning = False


while (1):
    #Chaque robot qui entre dans la zone d'entrée envoie sa voie et son temps, on vérifie l'ip pour ne l'ajouter qu'une fois dans la liste
    #On ajoute dans la liste l'ip u robot ainsi que son timig de la façon suivante liste = [[ip1,tps1],[ip2,tps2],..]
    msg = server.readMsg()
    if (msg.split()[0] == "RED" and msg.split()[1] not in orangeWay):
        orangeWay.append( [msg.split()[1],msg.split()[2]] )
    if (msg.split()[0]== "GREEN" and msg.split()[1] not in greenWay):
        greenWay.append( [msg.split()[1],msg.split()[2]] )

    #Si on est en cours de traitement
    if(isRunning == True):



    #Si on est pas déjà en cours de traitement
    if (isRunning == False):
        #On compare les liste pour savoir quelle voie est prioritaire (celle qui a eu le premier véhicule arrivé est prioritaire)
        if (greenWay[0][1] < orangeWay[0][1] ):
            isRunning = True
            greenIsRunning = True
        if ( greenWay[0][1] > orangeWay[0][1] ):
            isRunning = True
            orangeIsRunning = True
        if ( greenWay[0][1] == orangeWay[0][1] ):
            isRunning = True
            orangeIsRunning = True














i = 0
while(i < 100):
    print("Iteration " + str(i))
    server.appendMsg(str(time.time()))
    msg = server.readMsg()
    if(msg!=None):
        print(msg)
    time.sleep(1)
    i = i + 1