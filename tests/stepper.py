#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import signal
import sys

pulseforward=2000;
pulsereverse=2000;

if len(sys.argv)==3:
	pulseforward = int(sys.argv[1]);
	pulsereverse = int(sys.argv[2]);

print("Pulseforward : "+str(pulseforward)+" Pulsebackward:"+str(pulsereverse))	

def signal_handler(signal,frame):
	print('ctrl-c')
	GPIO.cleanup()
	sys.exit(0)
	
signal.signal(signal.SIGINT,signal_handler)

GPIO.setmode(GPIO.BCM)

S1EN=13
S1PUL=6
S1DIR=26

S2EN=22
S2PUL=27
S2DIR=17

GPIO.setup(S1EN,GPIO.OUT)
GPIO.setup(S1PUL,GPIO.OUT)
GPIO.setup(S1DIR,GPIO.OUT)
GPIO.setup(S2EN,GPIO.OUT)
GPIO.setup(S2PUL,GPIO.OUT)
GPIO.setup(S2DIR,GPIO.OUT)


print('stepping')

GPIO.output(S1DIR,0)
GPIO.output(S2DIR,0)

for x in range(0,pulseforward):
	GPIO.output(S1PUL,1)
	GPIO.output(S1PUL,0)
	GPIO.output(S2PUL,1)
	GPIO.output(S2PUL,0)	
	time.sleep(0.002)
GPIO.output(S1DIR,1)

GPIO.output(S2DIR,1)
for x in range(0,pulsereverse):
	GPIO.output(S1PUL,1)
	GPIO.output(S1PUL,0)
	GPIO.output(S2PUL,1)
	GPIO.output(S2PUL,0)
	time.sleep(0.003)

	

GPIO.output(S1EN,0 )
GPIO.output(S2EN,0 )

GPIO.cleanup()

	
