from mDev import *


class selfDrive:
    status = 1
    turn_left = False
    turn_right = False

    def checkDistance(self):
        SonicEchoTime = mdev.readReg(mdev.CMD_SONIC)
        distance = SonicEchoTime * 17.0 / 1000.0
       # print distance
        if (int(distance) < 35):
            mdev.writeReg(mdev.CMD_IO2, 1)
            mdev.writeReg(mdev.CMD_IO3, 1)
            mdev.writeReg(mdev.CMD_SERVO1, 1500)
            mdev.writeReg(mdev.CMD_PWM1, 0)
            mdev.writeReg(mdev.CMD_PWM2, 0)
            mdev.writeReg(mdev.CMD_BUZZER,250)
            time.sleep(0.4)
            mdev.writeReg(mdev.CMD_BUZZER,0)
            mdev.writeReg(mdev.CMD_IO1, 0)
            mdev.writeReg(mdev.CMD_IO2, 1)
            mdev.writeReg(mdev.CMD_IO3, 1)
            time.sleep(0.5)
            mdev.writeReg(mdev.CMD_IO1, 1)
            mdev.writeReg(mdev.CMD_IO2, 1)
            mdev.writeReg(mdev.CMD_IO3, 1)
            self.status = 2
            return False

    def backward(self):
        speed = 600
        mdev.writeReg(mdev.CMD_DIR1, 1)
        mdev.writeReg(mdev.CMD_DIR2, 1)
        mdev.writeReg(mdev.CMD_SERVO1, 1460)
        mdev.writeReg(mdev.CMD_PWM1, speed)
        mdev.writeReg(mdev.CMD_PWM2, speed)

    def stop(self):
        mdev.writeReg(mdev.CMD_IO1, 1)
        mdev.writeReg(mdev.CMD_IO2, 1)
        mdev.writeReg(mdev.CMD_IO3, 1)
        mdev.writeReg(mdev.CMD_SERVO1, 1480)
        mdev.writeReg(mdev.CMD_PWM1, 0)
        mdev.writeReg(mdev.CMD_PWM2, 0)
        mdev.writeReg(mdev.CMD_BUZZER, 0)

    def forward(self):
        speed = 450
        mdev.writeReg(mdev.CMD_DIR1, 0)
        mdev.writeReg(mdev.CMD_DIR2, 0)
        mdev.writeReg(mdev.CMD_PWM1, speed)
        mdev.writeReg(mdev.CMD_PWM2, speed)
        mdev.writeReg(mdev.CMD_SERVO1, 1480)
        mdev.writeReg(mdev.CMD_SERVO2, 1500)
        mdev.writeReg(mdev.CMD_SERVO3, 1500)

    def rightforward(self):
        speed = 450
        mdev.writeReg(mdev.CMD_SERVO1, 1200)
        mdev.writeReg(mdev.CMD_DIR1, 0)
        mdev.writeReg(mdev.CMD_DIR2, 0)
        mdev.writeReg(mdev.CMD_PWM1, speed)
        mdev.writeReg(mdev.CMD_PWM2, speed)

    def leftforward(self):
        speed = 600
        mdev.writeReg(mdev.CMD_SERVO1, 2300)
        mdev.writeReg(mdev.CMD_DIR1, 0)
        mdev.writeReg(mdev.CMD_DIR2, 0)
        mdev.writeReg(mdev.CMD_PWM1, speed)
        mdev.writeReg(mdev.CMD_PWM2, speed)

    def drive(self):
        try:
            while True:
                self.checkDistance()
            # print selfdrive.status
                if (self.status == 2):
                    self.backward()
                    time.sleep(2)
                    self.rightforward()
                    time.sleep(1.4)
                    self.turn_right = False
                    self.turn_left = True

                    self.status = 1

                else:
                    self.forward()

        except KeyboardInterrupt:
            self.stop()
        pass


selfdrive = selfDrive()
selfdrive.drive()
