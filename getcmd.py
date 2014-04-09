#Get Command
#By Tyler Spadgenske
import sttwin, cmds

def get(THRESHOLD, DEBUG=False):
    while True:
        raw_data = sttwin.listen_for_speech(threshold=THRESHOLD)
        try:
            data = raw_data[0][0]['utterance'].split()
            if data[0].lower() == 'cyclops' or data[0].lower() == 'psy' or data[0].lower() == 'si':
                return data
                break
            if data[0].lower() == 'stop':
                cmds.Walk(DEBUG=DEBUG).stop()
        except:
            pass
    
