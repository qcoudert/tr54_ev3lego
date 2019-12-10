from threading import Thread
import socket

class NetworkListener(Thread):
    """Class allowing the server to listen any message that came through network

    This class is using a socket to listen any UDP broadcast sent to the port 37020.
    This listener is running asynchronously and should be started with NetworkListener.start()
    """

    def __init__(self):
        super(NetworkListener, self).__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)        #Creating the socket
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)     #Configuring the socket
        self.sock.bind(("", 37020))                                         #Bind the socket to listen any message on port 37020
        self.sock.setblocking(0)
        self.sock.settimeout(None)

        self.ip = socket.gethostbyname(socket.gethostname())                #IP of the server

        self.mailbox = []                                                   #Array that contains any message listened
        
    def __listen(self):
        """Listen any message that comes through port 37020"""
        data = None
        print("Listening...")
        try:
            data, addr = self.sock.recvfrom(1024)
            print('----------------')
            print('Received message')
            print(self.ip)
            print(addr)
            print('----------------')
            if(addr[0]!=self.ip):
                self.mailbox.append(data.decode('utf-8'))
        except BlockingIOError as err:
            print("BlockingIOError: {0}".format(err))
        except socket.timeout:
            None

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
        self.broadAddr = self.getBroadcastAdd()

    def getBroadcastAdd(self):
        i = j = len(self.ip)
        while(self.ip[i-1]!='.'):
            i = i-1
        bAdd = self.ip[:(i-j)]
        bAdd = bAdd + '255'
        return bAdd

    def sendMessage(self, message):
        """Broadcast a string message with the provided socket"""
        try:
            self.sock.sendto(message.encode('utf-8'), (self.broadAddr, 37020))
            
        except OSError as err:
            print("OS error: {0}".format(err))

