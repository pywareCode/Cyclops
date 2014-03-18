import wiringpi2 as wiringpi  
import time  
  
pin_base = 65       # lowest available starting number is 65  
i2c_addr = 0x20     # A0, A1, A2 pins all wired to GND  
  
wiringpi.wiringPiSetup()                    # initialise wiringpi  
wiringpi.mcp23017Setup(pin_base,i2c_addr)   # set up the pins and i2c address  
  
wiringpi.pinMode(65, 1)         # sets GPA0 to output  
wiringpi.digitalWrite(65, 0)    # sets GPA0 to 0 (0V, off)   
  
# Note: MCP23017 has no internal pull-down, so I used pull-up and inverted  
# the button reading logic with a "not"  
while True:  
	wiringpi.digitalWrite(65, 1) # sets port GPA1 to 1 (3V3, on)
	time.sleep(1)
	wiringpi.digitalWrite(65, 0)
	time.sleep(1)
