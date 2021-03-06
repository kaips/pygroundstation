
from steppercontrol import steppercontrol
import RPi.GPIO as GPIO
import time
import threading

class genericstepper(steppercontrol):
    
    SEN = 0
    SPUL = 0
    SDIR = 0
    
    direction = steppercontrol.CW
    
    stepperstepangle = 0
    microsteps = 0
    gearratio = 0
    
    
    def open(self, sen, spul, sdir, stepperstepangle, microsteps, gearratio):
        
        self.SEN = sen
        self.SPUL = spul
        self.SDIR = sdir
        
        self.stepperstepangle = stepperstepangle
        self.microsteps = microsteps
        self.gearratio = gearratio
        
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(self.SEN,GPIO.OUT)
        GPIO.setup(self.SPUL,GPIO.OUT)
        GPIO.setup(self.SDIR,GPIO.OUT)
        
        GPIO.output(self.SDIR,self.direction)
        GPIO.output(self.SEN, 0)
        
        self.lock = threading.Lock()
        
        print("genericstepper: opened")
        
    def close(self):
        GPIO.cleanup()
        
    def stopAll(self):
        pass
        
        
    def disable(self):
        GPIO.output(self.SEN, 1)
        
        
    def move(self, direction, angle):
        return self.moveAngular(direction, angle, 4.0)
        
    def moveDuration(self, direction, angle, duration):
        return self.moveAngular(direction, angle, angle/duration)
    
    # direction: CW/CCW
    # angle: absolute angle to be moved
    # angularspeed: in angle/sec
        
    def moveAngular(self, direction, angle, angularspeed):
        
        self.lock.acquire()
        
        GPIO.output(self.SEN, 0)                # activate 
        
        steps = int(angle * self.gearratio * self.microsteps / self.stepperstepangle)
        
        totalduration = angle / float(angularspeed)
        
        # TODO calculate ramps for the steppers
        step_t = totalduration/steps;
        
        print("genericstepper: moving("+str(direction)+", "+str(angle)+", "+str(angularspeed)+") = "+str(steps)+" steps at "+str(step_t))
        
        GPIO.output(self.SDIR,direction);       # set direction
        
        for x in range(0,steps):
            GPIO.output(self.SPUL,1)
            GPIO.output(self.SPUL,0)
            time.sleep(step_t)
        
        self.lock.release()
        
        
        