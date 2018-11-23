import RPi.GPIO as GPIO
from time import sleep
 
class PIR():
    # CONSTANTS   
    PIN = 21

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def inAlarm(self):
        GPIO.setup(self.PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        readVal = GPIO.input(self.PIN)
        return readVal

if __name__ == '__main__':
    p = PIR()
    while True:
        value = p.inAlarm()
        print value
        sleep(1)