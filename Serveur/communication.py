import socket
from threading import Thread, RLock
import time
class Server(Thread):

    def __init__(self):
        super(Server, self).__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        #Creating the socket
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)     #Configuring the socket
        self.sock.bind(("", 37020))
        self.sock.setblocking(True)
        self.sock.settimeout(0.5)

        self.ip = socket.gethostbyname(socket.gethostname())                #IP of the server
        self.broadcastAdd = self.__getBroadcastAdd()                        #Broadcast Address the server will be using
        
        self.toSendMutex = RLock()                                           #Mutex used to access the 'toSend' stack pile
        self.toSend = ["EOS"]                                               #Stack pile stocking the messages to send

        self.receivedMutex = RLock()                                         #Mutex used to access the 'receivedMsg' stack pile
        self.receivedMsg = ["EOS"]                                          #Stack pile stocking the received messages

    def __sendMsg(self):
        with self.toSendMutex:
            try:
                self.sock.sendto(self.toSend.pop().encode('utf-8'), (self.broadcastAdd, 37020))
            except OSError as err:
                print("OS error: {0}".format(err))
                self.sock.close()
        print("Message sent\n")

    def __recvMsg(self):
        with self.receivedMutex:
            try:
                data, addr = self.sock.recvfrom(1024)
                if(addr[0]!=self.ip):
                    self.receivedMsg.append(data.decode('utf-8'))
            except BlockingIOError as err:
                print("BlockingIOError: {0}".format(err))
            except socket.timeout:
                None

    def __getBroadcastAdd(self):
        i = j = len(self.ip)
        while(self.ip[i-1]!='.'):
            i = i-1
        bAdd = self.ip[:(i-j)]
        bAdd = bAdd + '255'
        return str(bAdd)

    def peekStack(self, stack):
        i = len(stack)
        if(stack[i-1]!="EOS"):
            return True
        else:
            return False

    def run(self):
        while True:
            if(self.peekStack(self.toSend)):
                self.__sendMsg()

            self.__recvMsg()
    
    def appendMsg(self, msg):
        with self.toSendMutex:
            self.toSend.append(msg)
    
    def readMsg(self):
        with self.receivedMutex:
            msg = None
            if(self.peekStack(self.receivedMsg)):
                msg = self.receivedMsg.pop()
        return msg

