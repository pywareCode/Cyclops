# -*- coding: utf-8 -*-
#Commands
#By Tyler Spadgenske

import datetime, time, random
from tts import say

class What(object):
    def __init__(self, cmd, DEBUG=False):
        self.DEBUG = DEBUG
        self.cmd = cmd
        #Remove 'what' from command
        self.cmd.pop(0)
        #Run math() if math problem
        if cmd[0] == 'is' and cmd[1] != 'your':
            #Remove 'is' from command
            self.cmd.pop(0)
            self.math()
        #Run time() if time question
        if cmd[0] == 'time' or cmd[0] == 'day':
            self.time()
        if self.cmd[0] == 'is' and self.cmd[1] == 'your':
            self.cmd.pop(0)
            self.cmd.pop(0)
            self.me()

    def get_month(self, num, num2):
        if num2 == '1':
            self.day = 'January'
        if num2 == '2':
            self.day = 'February'
        if num2 == '3':
            self.day = 'March'
        if num2 == '4':
            self.day = 'April'
        if num2 == '5':
            self.day = 'May'
        if num2 == '6':
            self.day = 'June'
        if num2 == '7':
            self.day = 'July'
        if num2 == '8':
            self.day = 'August'
        if num2 == '9':
            self.day = 'September'
        if num == '1' and num2 == '0':
            self.day = 'October'
        if num == '1' and num2 == '1':
            self.day = 'November'
        if num == '1' and num2 == '2':
            self.day = 'December'
        return self.day
        
    def math(self):
        if self.DEBUG: print 'EQUATION:', self.cmd

        #Check for valid command again
        if len(self.cmd) == 3 or len(self.cmd) == 4:
            pass
        else:
            for i in range(0, 2):
                self.cmd.append(None)
            say('Invalid Command')

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
        except:
            if self.DEBUG: print 'Not, math, looking elsewhere...'

        if self.DEBUG: print 'ANSWER = ', str(self.answer)

    def time(self):
        #Get current time
        self.raw_time = str(datetime.datetime.now()).split()
        #Say time if selected command
        if self.cmd[0].lower() == 'time':
            time = str(self.raw_time[1])
            say('It is ' + time[0] + time[1] + time[2] + time[3] + time[4] + ' AM.')
        #Say day if selected command
        if self.cmd[0].lower() == 'day':
            time = str(self.raw_time[0])
            month = self.get_month(time[5], time[6])
            
            say('Today is ' + month + ' ' + time[-2] + time[-1] + ', ' + time[0] + time[1] + time[2] + time[3])

    def me(self):
        if self.cmd[0] == 'name':
            say('My name is Cyclops of course.')
        if self.cmd[0] == 'phone':
            say("I don't think I should tell you that.")
        if self.cmd[0] == 'email':
            say('My email is cyclopsrobot@gmail.com.')
        if self.cmd[0] == 'problem':
            say("Whatever it is, I don't care.")

#Move onto walking functions
class Walk():
    def __init__(self, cmd=['walk','happy'], DEBUG=False):
        self.cmd = cmd
        self.DEBUG = DEBUG
        print self.cmd
        self.cmd.pop(0)
        if len(self.cmd) != 0:
            if self.cmd[0] == 'forward':
                self.forward()
            if self.cmd[0] == 'backward':
                self.backward()
            if self.cmd[0] == 'left':
                self.left()
            if self.cmd[0] == 'right':
                self.right()

    def forward(self):
        say('Walking Forward')

    def backward(self):
        say('Walking Backward')

    def left(self):
        say('Turning left')

    def right(self):
        say('Turning right')

    def stop(self):
        say('Stopping')    

#Move onto arm functions
class Arm():
    def __init__(self, cmd, DEBUG=False):
        self.cmd = cmd
        self.DEBUG = DEBUG

    def pickup(self):
        try:
            say('Picking up ' + self.cmd[-1])
        except:
            say('Please name object')

    def setdown(self):
        say('Setting down ' + self.cmd[-1])

#Move onto location functions
class Where():
    def __init__(self, cmd, DEBUG=False):
        self.cmd = cmd
        self.DEBUG = DEBUG
        self.cmd.pop(0)
        if len(self.cmd) != 0:
            if self.cmd[-1].lower() == 'i':
                self.here()
            else:
                self.find()

    def here(self):
        say('GPS location module not added. here() called.')

    def find(self):
        say('GPS location module not added. find() called.')

class Take():
    def __init__(self, cmd, DEBUG=False):
        self.cmd = cmd
        self.DEBUG = DEBUG
        self.cmd.pop(0)
        if len(self.cmd) != 0:
            if self.cmd[0].lower() == 'picture':
                self.pic()
            if self.cmd[0].lower() == 'video':
                self.video()

    def pic(self):
        say('Taking Picture')

    def video(self):
        try:
            say('Recording video for ' + self.cmd[2] + ' seconds.')
        except:
            say('Please specify video length.')

class Tell():
    def __init__(self, cmd, DEBUG=False):
        self.cmd = cmd
        self.DEBUG = DEBUG
        self.cmd.pop(0)
        self.cmd.pop(0)
        self.cmd.pop(0)
        if len(self.cmd) != 0:
            if self.cmd[0].lower() == 'joke':
                self.joke()
            if self.cmd[0].lower() == 'riddle':
                self.riddle()

    def joke(self):
        a = ['Canoe.', 'Canoe help me with my homework?']
        b = ['Anee.', 'Anee one you like!']
        c = ['Arfur.', 'Arfur got!']
        d = ['Nana.', 'Nana your business.']
        e = ['Ya.', 'Wow. You sure are excited to see me!']
        f = ['Cows go', 'Cows don’t go who, they go moo!']
        g = ['Etch.', 'Bless you!']

        jokes = [a, b, c, d, e, f, g]
        joke = random.choice(jokes)

        say('Knock Knock.')
        time.sleep(4)
        say(joke[0])
        time.sleep(4)
        say(joke[1])


    def riddle(self):
        a = 'What gets wetter and wetter the more it dries?'
        b = 'You throw away the outside and cook the inside. Then you eat the outside and throw away the inside. What did you eat?'
        c = 'What goes up and down the stairs without moving?'
        d = 'What can you catch but not throw?'
        e = 'I can run but not walk. Wherever I go, thought follows close behind. What am I?'
        f = "What's black and white and red all over?"
        g = 'What goes around the world but stays in a corner?'

        riddles = [a, b, c, d, e, f, g]
        riddle = random.choice(riddles)
        say(riddle)
            
                
    
