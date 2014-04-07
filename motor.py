#Testing the L298N motor driver

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27, True)
GPIO.output(22, False)

p = GPIO.PWM(4, 100) # channel=4  frequency=50Hz
p2 = GPIO.PWM(17, 100)
p2.start(20)
p.start(20)
for e in range(0, 2):
	for i in range(0, 99):
		p.ChangeDutyCycle(i)
		p2.ChangeDutyCycle(i)
		time.sleep(.2)
	for i in range(99, 0):
		p.ChangeDutyCycle(i)
		p2.ChangeDutyCycle(i)
		time.sleep(.2)
GPIO.output(27, False)
GPIO.output(22, False)
p.stop()
GPIO.cleanup()
