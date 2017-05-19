#!/usr/bin/python


stepper_az = genericstepper()
stepper_el = genericstepper()
stepper_az.open(13,6,26,1.8,2,100)
stepper_el.open(22,27,17,1.8,2,100)

encoder_az = ae_as5047d()
if(encoder_az.open(1)<0):
    print ("main: encoder_az open error");
