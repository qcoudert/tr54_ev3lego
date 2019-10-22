import socket
from threading import Thread

class Communication(Thread):

    def __init__(self):
        Thread.__init__(self)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.bind(("", 37020))

        self.rcvData = ["EOS"]

    def listen(self):
        return self.rcvData
    
    def run(self):
        while True: 
            data, addr = self.sock.recvfrom(1024)
            self.rcvData.append(data)


