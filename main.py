#main.py
#By Tyler Spadgenske

import getcmd

def main(DEBUG=False):
    #Main loop
    while True:
        #Command getting loop
        while True:
            #Get the command and convert it to a list
            cmd = getcmd.get().split()
            if DEBUG: print cmd
            #If first word is "cyclops" Command is for robot so exit command loop
            if cmd[0].lower() == 'cyclops':
                break

        cmd.pop(0)
        num = 0
        for word in cmd:
            cmd[num] = word.lower()
            num += 1
        print cmd

        master_command = ''
        #Determin master command
        if cmd[0] == 'what':
            master_cmd = 'what'
        elif cmd[0] == 'walk':
            master_cmd = 'walk'
        elif cmd[0] == 'pickup':
            master_cmd = 'pickup'
        elif cmd[0] == 'set down':
            master_cmd = 'set down'
        elif cmd[0] == 'where':
            master_cmd = 'where'
        elif cmd[0] == 'take':
            master_cmd = 'take'
        elif cmd[0] == 'set':
            master_cmd = 'set'
        elif cmd[0] == 'tell':
            master_cmd = 'tell'
        elif cmd[0] == 'who':
            master_cmd = 'who'
        print master_command        
            
main(DEBUG=True)

