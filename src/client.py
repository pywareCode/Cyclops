#Cyclops CLI Client
#By Tyler Spadgenske

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.104'
port = 5150

server.connect((host, port))
data = server.recv(1024)
print bytes.decode(data)

while True:
    data = raw_input('>>')
    server.send(str.encode(data))
    if data == 'exit':
        break


print 'Closing Connection...'
server.close()
