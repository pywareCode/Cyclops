#main.py
#By Tyler Spadgenske
DEBUG = True

import getcmd, cmds
from tts import say

def Cyclops(DEBUG=False):
    #Main loop
    say('Hello. My name is Andy. Please wait while my system starts up.')
    while True:
        print
        #Get the command and convert it to a list
        cmd = getcmd.get().split()
        if DEBUG: print 'COMMAND:', cmd

        num = 0
        for word in cmd:
            cmd[num] = word.lower()
            num += 1
        if len(cmd) == 0:
            cmd.append('')
            say('Not complete command')
        #Determin master command
        if cmd[0] == 'what':
            cmds.What(cmd, DEBUG)
        elif cmd[0] == 'walk' or cmd[0] == 'turn':
            cmds.Walk(cmd, DEBUG)
        elif cmd[0] == 'stop':
            cmds.Walk(cmd, DEBUG).stop()
        elif cmd[0] == 'pickup' or cmd[0] == 'pick' and cmd[1] == 'up':
            cmds.Arm(cmd, DEBUG).pickup()
        elif cmd[0] == 'set' and cmd[1] == 'down':
            cmds.Arm(cmd, DEBUG).setdown()
        elif cmd[0] == 'where':
            cmds.Where(cmd, DEBUG)
        elif cmd[0] == 'take':
            cmds.Take(cmd, DEBUG)
        elif cmd[0] == 'set':
            pass #TODO
        elif cmd[0] == 'tell':
            cmds.Tell(cmd, DEBUG)
        elif cmd[0] == 'who':
            cmds.Who(cmd, DEBUG)
        else:
            say('Not valid command')
            
            
Cyclops(DEBUG=DEBUG)

