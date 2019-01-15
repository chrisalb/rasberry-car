
from TCPClient import TCPClient
from Command import COMMAND as cmd

from Freenove_Math import * 
import time
import threading
import math
#import copy


class DemoClass():
    tcp = TCPClient()
    default_Server_IP = "192.168.1.07"
    Camera_H_Pos = 90
    Camera_V_Pos = 90
    SERVO_MIN_ANGLE = 0
    SERVO_MAX_ANGLE = 180
    Is_Paint_Thread_On = False
    global t_Paint_Thread
    sonic_Index = 0
    sonic_buff = [0]*20
    send_Counter = 0
    Is_tcp_Idle = True
    def __init__(self, parent=None):
        self.Camera_V_Pos = self.Camera_V_Pos + 3
        self.Camera_V_Pos = constrain(self.Camera_V_Pos, 0, 90)
        self.tcp.connectToServer(address = (self.default_Server_IP, 12345))    
        self.tcp.sendData(cmd.CMD_CAMERA_UP + str(self.Camera_V_Pos))


if __name__ == "__main__":
    import sys
    
    dlg = DemoClass()