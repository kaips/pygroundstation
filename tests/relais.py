#!/usr/bin/env python

import sys
import serial
from sv3common import sv3

import pprint;
import time;

deviceAddr='f'

def main():
  sp=serial.Serial("/dev/ttyAMA0", 9600, timeout=0.05, stopbits=1, parity='N')

  g1 = (sv3(sp,deviceAddr+"g1\r"))
  g2 = (sv3(sp,deviceAddr+"g2\r"))
  g3 = (sv3(sp,deviceAddr+"g3\r"))
  
  print "outputs:"
  pprint.pprint(g1);
  pprint.pprint(g2);
  pprint.pprint(g3);
  
  #sv3(sp,deviceAddr+"a0,0\r")
  #sv3(sp,deviceAddr+"a1,0\r")
  #sv3(sp,deviceAddr+"b1,0\r") 
  #sv3(sp,deviceAddr+"a0,0\r")
  #sv3(sp,deviceAddr+"b0,0\r")
    
  #sv3(sp,deviceAddr+"a0,0\r")

  sp.close()
  
if __name__ == "__main__":
  main()