#Get Command
#By Tyler Spadgenske
import mic, tts, time

def get():
    microphone = mic.Mic(lmd='models/lm.lm', dictd='models/dic.dic',
                     lmd_persona='models/waitlm.lm', dictd_persona='models/waitdic.dic')
    print 'Class created...'
    time.sleep(3)
    while True:
        while True:
            word = microphone.passiveListen('cyclops')
            if word[1].lower() == 'cyclops':
                break
        cmd = microphone.activeListen()
        print 'COMMAND: ', cmd
        return cmd
if __name__ == '__main__':
    get()
        
    
