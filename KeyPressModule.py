import pygame

def init():# init method to initialize pygame and set up window
    pygame.init()
    win = pygame.display.set_mode((100, 100))


def getKey(keyName):  # function getKey
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()  # retrieves current state of all keyboard keys
    myKey = getattr(pygame, 'K_{}'.format(
