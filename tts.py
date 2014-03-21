import sys
import pyttsx
 
# main() function
def say(message='Sorry...... I do not understand.'):
  engine = pyttsx.init()
  engine.say(message)
  engine.runAndWait()
 
# call main
if __name__ == '__main__':
  say()
