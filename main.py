#!/usr/bin/python

#from lib.ae_as5047d import as5047d
#from lib.genericstepper import genericstepper
from lib.gs232b import gs232b
import time
import sys

#stepper_el = genericstepper()
#stepper_az = genericstepper()
#stepper_el.open(22,27,17,1.8,2,100)
#stepper_az.open(13,6,26,1.8,2,100)

#encoder_az = as5047d()
#encoder_el = as5047d()

#if(encoder_az.open(1)<0):
#    print ("main: encoder_az open error");
#if(encoder_el.open(0)<0):
#    print("main: encoder-el open error");

comport = ''

if(len(sys.argv)>1):
    comport = str(sys.argv[1])
    
    gsparser = gs232b()
    gsparser.open(comport)
    
else:
    print 'No COM Port given, exiting...'
    sys.exit(1)
    
    





#stepper_az.close()
#stepper_el.close()