import pygame
from time import sleep
pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()

buttons = {'x':0,'o':0,'s':0,'t':0,
