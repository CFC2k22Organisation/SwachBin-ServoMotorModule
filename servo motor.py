#Code written for IBM Call for code 2K22 (SwachBin)
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm=GPIO.PWM(18, 50)

pwm.start(0)
GPIO.setwarnings(False)
pwm.ChangeDutyCycle(5) # left -90 deg position
sleep(4)
pwm.ChangeDutyCycle(10) # right +90 deg position
sleep(1)
pwm.stop()
GPIO.cleanup()
