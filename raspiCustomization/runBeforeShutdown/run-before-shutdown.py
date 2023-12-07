import RPi.GPIO as GPIO
import time
import atexit

internet_led=21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(internet_led,GPIO.OUT)
for i in range(15):
	GPIO.output(internet_led,GPIO.HIGH)
	time.sleep(.2)

	GPIO.output(internet_led,GPIO.LOW)
	time.sleep(.2)

