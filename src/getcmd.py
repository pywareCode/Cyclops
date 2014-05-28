#Get Command
#By Tyler Spadgenske
import mic, tts, time, os

class Get_cmd():
    def __init__(self):
        self.microphone = mic.Mic(lmd='models/lm.lm', dictd='models/dic.dic',
                     lmd_persona='models/waitlm.lm', dictd_persona='models/waitdic.dic')
        self.run_client = False
        
    def get(self):
        while True:
            while True:
                self.client_cmd = self.get_client_cmd()
                if self.client_cmd != None:
                    self.cmd = self.client_cmd
                    self.run_client = True
                    break
                
                self.word = self.microphone.passiveListen('ANDY')
                if self.word:
                    break

            if self.run_client != True:
                self.cmd = self.microphone.activeListen()
                self.run_client = False
                
            print 'COMMAND: ', self.cmd
            return self.cmd

    def get_client_cmd(self):
        self.client = None
        if os.path.isfile('/home/pi/ANDY/src/cmd.txt'):
            self.readit = open('/home/pi/ANDY/src/cmd.txt', 'r')
            self.lines = self.readit.readlines()
            if self.lines != []:
                print self.lines[0]
                self.client = self.lines[0]

            os.remove('/home/pi/ANDY/src/cmd.txt')
            self.readit.close()

            self.client = None

        return self.client
def get_age():
    microphone = mic.Mic(lmd='models/agelm.lm', dictd='models/agedic.dic',
                     lmd_persona='models/waitlm.lm', dictd_persona='models/waitdic.dic')
    while True:
        age = microphone.activeListen()
        if age != '':
            break

    age = age.lower().capitalize()
    print age
    return age

    
    
if __name__ == '__main__':
    test = Get_cmd()
    e, r = test.get_client_cmd()
    print e
    print r
        
    
