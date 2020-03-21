import RPi.GPIO as GPIO
import time

chn_h1 = [0,1,2,3,4,5,6,7]
seglist  = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x67,0x77,0x7c,0x39,0x5e,0x79,0x71,0x00]
global count
global hexval

#define the functions before its called
#get hexval for the count
def get_hexval():
    global hexval
    hexval = seglist[count]
    return(hexval)

#output a hexvalue to a port
def out_hexval():
    for x in range(0,7):
        global hexval
        y = hexval >>x
        y &= 1
        GPIO.output(x,y)
    return()
    
# the main program start here

GPIO.setmode(GPIO.BCM)
GPIO.setup(chn_h1,GPIO.OUT)
count = 0;
while count< 16:
    global hexval
    hexval = get_hexval()
    out_hexval()
    count +=1
    time.sleep(1)


