#Servo Control
#By Tyler Spadgenske

#import libraries
import time
import RPi.GPIO as GPIO

class Servo():
    def __init__(self):
        self.DEBUG = True
        #Setup GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT)

        #Setup PWM
        self.frequency = 50#Hertz
        self.left_ankle = GPIO.PWM(7, self.frequency)

        #Setup duty cycles
        self.RIGHT = .4
        self.CENTER = 1.5
        self.LEFT = 2.5

        self.msPerCycle = 1000 / self.frequency

    def move(self, position, servo):
        self.dutyCyclePercentage = position * 100 / self.msPerCycle
        if self.DEBUG:
            print 'Position: ' + str(position)
            print 'Duty Cycle: ' + str(self.dutyCyclePercentage) + '%'
            print

        servo.start(self.dutyCyclePercentage)
        
    def cleanup(self):
        self.left_ankle.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    test = Servo()
    try:
        while True:
            test.move(test.RIGHT, test.left_ankle)
            time.sleep(1)
            print 'right'
            test.move(test.LEFT, test.left_ankle)
            time.sleep(1)
            print 'left'
            test.move(test.CENTER, test.left_ankle)
            print 'center'
            time.sleep(1)
    except:
        test.cleanup()
