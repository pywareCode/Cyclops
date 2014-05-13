#Testing the L298N motor driver
#Tyler Spadgenske

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

def step(step=1):
    for i in range(0, step):
        GPIO.output(8, True)
        time.sleep(2)
        GPIO.output(8, False)
        
        #GPIO.output(12, True)
        #time.sleep(1)
        #GPIO.output(12, False)
        
    GPIO.output(8, False)
    GPIO.output(12, False)
    GPIO.cleanup()

def arm():
    pass

if __name__ == '__main__':
    step()
