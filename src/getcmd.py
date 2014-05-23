#Get Command
#By Tyler Spadgenske
import mic, tts, time

def get():
    microphone = mic.Mic(lmd='models/lm.lm', dictd='models/dic.dic',
                     lmd_persona='models/waitlm.lm', dictd_persona='models/waitdic.dic')
    time.sleep(3)
    while True:
        while True:
            word = microphone.passiveListen('andy')
            if word[1].lower() == 'andy':
                break
        cmd = microphone.activeListen()
        print 'COMMAND: ', cmd
        return cmd

def get_age():
    microphone = mic.Mic(lmd='models/agelm.lm', dictd='models/agedic.dic',
                     lmd_persona='models/waitlm.lm', dictd_persona='models/waitdic.dic')

    print age
    age = activeListen()
    return int(age)

    
    
if __name__ == '__main__':
    get()
        
    
