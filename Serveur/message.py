"""This module should have been used to send packed messages in a fancy custom way that would have blown your mind away.

But it wasn't compatible with ev3 mindstorm's version of python :^)

RIP.."""

import struct

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

    def encode(self):
        """Encode the informations to get the data in bytes"""

        data = bytes(0)
        while(self.content):
            info = self.content.pop(0)
            if(type(info)!=str):
                t = self.getTypeString(info)
                data = data + struct.pack('!c'+t, t.encode(), info)
            else:
                t = 's'
                size = len(info)
                data = data + struct.pack('!ci%ds' % size, t.encode(), size, info.encode())
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

