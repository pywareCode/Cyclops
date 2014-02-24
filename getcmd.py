#Get Command
#By Tyler Spadgenske
import sttwin

def get(DEBUG=False):
    while True:
        data = sttwin.listen_for_speech()
        try:
            if DEBUG: print data[0][0]['utterance']
            return data[0][0]['utterance']
            break
        except:
            pass
    
