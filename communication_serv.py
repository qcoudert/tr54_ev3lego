import socket
from pybricks.tools import print

class Server:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def sendMsg(self, msg):
        try:
            self.sock.sendto(msg, ("192.168.43.255", 37020))
        except OSError as err:
            print("OS error: {0}".format(err))
            self.sock.close()