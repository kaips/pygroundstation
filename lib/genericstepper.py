
import RPi.GPIO as GPIO
import time

class genericstepper(steppercontrol):
    
    SEN = 0
    SPUL = 0
    SDIR = 0
    
    direction = self.CW
    
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
        
        print("genericstepper: opened")
        
    def close(self):
        GPIO.cleanup()
        
    def stopAll(self):
        
        
    def disable(self):
        GPIO.output(self.SEN, 1)
        
        
    def move(self, direction, angle):

        return self.move(direction, angle, 1)
        
    
    # direction: CW/CCW
    # angle: absolute angle to be moved
    # angularspeed: in angle/sec
        
    def move(self, direction, angle, angularspeed):
        GPIO.output(self.SEN, 0)                # activate 
        
        steps = round(angle * self.gearratio * self.microsteps / self.stepperstepangle)
        
        totalduration = angle / angularspeed
        
        # TODO calculate ramps for the steppers
        
        
        print("genericstepper: moving("+str(direction)", "+str(angle)+", "+str(angularspeed)") = "+str(steps)+" steps")
        
        GPIO.output(self.SDIR,direction);       # set direction
        
        for x in range(0,steps):
            GPIO.output(self.SPUL,1)
            GPIO.output(self.SPUL,0)
            time.sleep(0.002)
        
        
        
        
        