import pygame
from time import sleep
pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()

buttons = {'x':0,'o':0,'s':0,'t':0,
            'share':0,'R1':0,'options':0,'R2':0,
            'L2':0,'L1':0,
           'axis1':0.,'axis2':0.,'axis3':0.,'axis4':0.}
axiss=[0.,0.,0.,0.,0.,0.]
def getJS(name=''):
    global buttons
    # retrieve any events ...
    for event in pygame.event.get():  # Analog Sticks




