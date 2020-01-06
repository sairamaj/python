import tower
import disc

class Toh():
    def __init__(self):
        print("in toh.init")
        towerA = tower.Tower("A")
        towerA.addDisc(disc.Disc(24))
        towerA.addDisc(disc.Disc(18))
        towerA.addDisc(disc.Disc(12))
        self.towers = [towerA,tower.Tower("B"),tower.Tower("C")]

    def start(self):
        self.draw()
        
    
    def move(self, fromTower, toTower):
        topDisc = self.towers[0].removeTopDisc()
        self.towers[1].addDisc(topDisc)
        self.draw()

    def draw(self):
        for tower in self.towers:
            tower.draw()

    
    
