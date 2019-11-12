"""from communication import Server
import time

server = Server()
server.start()
print(server.ip)
print(server.broadcastAdd)

i = 0
while(i < 100):
    print("Iteration " + str(i))
    server.appendMsg("Yo")
    msg = server.readMsg()
    if(msg!=None):
        print(msg)
    time.sleep(1)
    i = i + 1"""

from message import Message

send = Message()
send.append(1)
send.append(1423)
send.append('Salut')

print(send.getTypeString(1))
data = send.encode()

recv = Message()
recv.decode(data)

print(recv.content)
