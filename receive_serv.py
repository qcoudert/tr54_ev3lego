#!/usr/bin/env python3

import socket
from pybricks.tools import print, wait
from threading import Thread
import time
import string
class Server(Thread):

    def __init__(self, ip):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        #Creating the socket
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)     #Configuring the socket
        self.sock.bind(("", 37020))

        self.ip = ip                                                        #IP of the server
        self.broadcastAdd = self.getBroadcastAdd()                          #Broadcast Address the server will be using

        self.receivedMsg = ["EOS"]                                          #Stack pile stocking the received messages

   
    def getMsg(self):
        data = None
        if(self.receivedMutex):
            if(self.peekStack(self.receivedMsg)):
                data = self.receivedMsg.pop()
        return data

    def recvMsg(self):
        data, addr = self.sock.recvfrom(1024)
        self.receivedMsg.append(data.decode("utf-8"))

    def peekStack(self, stack):
        i = len(stack)
        return (stack[i-1]!="EOS")

    def run(self):
        while True:
            self.recvMsg()
