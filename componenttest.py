#!/usr/bin/python

from lib.ae_as5047d import as5047d
from lib.genericstepper import genericstepper
import time

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


print(str(encoder_az.readAngle())+"\t"+str(encoder_el.readAngle()))
#stepper_az.moveAngular(0,10,7.0)
#stepper_el.moveAngular(1,10,3.1)
#stepper_az.moveDuration(0,10,1)

stepper_el.moveDuration(0,10,1);
print(str(encoder_az.readAngle())+"\t"+str(encoder_el.readAngle()))

stepper_az.close()
stepper_el.close()