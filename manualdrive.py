#!/usr/bin/python

from lib.ae_as5047d import as5047d
from lib.genericstepper import genericstepper
import time
import signal
import sys

# orderly shutdown:
def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    stepper_az.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
#print('Press Ctrl+C')
#signal.pause()

#initialise
stepper_el = genericstepper()
stepper_az = genericstepper()
stepper_el.open(22,27,17,1.8,2,100)
stepper_az.open(13,6,26,1.8,2,100)

encoder_az = as5047d()
encoder_el = as5047d()

if(encoder_az.open(1)<0):
    print ("main: encoder_az open error");
if(encoder_el.open(0)<0):
    print("main: encoder-el open error");


while 1:
    
    try:
        move_az = int(raw_input('Move Az:'))
        move_az_time = float(raw_input('Time Az:'))
        move_az_dir = float(raw_input('Dire Az:'))
        move_el = int(raw_input('Move El:'))
        move_el_time = float(raw_input('Time El:'))
        move_el_dir = float(raw_input('Dire Az:'))
    except ValueError:
        print "Not a number"
        continue

    print("Pre: "+str(encoder_az.readAngle())+"\t"+str(encoder_el.readAngle()))    
    
    stepper_az.moveDuration(move_az_dir,move_az,move_az_time)
    stepper_el.moveDuration(move_el_dir,move_el,move_el_time);
    
    print("Post: "+str(encoder_az.readAngle())+"\t"+str(encoder_el.readAngle()))

stepper_az.close()
