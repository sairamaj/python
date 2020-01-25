import pygame

DISCHEIGHT = 12


class Disc():
    def __init__(self, size, color):
        self.color = color
        self.size = size

    def draw(self, gameDisplay, refX, refY):
        pygame.draw.rect(gameDisplay, self.color,
                         (refX-self.size/2, refY-DISCHEIGHT, self.size, DISCHEIGHT))
