from network import NetworkListener, MessageSender
import utils
import time

listener = NetworkListener()
listener.start()
sender = MessageSender()
print(listener.ip)

greenWay = [[],[]]              #[[IP du véhicule sur la voie verte],[Heure d'entrée sur la voie verte]]
orangeWay = [[],[]]             #[[IP du véhicule sur la voie orange],[Heure d'entrée sur la voie orange]]
isRunning = False               #Faux si aucune permission n'est actuellement accordée, Vrai si une permission est actuellement accordée à une voie
greenIsRunning = False          #Faux si les véhicules de la voie verte n'ont pas la permission de passer, vrai sinon
orangeIsRunning = False         #Faux si les véhicules de la voie verte n'ont pas la permission de passer, vrai sinon


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
            utils.deleteColumnContainingIP(orangeWay, msg[1])

    print(greenWay)
    print(orangeWay)

    #Si on est en cours de traitement
    if(isRunning == True):
        if(greenIsRunning == True):
            if(greenWay[0]):
                for elt in greenWay[0]:
                    sender.sendMessage(elt + " " + "YES")
            greenIsRunning = False
            isRunning = False
        elif(orangeIsRunning == True):
            if(orangeWay[0]):
                for elt in orangeWay[0]:
                    sender.sendMessage(elt + " " + "YES")
            orangeIsRunning = False
            isRunning = False
        else:
            isRunning = False

    #Si on est pas déjà en cours de traitement
    if (isRunning == False):
        #On compare les liste pour savoir quelle voie est prioritaire (celle qui a eu le premier véhicule arrivé est prioritaire)
        if(greenWay[1] and orangeWay[1]):
            #Vert prioritaire
            if (greenWay[1][0] < orangeWay[1][0] ):
                isRunning = True
                greenIsRunning = True
            #Orange prioritaire
            elif ( greenWay[1][0] >= orangeWay[1][0] ):
                isRunning = True
                orangeIsRunning = True
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