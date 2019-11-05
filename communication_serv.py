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
        
        self.toSendMutex = True                                             #Mutex used to access the 'toSend' stack pile
        self.toSend = ["EOS"]                                               #Stack pile stocking the messages to send

        self.receivedMutex = True                                           #Mutex used to access the 'receivedMsg' stack pile
        self.receivedMsg = ["EOS"]                                          #Stack pile stocking the received messages

    def sendMsg(self):
        if(self.toSendMutex):
            self.toSendMutex = False
            if(self.peekStack(self.toSend)):
                try:
                    self.sock.sendto(self.toSend.pop().encode("utf-8"), (self.broadcastAdd, 37020))
                except OSError as err:
                    print("OS error: {0}".format(err))
                    self.sock.close()
                print("Message sent")
                self.toSendMutex = True
                print("msg sent")

    def queueMsg(self, msg):
        if(self.toSendMutex):
            self.toSendMutex = False
            self.toSend.append(msg)
            self.toSendMutex = True


    def recvMsg(self):
        data, addr = self.sock.recvfrom(1024)
        self.receivedMsg.append(data.decode("utf-8"))

    def getBroadcastAdd(self):
        i = j = len(self.ip)
        while(self.ip[i-1]!='.'):
            i = i-1
        bAdd = self.ip[:(i-j)]
        bAdd = bAdd + '255'
        return str(bAdd)

    def peekStack(self, stack):
        i = len(stack)
        return (stack[i-1]!="EOS")



    def run(self):
        while True:
            if(self.peekStack(self.toSend)):
                self.sendMsg()
            if(self.receivedMutex):
                self.receivedMutex = False
                if(self.peekStack(self.receivedMsg)):
                    brick.display.text(self.recvMsg())
                self.receivedMutex = True
