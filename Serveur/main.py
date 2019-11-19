from communication import Server
import time
from message import Message
server = Server()
server.start()
print(server.ip)
print(server.broadcastAdd)
msge = Message()
msge.append("Hello")

i = 0
while(i < 100):
    print("Iteration " + str(i))
    server.appendMsg(msge.encode())
    time.sleep(1)
    i = i + 1