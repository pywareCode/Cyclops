#Testing the L298N motor driver
#Tyler Spadgenske

#Pins:
#21: Left Leg Backward
#22: Left Leg Forward

#16: Right Leg Forward
#15: Right Leg Backward

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

#Setup left foot objects
left_backward = GPIO.PWM(21, 100)
left_forward = GPIO.PWM(22, 100)

#Setup right foot objects
right_backward = GPIO.PWM(18, 100)
right_forward = GPIO.PWM(19, 100)
def step(step=1):
    left_forward.start(50)
    time.sleep(5)
    left_forward.stop()
        
    #GPIO.output(22, True)
    #time.sleep(.4)
    #GPIO.output(22, False)
    #time.sleep(2)

    #GPIO.output(19, True)
    #time.sleep(.4)
    #GPIO.output(19, False)
    #time.sleep(2)
        
    #GPIO.output(21, True)
    #time.sleep(.4)
    #GPIO.output(21, False)
    #time.sleep(2)
        
    GPIO.output(18, False)
    GPIO.output(19, False)
    GPIO.output(21, False)
    GPIO.output(22, False)
    GPIO.cleanup()

def arm():
    pass

if __name__ == '__main__':
    step()
