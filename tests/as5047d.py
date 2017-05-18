#!/usr/bin/python

import spidev
import time
from pprint import pprint

class as5047d(object):

  READ = 1
  WRITE = 0
  NOP = 	0x0000
  ERRFL = 	0x0001
  DIAAGC=	0x3FFC
  MAG = 	0x3FFD
  ANGLEUNC=0x3FFE
  ANGLECOM=0x3FFF

  def __init__(self, chipselect):
    self.spi = spidev.SpiDev()
    self.spi.open(0,chipselect)
    self.spi.mode = 0b01
    
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
    
    
    
c0 = as5047d(0);
c1 = as5047d(1);

for i in range(0,100):
  #print("ERRFL:  "+str(c0.read(c0.ERRFL)))
  #print("MAG:    "+str(c0.read(c0.MAG)))
  #print("DIAAGCS:"+str(c0.read(c0.DIAAGC)))
  #print("ANGLEUNC:"+str(c0.read(c0.ANGLEUNC)))

  print("ERRFL:  "+str(c1.read(c0.ERRFL)))
  print("MAG:    "+str(c1.read(c0.MAG)))
  print("DIAAGCS:"+str(c1.read(c0.DIAAGC)))
  print("ANGLEUNC:"+str(c1.read(c1.ANGLEUNC)))
  time.sleep(0.2)


