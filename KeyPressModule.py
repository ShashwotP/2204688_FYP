import pygame

def init():# init method to initialize pygame and set up window
    pygame.init()
    win = pygame.display.set_mode((100, 100))


def getKey(keyName):  # function getKey
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()  # retrieves current state of all keyboard keys
    myKey = getattr(pygame, 'K_{}'.format(
        keyName))  # constructs the name of desired key from keyname and retrieves corresponding key constant
    if keyInput[myKey]:  # checks desired key is pressed
        ans = True
        print('key a awas pressed')