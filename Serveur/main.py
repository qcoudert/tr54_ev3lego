from network import NetworkListener, MessageSender
import utils
import time

listener = NetworkListener()
listener.start()
sender = MessageSender()
print(listener.ip)

greenWay = [[],[]]
orangeWay = [[],[]]
isRunning = False
greenIsRunning = False
orangeIsRunning = False


while (1):
    #Chaque robot qui entre dans la zone d'entrée envoie sa voie et son temps, on vérifie l'ip pour ne l'ajouter qu'une fois dans la liste
    #On ajoute dans la liste l'ip u robot ainsi que son timing de la façon suivante liste = [[ip1,tps1],[ip2,tps2],..]
    if(listener.mailbox):    
        msg = listener.mailbox.pop(0).split()
        if (msg[0] == "RED" and msg[1] not in orangeWay[0]):
            orangeWay[0].append(msg[1])
            orangeWay[1].append(msg[2])
        elif (msg[0]== "GREEN" and msg[1] not in greenWay[0]):
            greenWay[0].append(msg[1])
            greenWay[1].append(msg[2])
        #Si le robot n'est plus dans la zone d'entrée/conflit alors on le supprime des listes de passage
        elif (msg[0]== "OOC"):
            utils.deleteColumnContainingIP(greenWay, msg[1])
            utils.deleteColumnContainingIP(orangeIsRunning, msg[1])

    print(greenWay)
    print(orangeWay)

    #Si on est en cours de traitement
    if(isRunning == True):
        if(greenIsRunning == True):
            for elt in greenWay[0]:
                sender.sendMessage(elt + " " + "YES")
            #Une fois que tous les robots de liste vertes sont passés alors la liste est vide et on peut faire passer ceux de la liste orange
            if(not greenWay):
                greenIsRunning = False
                orangeIsRunning = True
                
        if(orangeIsRunning == True):
            for elt in orangeWay[0]:
                sender.sendMessage(elt + " " + "YES")
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
        if(greenWay[1] and orangeWay[1]):
            if (greenWay[1][0] < orangeWay[1][0] ):
                isRunning = True
                greenIsRunning = True
            #Orange prioritaire
            elif ( greenWay[1][0] > orangeWay[1][0] ):
                isRunning = True
                orangeIsRunning = True
            #Si les temps sont égaux alors ont choisit arbitrairement l'orange comme voie prioritaire
            else:
                isRunning = True
                orangeIsRunning = True
        elif(not(greenWay) and not(orangeWay)):
            isRunning=False
            orangeIsRunning=False
            greenIsRunning=False
        elif(not(greenWay)):
            isRunning=True
            orangeIsRunning=True
        else:
            isRunning=True
            greenIsRunning=True