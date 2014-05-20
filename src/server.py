#Cyclops server test
#By Tyler Spadgenske

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 5150
server.bind((host, port))
server.listen(5)
print 'Listing for a client...'
client, addr = server.accept()
print      'Accepted connection from ', addr
client.send(str.encode('Welcome to The Cyclops server!'))

while True:
    data = client.recv(1024)
    if bytes.decode(data) == 'exit':
        break
    else:
        print 'Recieved data from client: ', bytes.decode(data)

print 'Closing connection...'
client.send(str.encode('exit'))
client.close()
            
