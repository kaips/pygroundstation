
import serial
import io

class gs232b(object):
    
    comport = ''
    serial = 0
    
    az_target = 0
    el_target = 0
    
    
    def open(self, comport):
        self.comport = comport
        self.serial = serial.Serial()
        self.serial.baudrate = 9600
        self.serial.port = self.comport
        
        self.serial.open()
        if(self.serial.isOpen()):
            print 'Serial Port open'
        else:
            print 'Opening serial port failed'
        
        buf = '';
        while 1:
            c = self.serial.read()
            buf = buf+c
            # received a CR - parse buffer
            if(ord(c)==13):
                print buf
                
                if(buf[0]=='W'):
                    print 'move'
                    self.az_target = int(buf[1:4])
                    self.el_target = int(buf[5:8])
                elif(buf[0]=='C' and buf[1]=='2'):
                    print 'status'
                    answer = "Az="+('%03d' % self.az_target)+" EL="+('%03d' % self.el_target)
                    print answer
                    
                    self.serial.write(answer)
                
                buf = ''
            
        
        
    def close(self):
        if(self.serial.isOpen()):
            self.serial.close()
            
       
        
        
        
        
        