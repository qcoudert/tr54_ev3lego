import socket

class Communication:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.sockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.bind(("", 37020))

        self.rcvData = ["EOS"]

    def listen(self):
        data, addr = self.sock.recvfrom(1024)
        self.rcvData.append(data)