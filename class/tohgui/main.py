####################################
# minmimum game required.
####################################
import pygame
import toh
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

display_width =  800
display_height = 800

gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill(black)

toh = toh.Toh(gameDisplay)
toh.draw()
pygame.display.update()
time.sleep(4)
