import RPi.GPIO as GPIO
from time import sleep
 
class PIR():
    # CONSTANTS   
    PIN = 21

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def getState(self):
        GPIO.setup(self.PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        readVal = GPIO.input(self.PIN)
	return readVal

if __name__ == '__main__':
    p = PIR()
    val = 0
    while True:
	newval = p.getState()
	if newval != val:
	    val = newval
	    if val == 1:
	        print "MOTION DETECTED!!"
	    else:
	        print "...all quiet now..."
        sleep(0.25)