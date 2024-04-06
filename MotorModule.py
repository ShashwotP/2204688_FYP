
#works
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)# configure GPIO pin mode to BCM
GPIO.setwarnings(False)# suppress warnings related to GPIOs

#define motor class
class Motor():
    def __init__(self, EnaA, In1A, In2A, EnaB, In1B, In2B):# constructor method to initialize motor object
        #GPIO pin numbers to control motors, assign pins to instance variables later
        self.EnaA = EnaA#2
        self.In1A = In1A#3
        self.In2A = In2A#4
        self.EnaB = EnaB#17
        self.In1B = In1B#22
        self.In2B = In2B#27
        GPIO.setup(self.EnaA, GPIO.OUT)#configure GPIO pins as outputs
        GPIO.setup(self.In1A, GPIO.OUT)
        GPIO.setup(self.In2A, GPIO.OUT)
        GPIO.setup(self.EnaB, GPIO.OUT)
        GPIO.setup(self.In1B, GPIO.OUT)
        GPIO.setup(self.In2B, GPIO.OUT)
        self.pwmA = GPIO.PWM(self.EnaA, 100);#set up pwm for controlling motor speed
        self.pwmA.start(0);# start duty cycle at 0
        self.pwmB = GPIO.PWM(self.EnaB, 100);
        self.pwmB.start(0);

    def move(self, speed=0.5, turn=0, t=0):#method move to control movement of motors
        speed *=100#scale speed value
        turn *=100
        leftSpeed = speed - turn#calculate speed for left and right motors
        rightSpeed = speed + turn

        if leftSpeed >100: leftSpeed=100#limit speed range from -100 to 100
        elif leftSpeed <-100: leftSpeed= -100
        if rightSpeed >100: rightSpeed=100
        elif rightSpeed <-100: rightSpeed= -100


        self.pwmA.ChangeDutyCycle(abs(leftSpeed))#set duty cycle of pwm signals for controlling motor speed
        self.pwmB.ChangeDutyCycle(abs(rightSpeed))

        if leftSpeed > 0:#sets direction of left motor
            GPIO.output(self.In1A, GPIO.HIGH)
            GPIO.output(self.In2A, GPIO.LOW)
        else:
            GPIO.output(self.In1A, GPIO.LOW)
            GPIO.output(self.In2A, GPIO.HIGH)

        if rightSpeed > 0:#sets the direction of right motor
            GPIO.output(self.In1B, GPIO.HIGH)
            GPIO.output(self.In2B, GPIO.LOW)
        else:
            GPIO.output(self.In1B, GPIO.LOW)
            GPIO.output(self.In2B, GPIO.HIGH)
        sleep(t)#pause motors

    def stop(self, t=0):#method stop to stop the motors
        self.pwmA.ChangeDutyCycle(0);
        self.pwmB.ChangeDutyCycle(0);
        sleep(t)

#creates instance of motor class motor1 with GPIO pins 2,3,4,17,22,27
motor1 = Motor(2, 3, 4, 17, 22, 27)

motor1.move(0.3,0, 2)#back
motor1.stop(1)
motor1.move(-0.3,0, 2)#forward
motor1.stop(1)
#motor1.move(-0.5,0.2, 2)#left
#motor1.stop(1)
motor1.move(0.5,0.2, 2)#right
motor1.stop(1)

#
#
# import RPi.GPIO as GPIO
# from time import sleep
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
#
# class Motor():
#     def __init__(self, EnaA, In1A, In2A, EnaB, In1B, In2B):
#         self.EnaA = EnaA
#         self.In1A = In1A
#         self.In2A = In2A
#         self.EnaB = EnaB
#         self.In1B = In1B
#         self.In2B = In2B
#         GPIO.setup(self.EnaA, GPIO.OUT)
#         GPIO.setup(self.In1A, GPIO.OUT)
#         GPIO.setup(self.In2A, GPIO.OUT)
#         GPIO.setup(self.EnaB, GPIO.OUT)
#         GPIO.setup(self.In1B, GPIO.OUT)
#         GPIO.setup(self.In2B, GPIO.OUT)
#         self.pwmA = GPIO.PWM(self.EnaA, 100);
#         self.pwmA.start(0);
#         self.pwmB = GPIO.PWM(self.EnaB, 100);
#         self.pwmB.start(0);
#
#     def moveF(self, speed=50, t=0):
#         self.pwmA.ChangeDutyCycle(speed)
#         GPIO.output(self.In1A, GPIO.LOW)
#         GPIO.output(self.In2A, GPIO.HIGH)
#         self.pwmB.ChangeDutyCycle(speed)
#         GPIO.output(self.In1B, GPIO.LOW)
#         GPIO.output(self.In2B, GPIO.HIGH)
#         sleep(t)
#
#
#     def stop(self, t=0):
#         self.pwmA.ChangeDutyCycle(0);
#         self.pwmB.ChangeDutyCycle(0);
#         sleep(t)
#
# motor1 = Motor(2, 3, 4, 17, 22, 27)
#
#
# motor1.moveF(30, 2)
# motor1.stop(1)
# motor1.moveF(-30,2)
# motor1.stop(1)
#
#
#
# import RPi.GPIO as GPIO
# from time import sleep
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
#
# class Motor():
#     def __init__(self,EnaA,In1A,In2A,EnaB,In1B,In2B):
#         self.EnaA = EnaA
#         self.In1A = In1A
#         self.In2A = In2A
#         self.EnaB = EnaB
#         self.In1B = In1B
#         self.In2B = In2B
#         GPIO.setup(self.EnaA, GPIO.OUT)
#         GPIO.setup(self.In1A, GPIO.OUT)
#         GPIO.setup(self.In2A, GPIO.OUT)
#         GPIO.setup(self.EnaB, GPIO.OUT)
#         GPIO.setup(self.In1B, GPIO.OUT)
#         GPIO.setup(self.In2B, GPIO.OUT)
#         self.pwmA = GPIO.PWM(self.EnaA, 100);
#         self.pwmA.start(0);
#         self.pwmB = GPIO.PWM(self.EnaB, 100);
#         self.pwmB.start(0);
#
#     def move(self, speed=0.5, turn=0, t=0):
#         speed *= 100
#         turn *= 100
#         leftSpeed = speed - turn
#         rightSpeed = speed + turn
#         if leftSpeed > 100:
#             leftSpeed = 100
#         elif leftSpeed < -100:
#             leftSpeed = -100
#         if rightSpeed > 100:
#             rightSpeed = 100
#         elif rightSpeed < -100:
#             rightSpeed = -100
#
#         self.pwmA.ChangeDutyCycle(abs(leftSpeed))
#         self.pwmB.ChangeDutyCycle(abs(rightSpeed))
#
#         if leftSpeed > 0:
#             GPIO.output(self.In1A, GPIO.HIGH)
#             GPIO.output(self.In2A, GPIO.LOW)
#         else:
#             GPIO.output(self.In1A, GPIO.LOW)
#             GPIO.output(self.In2A, GPIO.HIGH)
#
#         if rightSpeed > 0:
#             GPIO.output(self.In1B, GPIO.HIGH)
#             GPIO.output(self.In2B, GPIO.LOW)
#         else:
#             GPIO.output(self.In1B, GPIO.LOW)
#             GPIO.output(self.In2B, GPIO.HIGH)
#
#         sleep(t)
#
#     def stop(self, t=0):
#         self.pwmA.ChangeDutyCycle(0);
#         self.pwmB.ChangeDutyCycle(0);
#         sleep(t)

    # def main():
    #     motor.move(0.6, 0, 2)
    #     motor.stop(2)
    #     motor.move(-0.5, 0.2, 2)
    #     motor.stop(2)









# import RPi.GPIO as GPIO
# from time import sleep
#
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
#
#
# class Motor():
#     def __init__(self, EnaA, In1A, In2A, EnaB, In1B, In2B):
#         self.EnaA = EnaA
#         self.In1A = In1A
#         self.In2A = In2A
#         self.EnaB = EnaB
#         self.In1B = In1B
#         self.In2B = In2B
#         GPIO.setup(self.EnaA, GPIO.OUT)
#         GPIO.setup(self.In1A, GPIO.OUT)
#         GPIO.setup(self.In2A, GPIO.OUT)
#         GPIO.setup(self.EnaB, GPIO.OUT)
#         GPIO.setup(self.In1B, GPIO.OUT)
#         GPIO.setup(self.In2B, GPIO.OUT)
#         self.pwmA = GPIO.PWM(self.EnaA, 100);
#         self.pwmA.start(0);
#         self.pwmB = GPIO.PWM(self.EnaB, 100);
#         self.pwmB.start(0);
#
#     def move(self, speed=0.5, turn=0, t=0):
#         speed *=100
#         turn *=100
#         leftSpeed = speed - turn
#         rightSpeed = speed + turn
#
#         if leftSpeed >100: leftSpeed=100
#         elif leftSpeed <-100: leftSpeed= -100
#         if rightSpeed >100: rightSpeed=100
#         elif rightSpeed <-100: rightSpeed= -100
#
#
#         self.pwmA.ChangeDutyCycle(abs(leftSpeed))
#         self.pwmB.ChangeDutyCycle(abs(rightSpeed))
#
#         if leftSpeed > 0:
#             GPIO.output(self.In1A, GPIO.HIGH)
#             GPIO.output(self.In2A, GPIO.LOW)
#         else:
#             GPIO.output(self.In1A, GPIO.LOW)
#             GPIO.output(self.In2A, GPIO.HIGH)
#
#         if rightSpeed > 0:
#             GPIO.output(self.In1B, GPIO.HIGH)
#             GPIO.output(self.In2B, GPIO.LOW)
#         else:
#             GPIO.output(self.In1B, GPIO.LOW)
#             GPIO.output(self.In2B, GPIO.HIGH)
#         sleep(t)
#
#     def stop(self, t=0):
#         self.pwmA.ChangeDutyCycle(0);
#         self.pwmB.ChangeDutyCycle(0);
#         sleep(t)
#
#
# motor1 = Motor(2, 3, 4, 17, 22, 27)
#
# motor1.move(0.6,0, 2)
# motor1.stop(1)







