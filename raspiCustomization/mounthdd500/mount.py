import os
import time
import RPi.GPIO as GPIO
import time
import atexit

isconnected=False
pin23state=False
blue_led=21
green_led=21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(blue_led,GPIO.OUT)
GPIO.setup(green_led,GPIO.OUT)
# Specify path
path = '/dev/disk/by-label/hdd500'
# GPIO.output(internet_led,GPIO.HIGH)
 
# Check whether the specified
# path exists or not
while True:
    isExist = os.path.exists(path)
    if isExist:
        mountpoint=os.popen("findmnt /media/hdd500").read()
        if "/media/hdd500" in mountpoint:
            print("Already mounted")
            # GPIO.output(green_led,GPIO.HIGH)
        else:
            print("Trying to mount....")
            feed=os.popen("sudo systemctl start media-hdd500.mount").read()
            print(feed)
            if feed.replace("\n","").strip()=="":
                print("Mounnted successfully....")
                mountpoint=os.popen("findmnt /media/hdd500").read()
                print(mountpoint)
                break
                # GPIO.output(green_led,GPIO.HIGH)
                # GPIO.output(blue_led,GPIO.HIGH)
                time.sleep(10)
                # GPIO.output(green_led,GPIO.LOW)
                # GPIO.output(blue_led,GPIO.LOW)

    else:
        print("disk not available.")
    time.sleep(5)

