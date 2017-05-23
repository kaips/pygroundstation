#!/usr/bin/python

import smbus
import time

i2c = smbus.SMBus(1)

HMC5883_ID = 0x1E

def twos_complement(val, nbits):
    """Compute the 2's complement of int value val"""
    if val < 0:
      val = (1 << nbits) + val
    else:
      if (val & (1 << (nbits - 1))) != 0:
        val = val - (1 << nbits)
    return val


for cmd in range(1,20):

  i2c.write_byte_data(HMC5883_ID,2, 1); # single measurement mode
  
  #print("Status: "+str(i2c.read_byte_data(HMC5883_ID,9)));
  # wait for DRDY

  xhb = i2c.read_byte_data(HMC5883_ID,3)
  xlb = i2c.read_byte_data(HMC5883_ID,4)
  
  zhb = i2c.read_byte_data(HMC5883_ID,5)
  zlb = i2c.read_byte_data(HMC5883_ID,6)
  
  yhb = i2c.read_byte_data(HMC5883_ID,7)
  ylb = i2c.read_byte_data(HMC5883_ID,8)
  
  #i2c.write_byte(HMC5883_ID,3);
  
  xmag = (xhb<<8)|xlb;
  ymag = (yhb<<8)|ylb;
  zmag = (zhb<<8)|zlb;
  
  xmag = twos_complement(xmag,16);
  ymag = twos_complement(ymag,16);
  zmag = twos_complement(zmag,16);
  
  
  #print("Status: "+str(i2c.read_byte_data(HMC5883_ID,9)));
  print("cmd: "+str(cmd)+"\t"+str(xmag)+"\t"+str(ymag)+"\t"+str(zmag))

  #print("xhb: "+str(xhb)+" xlb: "+str(xlb))
  #print("xhb: "+str(yhb)+" xlb: "+str(ylb))
  #print("xhb: "+str(zhb)+" xlb: "+str(zlb))
  
  time.sleep(1)