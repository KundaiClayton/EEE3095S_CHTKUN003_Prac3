#import dependancie
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

#variable for button GPIO pin
button=18
#variable for LED pin
LED=24

#setup button
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#setup led
GPIO.setup(LED,GPIO.OUT)

#button state
ButtonPressed=False

try:
	while(1):
		if GPIO.input(button)==0:
			print "Button pressed"
			if ButtonPressed==False:
				GPIO.output(LED,True)
				print "LED ON"
				ButtonPressed=True
				sleep(0.5)

			else:
				GPIO.output(LED,False)
				print "LED OFF"
				ButtonPressed=False
				sleep(0.5)
finally:
	GPIO.cleanup()
