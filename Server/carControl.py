from .mDev import *

def runner(**data):
    speed = data['speed']
    direction = data['direction']
    turning_angle = data['turning_angle']

    mdev.writeReg(mdev.CMD_SERVO1,int(turning_angle))
    mdev.writeReg(mdev.CMD_DIR1,int(direction))
    mdev.writeReg(mdev.CMD_DIR2,int(direction))
    mdev.writeReg(mdev.CMD_PWM1,int(speed))
    mdev.writeReg(mdev.CMD_PWM2,int(speed))        	        
    
    return speed
    
def camera(**data):
    for i in range(300, 1200, 2000):
        camera_left_right = i
        time.sleep(0.03)

    camera_up_down = data['camera_up_down']
    # mdev.writeReg(mdev.CMD_SERVO2,int(camera_left_right))
    mdev.writeReg(mdev.CMD_SERVO3,int(camera_up_down))
    return 'ok'
        
def forward():
    speed = 900
    mdev.writeReg(mdev.CMD_DIR1,0)
    mdev.writeReg(mdev.CMD_DIR2,0)
    mdev.writeReg(mdev.CMD_PWM1,speed)
    mdev.writeReg(mdev.CMD_PWM2,speed)        	        

def rightforward():
    speed = 900
    mdev.writeReg(mdev.CMD_SERVO1,300)
    mdev.writeReg(mdev.CMD_DIR1,0)
    mdev.writeReg(mdev.CMD_DIR2,0)
    mdev.writeReg(mdev.CMD_PWM1,speed)
    mdev.writeReg(mdev.CMD_PWM2,speed)
    	        

def leftforward():
    speed = 900
    mdev.writeReg(mdev.CMD_SERVO1,1800)
    mdev.writeReg(mdev.CMD_DIR1,0)
    mdev.writeReg(mdev.CMD_DIR2,0)
    mdev.writeReg(mdev.CMD_PWM1,speed)
    mdev.writeReg(mdev.CMD_PWM2,speed)
    	        

def backward():
    speed = 900
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
                    for i in range(0,900,10):
                        mdev.writeReg(mdev.CMD_PWM1,i)
                        mdev.writeReg(mdev.CMD_PWM2,i)
                    time.sleep(2)

                    mdev.writeReg(mdev.CMD_SERVO1,300)

                    mdev.writeReg(mdev.CMD_DIR1,1)
                    mdev.writeReg(mdev.CMD_DIR2,1)	

                    for i in range(0,900,10):	
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