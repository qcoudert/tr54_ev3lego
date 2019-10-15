import socket

class Server:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.settimeout(0.2)
        self.sock.bind(("", 44444))

    def sendMsg(self, msg):
        self.sock.sendto(msg, ('<broadcast>', 37020))
