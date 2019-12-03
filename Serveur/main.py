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
    #On ajoute dans la liste l'ip u robot ainsi que son timing de la façon suivante liste = [[ip1,tps1],[ip2,tps2],..]
    msg = server.readMsg()
    if (msg.split()[0] == "RED" and msg.split()[1] not in orangeWay):
        orangeWay.append( [msg.split()[1],msg.split()[2]] )
    if (msg.split()[0]== "GREEN" and msg.split()[1] not in greenWay):
        greenWay.append( [msg.split()[1],msg.split()[2]] )
    #Si le robot n'est plus dans la zone d'entrée/conflit alors on le supprime des listes de passage
    if (msg.split()[0]== "OOC"):
        for elt in greenWay:
            if(msg.split()[1] == greenWay[elt][0]):
                orangeWay.pop(elt)
        for elt in orangeWay:
            if(msg.split()[1] == orangeWay[elt][0]):
                orangeWay.pop(elt)


    #Si on est en cours de traitement
    if(isRunning == True):
        if(greenIsRunning == True):
            for elt in greenWay:
                Server.serv_sender.sendMessage(greenWay[elt][0] + " " + "YES")
            #Une fois que tous les robots de liste vertes sont passés alors la liste est vide et on peut faire passer ceux de la liste orange
            if(not greenWay):
                greenIsRunning = False
                orangeIsRunning = True
                
        if(orangeIsRunning == True):
            for elt in orangeWay:
                Server.serv_sender.sendMessage(greenWay[elt][0] + " " + "YES")
            #Une fois que tous les robots de liste vertes sont passés alors la liste est vide et on peut faire passer ceux de la liste orange
            if(not orangeWay):
                orangeIsRunning = False
                greenIsRunning = True 

        #Si les deux listes sont vides alors il n'y a plus de robots dans les zones d'entrées/conflits > on recommence le processus comme au départ
        if(not orangeWay and not greenWay):
            isRunning == False
            greenIsRunning = False
            orangeIsRunning = False


    #Si on est pas déjà en cours de traitement
    if (isRunning == False):
        #On compare les liste pour savoir quelle voie est prioritaire (celle qui a eu le premier véhicule arrivé est prioritaire)
        #Vert prioritaire
        if (greenWay[0][1] < orangeWay[0][1] ):
            isRunning = True
            greenIsRunning = True
        #Orange prioritaire
        if ( greenWay[0][1] > orangeWay[0][1] ):
            isRunning = True
            orangeIsRunning = True
        #Si les temps sont égaux alors ont choisit arbitrairement l'orange comme voie prioritaire
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