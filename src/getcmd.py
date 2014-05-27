#Get Command
#By Tyler Spadgenske
import mic, tts, time

class Get_cmd():
    def __init__(self):
        self.microphone = mic.Mic(lmd='models/lm.lm', dictd='models/dic.dic',
                     lmd_persona='models/waitlm.lm', dictd_persona='models/waitdic.dic')
        time.sleep(3)
        
    def get(self):
        while True:
            while True:
                self.word = self.microphone.passiveListen('andy')
                if self.word[1].lower() == 'andy':
                    break
            self.cmd = self.microphone.activeListen()
            print 'COMMAND: ', self.cmd
            return self.cmd

    def get_client_cmd(self):
        self.client = None
        self.goodcmd = False
        self.readit = open('/home/pi/ANDY/src/cmd.txt', 'r')
        self.lines = self.readit.readlines()
        print self.lines[0]
        if self.lines != [] or self.lines != ['']:
            self.goodcmd = True
            self.client = self.lines[0]

        return self.client, self.goodcmd 
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
        
    
