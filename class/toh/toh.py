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
        realFrom = fromTower-1
        realTo  = toTower-1
        topDisc = self.towers[realFrom].removeTopDisc()
        self.towers[realTo].addDisc(topDisc)
        self.draw()

    def draw(self):
        for tower in self.towers:
            tower.draw()
    
    def isGameOver(self):
        # check whether any tower other than first one has 3 discs
        for tower in self.towers[1:]:
            if tower.getDiscCount() == 3:
                return True
        return False


    
    
