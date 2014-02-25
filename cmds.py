#Commands
#By Tyler Spadgenske

class What(object):
    def __init__(self, cmd, DEBUG=False):
        if DEBUG: print 'Running Command...'
        self.cmd = cmd
        self.cmd.pop(0)
        self.cmd.pop(0)
        self.DEBUG = DEBUG
        
    def math(self):
        if self.DEBUG: print 'EQUATION:', self.cmd

        #Check for valid command again
        if len(self.cmd) == 3 or len(self.cmd) == 4:
            pass
        else:
            for i in range(0, 2):
                self.cmd.append(None)
            if self.DEBUG: print 'Invalid Command'

        #Solve problem
        self.answer = None
        try:
            if self.cmd[1] == 'plus':
                self.answer = int(self.cmd[0]) + int(self.cmd[2])
            elif self.cmd[1] == 'minus':
                self.answer = int(self.cmd[0]) - int(self.cmd[2])
            elif self.cmd[1] == 'times':
                self.answer = int(self.cmd[0]) * int(self.cmd[2])
            elif self.cmd[1] == 'divided':
                self.answer = int(self.cmd[0]) / int(self.cmd[3])
            else:
                if self.DEBUG: print 'Invalid Equation'
        except:
            if self.DEBUG: print 'Invalid Imput'

        if self.DEBUG: print 'ANSWER = ', str(self.answer)
            
        
    
