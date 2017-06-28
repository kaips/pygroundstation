import threading
import time
import Queue


class rotorcontrol(threading.Thread):
    
    running = 0;
    
    commandqueue = Queue.Queue(10)
    commandqueueLock = threading.Lock()
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.threadId = 1
        self.name = 'rotorcontrol'
    
    def open(self, motor_az, motor_el, encoder_az, encoder_el):
        
        self.encoder_az = encoder_az
        self.encoder_el = encoder_el
        self.motor_az = motor_az
        self.motor_el = motor_el
        
        # calibrate
        
        # TODO do later. assume encoders are pre-calibrated
        
        # get rotor specific min/max values
        self.az_min = 1
        self.az_max = 360
        self.el_min = 0
        self.el_min = 100
        
        
        pass
    
    # run thread
    def run(self):
        # do everything here
        print "Thread Starting..."
        
        while(self.running):
        
            self.commandqueueLock.acquire()
            if not self.commandqueue.empty():
                data = self.commandqueue.get()
                self.commandqueueLock.release()
                print data
                
                # move towards to rotation
                current_az = self.encoder_az.readAngle()
                current_el = self.encoder_el.readAngle()
                dest_az = data[0]
                dest_el = data[1]
                
                if( not (self.az_min < dest_az < self.az_max) ):
                    # move az
                    #TODO
                    
                if( not (self.el_min < dest_el < self.el_max) ):
                    # move el
                    #TODO
                
            else:
                self.commandqueueLock.release()
        
    
    
    # non blocking - add to execution queue
    def commandMove(self, dest_az, dest_el):
        if(running==1):
            # add to queue
            self.commandqueueLock.acquire()
            self.commandqueue.put([dest_az, dest_el])
            self.commandqueueLock.release()
        
            pass
    
    # read position now 
    def readPositionAz(self):
        return self.encoder_az.readAngle()
    def readPositionEl(self):
        return self.encoder_el.readAngle()
    
    # clean up
    def close(self):
        pass