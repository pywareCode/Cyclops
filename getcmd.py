#Get Command
#By Tyler Spadgenske
import sttwin

def get(THRESHOLD, DEBUG=False):
    while True:
        raw_data = sttwin.listen_for_speech(threshold=THRESHOLD)
        try:
            data = raw_data[0][0]['utterance'].split()
            if DEBUG: print data
            if data[0].lower() == 'cyclops':
                return data
                break
        except:
            pass
    
