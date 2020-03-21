import RPi.GPIO as GPIO
import time
GPIO.RPI_INFO
chn_hi = [0,2,4,6]
chn_lo = [1,3,5,7]
chn_h1 = [0,1,2,3,4,5,6,7]
chn_h2 = [8,9,10,11,12,13,14,15]
chn_h3 = [16,17,18,19,20,21,22,23]


i=10

GPIO.setmode(GPIO.BCM)


GPIO.setup(chn_h1,GPIO.OUT)
GPIO.setup(chn_h2,GPIO.OUT)
GPIO.setup(chn_h3,GPIO.OUT)
#we now output blink to the h1 ports
GPIO.output(chn_h1,0)
GPIO.output(chn_h1,1)
GPIO.output(chn_h1,0)
time.sleep(1)
#we now output blink to the h1 ports
GPIO.output(chn_h2,0)
GPIO.output(chn_h2,1)
GPIO.output(chn_h2,0)
time.sleep(1)
#we now output blink to the h1 ports
GPIO.output(chn_h3,0)
GPIO.output(chn_h3,1)
GPIO.output(chn_h3,0)
time.sleep(1)
