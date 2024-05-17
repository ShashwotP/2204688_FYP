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
    pygame.display.update()  # updates display and returns ans which indicates whether desired key was pressed or not
    return ans

def main():
    if getKey('a'):
        print('Key a was pressed')
    if getKey('b'):
        print('Key b was pressed')
    if getKey('LEFT'):
        print('Key left was pressed')
    if getKey('RIGHT'):
        print('Key right was pressed')





