import thread
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
        
        # calibrate
        
        
        pass
    
    # run thread
    def run(self):
        # do everything here
        print "Thread Starting..."
        
        self.commandqueueLock.acquire()
        if not self.commandqueue.empty():
            data = self.commandqueue.get()
            self.commandqueueLock.release()
            print data
        else:
            self.commandqueueLock.release()
        
        pass
    
    
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
        pass
    def readPositionEl(self):
        pass
    
    # clean up
    def close(self):
        pass