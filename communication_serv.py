#!/usr/bin/env python3

import socket
from pybricks.tools import print, wait
from threading import Thread
import time
import struct
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
            #self.toSendMutex = False
            try:
                self.sock.sendto(self.toSend.pop().encode('utf-8'), (self.broadcastAdd, 37020))
            except OSError as err:
                print("OS error: {0}".format(err))
                self.sock.close()
            print("Message sent")
            self.toSendMutex = True

    def queueMsg(self, msg):
        if(self.toSendMutex):
            #self.toSendMutex = False
            self.toSend.append(msg)
            self.toSendMutex = True

    def getMsg(self):
        data = None
        if(self.receivedMutex):
            #self.receivedMutex = False
            if(self.peekStack(self.receivedMsg)):
                data = self.receivedMsg.pop()
            self.receivedMutex = True
        return data

    def recvMsg(self):
        data, addr = self.sock.recvfrom(1024)
        print(addr)
        if(addr[0]!=self.ip):
            self.receivedMsg.append(data.decode('utf-8'))
        else:
            data = None
        
        if(data!=None):
            print("Message received")

    def getBroadcastAdd(self):
        i = j = len(self.ip)
        while(self.ip[i-1]!='.'):
            i = i-1
        bAdd = self.ip[:(i-j)]
        bAdd = bAdd + '255'
        return bAdd

    def peekStack(self, stack):
        i = len(stack)
        return (stack[i-1]!="EOS")

    
    def run(self):
        while True:
            self.recvMsg()

 
