#!/usr/bin/python

#from lib.ae_as5047d import as5047d
#from lib.genericstepper import genericstepper
from lib.gs232b import gs232b
from lib.rotorcontrol import rotorcontrol
import time
import sys
import signal



# orderly shutdown:
def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    stepper_az.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

#initialise
comport = ''

if(len(sys.argv)>1):
    comport = str(sys.argv[1])
else:
    print 'No COM Port given, exiting...'
    sys.exit(1)

#stepper_el = genericstepper()
#stepper_az = genericstepper()
#stepper_el.open(22,27,17,1.8,2,100)
#stepper_az.open(13,6,26,1.8,2,100)

#encoder_az = as5047d()
#encoder_el = as5047d()

#if(encoder_az.open(1)<0):
#    print ("main: encoder_az open error");
#    sys.exit(0);
#if(encoder_el.open(0)<0):
#    print("main: encoder-el open error");
#    sys.exit(0);
    
control = rotorcontrol()
gsparser = gs232b()

if(control.open(stepper_el, stepper_az, encoder_az, encoder_el)==0)
    sys.exit(0)
    
if(gsparser.open(comport)==0)
    sys.exit(0)
    
    
control.run()
gsparser.run(control)




#stepper_az.close()
