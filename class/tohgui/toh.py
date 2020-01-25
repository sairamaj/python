import pygame
import tower
import disc


class Toh():
    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay
        self.towers = [
            tower.Tower(gameDisplay, 150, 400, (255, 0, 0)),
            tower.Tower(gameDisplay, 400, 400, (0, 255, 0)),
            tower.Tower(gameDisplay, 650, 400, (0, 0, 255))]
        firstTower = self.towers[0]
        firstTower.addDisc(disc.Disc(150, (125, 125, 125)))
        firstTower.addDisc(disc.Disc(100, (125, 125, 0)))
        firstTower.addDisc(disc.Disc(50, (125, 0, 0)))

    def start(self):
        self.draw()

    def draw(self):
        for tower in self.towers:
            tower.draw()
