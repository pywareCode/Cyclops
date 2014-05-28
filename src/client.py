
#Andy CLI Client
#By Tyler Spadgenske

import socket, sys, time

class Client():
    def __init__(self):
        self.logo()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '192.168.0.104'
        self.port = 5150
        try:
            self.server.connect((self.host, self.port))
            self.data = self.server.recv(1024)
            print bytes.decode(self.data)
        except:
            print 'Cannot Connect to Andy'
            time.sleep(10)
            sys.exit()

        
    def logo(self):
        print'           _   _ _______     __'
        print'     /\   | \ | |  __ \ \   / /'
        print'    /  \  |  \| | |  | \ \_/ / '
        print'   / /\ \ | . ` | |  | |\   /  '
        print'  / ____ \| |\  | |__| | | |   '
        print' /_/    \_\_| \_|_____/  |_|'
        print'+++++++++++++++++++++++++++++++++++++++++++++++'                             
        print
        print 'ANDY Humanoid Robot CLI Interface'
        print 'Copyright (c) 2014 Tyler Spadgenske'
        print
        print '+++++++++++++++++++++++++++++++++++++++++++++++'
        print 'Type "cmds" for list of cmds, "help" for help, "exit" for exiting.'

    def send_cmd(self):

        while True:
            self.data = raw_input('>>')
            self.server.send(str.encode(self.data))
            if self.data == 'exit':
                break

    def end(self):
        print 'Closing Connection...'
        self.server.close()

if __name__ == '__main__':
    cli = Client()
    cli.send_cmd()
