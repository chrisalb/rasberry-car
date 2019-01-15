from .mDev import *

def forward():
    speed = 400
    mdev.writeReg(mdev.CMD_DIR1,0)
    mdev.writeReg(mdev.CMD_DIR2,0)
    mdev.writeReg(mdev.CMD_PWM1,speed)
    mdev.writeReg(mdev.CMD_PWM2,speed)        	        

def rightforward():
    speed = 400
    mdev.writeReg(mdev.CMD_SERVO1,300)
    mdev.writeReg(mdev.CMD_DIR1,0)
    mdev.writeReg(mdev.CMD_DIR2,0)
    mdev.writeReg(mdev.CMD_PWM1,speed)
    mdev.writeReg(mdev.CMD_PWM2,speed)
    	        

def leftforward():
    speed = 400
    mdev.writeReg(mdev.CMD_SERVO1,1800)
    mdev.writeReg(mdev.CMD_DIR1,0)
    mdev.writeReg(mdev.CMD_DIR2,0)
    mdev.writeReg(mdev.CMD_PWM1,speed)
    mdev.writeReg(mdev.CMD_PWM2,speed)
    	        

def backward():
    speed = 400
    mdev.writeReg(mdev.CMD_DIR1,1)
    mdev.writeReg(mdev.CMD_DIR2,1)
    mdev.writeReg(mdev.CMD_PWM1,speed)
    mdev.writeReg(mdev.CMD_PWM2,speed)     

def stop():
        mdev.writeReg(mdev.CMD_IO1,1)
        mdev.writeReg(mdev.CMD_IO2,1)
        mdev.writeReg(mdev.CMD_IO3,1)
        mdev.writeReg(mdev.CMD_SERVO1,1500)
        mdev.writeReg(mdev.CMD_PWM1,0)
        mdev.writeReg(mdev.CMD_PWM2, 0)    

def drive(self):
    try:		
            mdev.writeReg(mdev.CMD_DIR1,0)
            mdev.writeReg(mdev.CMD_DIR2,0)	

            for i in range(0,3):
                mdev.writeReg(mdev.CMD_IO1,0)
                mdev.writeReg(mdev.CMD_IO2,1)
                mdev.writeReg(mdev.CMD_IO3,1)
                
                mdev.writeReg(mdev.CMD_IO1,1)
                mdev.writeReg(mdev.CMD_IO2,0)
                mdev.writeReg(mdev.CMD_IO3,1)
                
                mdev.writeReg(mdev.CMD_IO1,1)
                mdev.writeReg(mdev.CMD_IO2,1)
                mdev.writeReg(mdev.CMD_IO3,0)
            

                while True:
                    for i in range(0,400,10):	
                        mdev.writeReg(mdev.CMD_PWM1,i)
                        mdev.writeReg(mdev.CMD_PWM2,i)
                    time.sleep(2)

                    mdev.writeReg(mdev.CMD_SERVO1,300)

                    mdev.writeReg(mdev.CMD_DIR1,1)
                    mdev.writeReg(mdev.CMD_DIR2,1)	

                    for i in range(0,400,10):	
                        mdev.writeReg(mdev.CMD_PWM1,i)
                        mdev.writeReg(mdev.CMD_PWM2,i)
                        
                    time.sleep(2)
                        
                    mdev.writeReg(mdev.CMD_SERVO1,1500)
                    mdev.writeReg(mdev.CMD_PWM1,0)
                    mdev.writeReg(mdev.CMD_PWM2,0)

                    mdev.writeReg(mdev.CMD_DIR1,0)
                    mdev.writeReg(mdev.CMD_DIR2,0)	
                    
    except KeyboardInterrupt:
        mdev.writeReg(mdev.CMD_IO1,1)
        mdev.writeReg(mdev.CMD_IO2,1)
        mdev.writeReg(mdev.CMD_IO3,1)
        mdev.writeReg(mdev.CMD_SERVO1,1500)
        mdev.writeReg(mdev.CMD_PWM1,0)
        mdev.writeReg(mdev.CMD_PWM2, 0)
    pass
def blink():
    for i in range(0,3):
        mdev.writeReg(mdev.CMD_IO1,0)
        mdev.writeReg(mdev.CMD_IO2,1)
        mdev.writeReg(mdev.CMD_IO3,1)
        time.sleep(0.3)
        mdev.writeReg(mdev.CMD_IO1,1)
        mdev.writeReg(mdev.CMD_IO2,0)
        mdev.writeReg(mdev.CMD_IO3,1)
        time.sleep(0.3)
        mdev.writeReg(mdev.CMD_IO1,1)
        mdev.writeReg(mdev.CMD_IO2,1)
        mdev.writeReg(mdev.CMD_IO3,0)
        time.sleep(0.3)
        mdev.writeReg(mdev.CMD_IO1,1)
        mdev.writeReg(mdev.CMD_IO2,1)
        mdev.writeReg(mdev.CMD_IO3,1)