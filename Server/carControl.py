import threading
from .mDev import *


def runner(**data):
    speed = data['speed']
    direction = data['direction']
    turning_angle = data['turning_angle']

    mdev.writeReg(mdev.CMD_SERVO1, int(turning_angle))
    mdev.writeReg(mdev.CMD_DIR1, int(direction))
    mdev.writeReg(mdev.CMD_DIR2, int(direction))
    mdev.writeReg(mdev.CMD_PWM1, int(speed))
    mdev.writeReg(mdev.CMD_PWM2, int(speed))

    return ''


def camera(**data):
    
    if 'camera_up' in data:
        for x in range(1500, 3000, 2):
            if x == 3000:
                break
            mdev.writeReg(mdev.CMD_SERVO3, x)

    if 'camera_down' in data:
        for x in range(3000, 400, -20):
            if x == 1300:
                break
            mdev.writeReg(mdev.CMD_SERVO3, x)
            time.sleep(0.3)

    if 'camera_left' in data:
        for x in range(0, 3000, 20):
            if x == 3000:
                break
            mdev.writeReg(mdev.CMD_SERVO2, x)
            time.sleep(0.3)

    if 'camera_right' in data:
        for x in range(3000, 0, -20):
            if x == 0:
                break
            mdev.writeReg(mdev.CMD_SERVO2, x)
            time.sleep(0.3)

    stop()


# mdev.writeReg(mdev.CMD_SERVO2, int(camera_left_right)) < 700 höger  - 2000 rakt fram - 3000 till vänster
# mdev.writeReg(mdev.CMD_SERVO3, int(camera_up_down)) < 1500 rakt fram - 3000 rakt upp - 1300 längst ned
    return 'ok'


def checkdistance():
    while True:
        SonicEchoTime = mdev.readReg(mdev.CMD_SONIC)
        distance = SonicEchoTime * 17.0 / 1000.0
        if (int(distance) < 40 and int(distance) > 0):
            stop()
            buzz()
            mdev.writeReg(mdev.CMD_IO1, 0)
            mdev.writeReg(mdev.CMD_IO2, 1)
            mdev.writeReg(mdev.CMD_IO3, 1)
            time.sleep(1)
            mdev.writeReg(mdev.CMD_IO1, 1)
            mdev.writeReg(mdev.CMD_IO2, 1)
            mdev.writeReg(mdev.CMD_IO3, 1)

def forward():
    speed = 1100
    mdev.writeReg(mdev.CMD_DIR1, 0)
    mdev.writeReg(mdev.CMD_DIR2, 0)
    mdev.writeReg(mdev.CMD_PWM1, speed)
    mdev.writeReg(mdev.CMD_PWM2, speed)
    mdev.writeReg(mdev.CMD_SERVO1, 1480)
    mdev.writeReg(mdev.CMD_SERVO2, 1500)
    mdev.writeReg(mdev.CMD_SERVO3, 1500)

    return ''


def rightforward():
    speed = 1000
    mdev.writeReg(mdev.CMD_SERVO1, 1150)
    mdev.writeReg(mdev.CMD_DIR1, 0)
    mdev.writeReg(mdev.CMD_DIR2, 0)
    mdev.writeReg(mdev.CMD_PWM1, speed)
    mdev.writeReg(mdev.CMD_PWM2, speed)
    SonicEchoTime = mdev.readReg(mdev.CMD_SONIC)
    distance = SonicEchoTime * 17.0 / 1000.0

    return ''


def leftforward():
    speed = 1000
    mdev.writeReg(mdev.CMD_SERVO1, 1950)
    mdev.writeReg(mdev.CMD_DIR1, 0)
    mdev.writeReg(mdev.CMD_DIR2, 0)
    mdev.writeReg(mdev.CMD_PWM1, speed)
    mdev.writeReg(mdev.CMD_PWM2, speed)
    SonicEchoTime = mdev.readReg(mdev.CMD_SONIC)
    distance = SonicEchoTime * 17.0 / 1000.0

    return ''


def backward():
    speed = 1000
    mdev.writeReg(mdev.CMD_DIR1, 1)
    mdev.writeReg(mdev.CMD_DIR2, 1)
    mdev.writeReg(mdev.CMD_SERVO1, 1460)
    mdev.writeReg(mdev.CMD_PWM1, speed)
    mdev.writeReg(mdev.CMD_PWM2, speed)


def stop():
    mdev.writeReg(mdev.CMD_IO1, 1)
    mdev.writeReg(mdev.CMD_IO2, 1)
    mdev.writeReg(mdev.CMD_IO3, 1)
    mdev.writeReg(mdev.CMD_SERVO1, 1480)
    mdev.writeReg(mdev.CMD_SERVO2, 2000)
    mdev.writeReg(mdev.CMD_SERVO3, 1500)
    mdev.writeReg(mdev.CMD_PWM1, 0)
    mdev.writeReg(mdev.CMD_PWM2, 0)
    mdev.writeReg(mdev.CMD_BUZZER, 0)

    return ''


def buzz():
    mdev.writeReg(mdev.CMD_BUZZER, 250)


def blink():
    for i in range(0, 3):
        mdev.writeReg(mdev.CMD_IO1, 0)
        mdev.writeReg(mdev.CMD_IO2, 1)
        mdev.writeReg(mdev.CMD_IO3, 1)
        time.sleep(0.3)
        mdev.writeReg(mdev.CMD_IO1, 1)
        mdev.writeReg(mdev.CMD_IO2, 0)
        mdev.writeReg(mdev.CMD_IO3, 1)
        time.sleep(0.3)
        mdev.writeReg(mdev.CMD_IO1, 1)
        mdev.writeReg(mdev.CMD_IO2, 1)
        mdev.writeReg(mdev.CMD_IO3, 0)
        time.sleep(0.3)
        mdev.writeReg(mdev.CMD_IO1, 1)
        mdev.writeReg(mdev.CMD_IO2, 1)
        mdev.writeReg(mdev.CMD_IO3, 1)


""" 
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



mdev.writeReg(mdev.CMD_SERVO2, int(camera_left_right)) < 700 höger  - 2000 rakt fram - 3000 till vänster
mdev.writeReg(mdev.CMD_SERVO3, int(camera_up_down)) < 1500 rakt fram - 3000 rakt upp - 1300 längst ned

"""
