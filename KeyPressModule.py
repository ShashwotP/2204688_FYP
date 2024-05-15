import pygame

def init():# init method to initialize pygame and set up window
    pygame.init()
    win = pygame.display.set_mode((100, 100))


def getKey(keyName):  # function getKey
    ans = False
    for eve in pygame.event.get(): pass
