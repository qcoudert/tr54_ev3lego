from communication import Server
import time

server = Server()
server.start()
print(server.ip)
print(server.broadcastAdd)

i = 0
while(i < 100):
    print("Iteration " + str(i))
    server.appendMsg(str(time.time()))
    msg = server.readMsg()
    if(msg!=None):
        print(msg)
    time.sleep(1)
    i = i + 1