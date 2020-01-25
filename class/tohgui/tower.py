import pygame

BASEWIDTH = 200
BASEHEIGHT = 20
POLEWIDTH = 20
POLEHEIGHT = 200


class Tower():
    def __init__(self, gameDisplay, refX, refY, color):
        self.gameDisplay = gameDisplay
        self.color = color
        self.refX = refX
        self.refY = refY
        self.discs = []

    def addDisc(self, disc):
        self.discs.append(disc)

    def draw(self):
        self.drawPole()
        discRefy = self.refY
        for disc in self.discs:
            disc.draw(self.gameDisplay, self.refX, discRefy)
            discRefy -= 12 # get disc height

    def drawPole(self):
        pygame.draw.rect(self.gameDisplay, self.color,
                         (self.refX-BASEWIDTH/2, self.refY, BASEWIDTH, BASEHEIGHT))
        pygame.draw.rect(self.gameDisplay, self.color, (self.refX -
                                                        POLEWIDTH/2, self.refY-POLEHEIGHT, POLEWIDTH, POLEHEIGHT))
