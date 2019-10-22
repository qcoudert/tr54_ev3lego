import socket
from pybricks.tools import print
from threading import Thread
class Server(Thread):

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        #Creating the socket
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)     #Configuring the socket

        self.ip = self.sock.getsockname()[0]                                #IP of the server
        self.broadcastAdd = self.getBroadcastAdd                            #Broadcast Address the server will be using
        
        self.toSendMutex = True                                            #Mutex used to access the 'toSend' stack pile
        self.toSend = ["EOS"]                                               #Stack pile stocking the messages to send

        self.receivedMutex = True                                           #Mutex used to access the 'receivedMsg' stack pile
        self.receivedMsg = ["EOS"]                                          #Stack pile stocking the received messages

    def sendMsg(self):
        if(self.toSendMutex):
            self.toSendMutex = False
            try:
                self.sock.sendto(toSend.pop(), (self.broadcastAdd, 37020))
            except OSError as err:
                print("OS error: {0}".format(err))
                self.sock.close()
            self.toSendMutex = True

    def getBroadcastAdd(self):
        i = j = len(self.ip)
        while(self.ip[i-1]!='.')
            i = i-1
        bAdd = self.ip[:(i-j)]
        bAdd = bAdd + '255'
        return bAdd

    def peekStack(stack):
        i = len(stack)
        if(stack[i-1]!="EOS"):
            return False
        else:
            return True
    
    def run(self):
        while True:
            if(peekStack(self.toSend)):
                sendMsg()
            

