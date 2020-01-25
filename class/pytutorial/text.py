import pygame
import time

black = (0,0,0)
red = (255, 0, 0)
pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Tower of Hanoi!!!")
clock = pygame.time.Clock()
display_width = 800
display_height = 600

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)

message_display('Hello world')