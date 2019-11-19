from threading import Thread
import socket
from pybricks.tools import print
import ipaddress
import struct

class NetworkListener(Thread):
    """Class allowing users to listen any message that came through network

    This class is using a socket to listen any UDP broadcast sent to the port 37020.
    This listener is running asynchronously and should be started with NetworkListener.start()
    """

    def __init__(self, ip):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        #Creating the socket
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)     #Configuring the socket
        self.sock.bind(("", 37020))                                         #Bind the socket to listen any message on port 37020

        self.ip = ip                                                        #IP of the user

        self.mailbox = []                                                   #Array that contains any message listened
        
    def __listen(self):
        """Listen any message that comes through port 37020"""
        data = None
        msg = Message()
        try:
            data, addr = self.sock.recvfrom(1024)
        except OSError as err:
            print("OSError: {0}".format(err))
        #TODO: Create filter so that addr is different from self.ip (addr is a bytes array so HF :^) )
        if(data!=None):
            self.mailbox.append(msg.decode(data))   #Decode the data with the Message class
            print(addr)
            print(ipaddress.IPv4Address(addr[4:8]))
            print("------------")

    def run(self):
        while(1):
            self.__listen()

class MessageSender:

    def __init__(self, ip, socket):
        """Initialize the object

        'ip' must be a string with the ip of the user
        'socket' will be the socket object used to UDP broadcast messages
        socket should often use the same socket than the NetworkListener in this project
        """

        self.sock = socket  #Socket object used to broadcast messages
        self.ip = ip   #IP of the user
        self.content = Message()

    def getBroadcastAdd(self):
        i = j = len(self.ip)
        while(self.ip[i-1]!='.'):
            i = i-1
        bAdd = self.ip[:(i-j)]
        bAdd = bAdd + '255'
        return bAdd

    def append(self, data):
        self.content.append(data)

    def sendMessage(self):
        """Broadcast a string message with the provided socket"""
        if(self.content.isEmpty()):
            return -1

        try:
            self.sock.sendto(self.content.encode(), (self.getBroadcastAdd(), 37020))    #Encode the data with the Message class and then broadcast it   
        except OSError as err:
            print("OS error: {0}".format(err))
        finally:
            print("Sent:{0}".format(self.content.content.pop()))
            self.content = Message()
        
        return 0

TYPE_SWITCHER = {
    int: 'i',
    float: 'f',
    str: 's',
    bool: 'b',
}

class Message:
    """Class used to pack and unpack messages sent through a socket

    An unlimited number of different natives objects (int, float, bool, string, char) can be sent.
    Append information in your Message with append(data) and encode it with encode() to return the bytes data.
    If you want to decode a Message, use decode(data) and all the informations will be stored in Message.content"""

    def __init__(self):
        self.content = []
    
    def append(self, data):
        """Append the information into an array"""

        self.content.append(data)

    def isEmpty(self):
        """Return True if the message does not contain any information"""

        if(self.content):
            return False
        else:
            return True

    def encode(self):
        """Encode the informations to get the data in bytes"""

        data = bytes(0)
        while(self.content):
            info = self.content.pop(0)
            if(type(info)!=str):
                t = self.getTypeString(info)
                data = data + struct.pack('!i'+t, t.encode(), info)
            else:
                t = 's'
                size = len(info)
                data = data + struct.pack('!ii%ds' % size, t.encode(), size, info.encode())
        return data
    
    def decode(self, data):
        """Decode the data and store it in the self.content array"""

        self.content = []
        currentByte = 0
        dataSize = len(data)

        while(currentByte<dataSize):
            t = struct.unpack('!c', data[currentByte:currentByte+1])[0].decode()
            currentByte+=1
            if(t!='s'):
                self.content.append(struct.unpack('!'+t, data[currentByte:currentByte+struct.calcsize(t)])[0]) #Unpack the next info (assumed of 't' type) and add it to the array
                currentByte+=struct.calcsize(t)
            else:
                ssize = struct.unpack('!i', data[currentByte:currentByte+4])[0]
                currentByte+=4
                self.content.append(struct.unpack('!%ds' % ssize, data[currentByte:currentByte+ssize])[0].decode())
                currentByte+=ssize


    def getTypeString(self, data):
        """Get the format string that match the data"""
        
        return TYPE_SWITCHER.get(type(data), 'i')


