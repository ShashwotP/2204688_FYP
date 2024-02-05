from MotorModule import Motor

motor = Motor(2, 3, 4, 17, 22, 27)

import KeyPressModule as kp

kp.init()

def main():
    if kp.getKey('UP'):
        motor.move(0.6,0,0.1)




