import RPi.GPIO as GPIO
import time
chn_h1 = [0,1,2,3,4,5,6,7]
chn_h2 = [8,9,10,11,12,13,14,15]
cmdlist = [0x3b,0x0e,0x02,0x01,0x01,0x01,0x01,0x01,0x00]
msglist = ['A' ,'D' ,'M' ,'-' ,'R' ,'a' ,'s' ,'p' ,0x00]
count = 0
cmdval = 0
msgval= 0

#define the functions before its called
#get cmdval for the setting the LCD mode
def get_cmdval():
    global cmdval
    global cmdlist
    cmdval = cmdlist[count]
    return(cmdval)

#get msgval for the LCD to be displayed
def get_msgval():
    global msgval
    global msglist
    msgval = msglist[count]
    return(msgval)

#output a cmdvalue to a LCD 
def out_cmdval():
    for x in range(0,7):
        global cmdval
        y = cmdval >>x
        y &= 1
        GPIO.output(x,y)
    return()
    
#output a msgvalue to a LCD
def out_msgval():
    for x in range(0,7):
        global msgval
        y = ord(msgval) >>x
        y &= 1
        GPIO.output(x,y)
    return()

#strobe message and command RS(10),RW(9),E(8)
def out_cmdstrobe():
    #clear all pins
    global chn_h2
    GPIO.output(chn_h2,0)
    # RS is 0 and then E is toggled
    GPIO.output(10,1)
    GPIO.output(10,0)
    return()

def out_msgstrobe():
    #clear all pins
    global chn_h2
    GPIO.output(chn_h2,0)
    # RS is made 1 and then E is toggled
    GPIO.output(8,1)
    GPIO.output(10,1)
    GPIO.output(10,0)
    GPIO.output(8,0)
    return()

# the main program start here

GPIO.setmode(GPIO.BCM)
GPIO.setup(chn_h1,GPIO.OUT)
GPIO.setup(chn_h2,GPIO.OUT)
# Step 1 is to configure the LCD as 8 bit 2 line
count = 0;
while count< 8:
    global cmdval
    cmdval = get_cmdval()
    out_cmdval()
    out_cmdstrobe()
    count +=1
    time.sleep(0.1)
# Step 2 is to send the message    
count = 0
while count< 8:
    global cmdval
    msgval = get_msgval()
    out_msgval()
    out_msgstrobe()
    count +=1
    time.sleep(0.1)

