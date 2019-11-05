""" from communication import Server
import time

server = Server()
server.start()
print(server.ip)
print(server.broadcastAdd)

i = 0
while(i < 10):
    print("Iteration " + str(i))
    server.appendMsg("Je suis si seul :'(")
    msg = server.readMsg()
    if(msg!=None):
        print(msg)
    time.sleep(1)
    i = i + 1 """

import struct

data = bytes()
data += struct.pack('lh', 1234, 1)

print(data[0:4])

res = struct.unpack('l', data[0:4])

print(res)