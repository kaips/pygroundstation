#!/usr/bin/python

from absoluteencoder import absoluteencoder
import spidev
import time
from pprint import pprint

class as5047d(absoluteencoder):

  READ = 1
  WRITE = 0
  NOP = 	0x0000
  ERRFL = 	0x0001
  DIAAGC=	0x3FFC
  MAG = 	0x3FFD
  ANGLEUNC=0x3FFE
  ANGLECOM=0x3FFF

  def __init__(self):
    self.spi = spidev.SpiDev()
    
  def parity(self,data):
    parity=0
    for i in range(0,15):
      parity = parity + ((data>>i)&1)
    return parity % 2
    
  def cmdframe(self, addr, rw):
    frame = ((rw&1)<<14) | (addr&0x3FFF)
    # calculate even parity and put it in 15
    frame |= self.parity(frame) << 15
    
    return frame
    
  def send(self, frame):
    r = self.spi.xfer2([(frame>>8)&0xFF, frame&0xFF])
    
    return (r[1]) | (r[0]<<8)
    
  def read(self, addr):
    # generate command frame
    frame1 = self.cmdframe(addr,1)    
    frame2 = self.cmdframe(self.NOP,1)
    
    #print("frame1: "+str(frame1)+"\tframe2: "+str(frame2))
    
    self.send(frame1)
    r = self.send(frame2)
    
    if self.parity(r) != (r>>15):
      print("Parity error")
    if ((r>>14)&1)==1:
      print("Command Frame error")
    
    return r & 0x03FFF;
    
    
  def write(self,addr,data):
    # generate command frame
    return 0;

  def open(self, param):
    self.spi.open(0,param)
    self.spi.mode = 0b01
    print("AE_AS5047D: open("+str(param)+")")
    
    # selfcheck
    errfl = self.read(self.ERRFL);
    diaagcs = self.read(self.DIAAGC);
    
    if(errfl>0):
      print("AE_AS5047D: ERRFL set - this should not happen ("+errfl+")")
      return -1;
    if((diaagcs & 0x0100)>0):
      print("AE_AS5047D: Offset compensation not ready");
    if((diaagcs & 0x0200)>0):
      print("AE_AS5047D: Cordic overflow");
    if((diaagcs & 0x0400)>0):
      print("AE_AS5047D: Magnetic field strength high");
      return -1;
    if((diaagcs & 0x0800)>0):
      print("AE_AS5047D: Magnetic field strength low");
      return -1;  
    print("AE_AS5047D: AGC = "+str(diaagcs&0xFF));
    
    return 1;
      
  def readAngle(self):
    
    anglecom = self.read(self.ANGLECOM);
    #print(str(anglecom))
    
    return anglecom / 16384.0 * 360.0;

  def close(self):
    return 1;
  


