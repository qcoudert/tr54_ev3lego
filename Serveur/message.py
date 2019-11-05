
import struct

BROADCAST_MESSAGE = "broadcast"

class Message:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.content = []
    
    def appendMsg(self, value):
        self.content.append(value)

    def encode(self):
        data = bytes()
        for o in self.content:
            if 

    def decode(self, data):
        None
