import tower

class Toh():
    def __init__(self):
        print("in toh.init")
        self.towers = [tower.Tower("A"),tower.Tower("B"),tower.Tower("C")]
    
    def start(self):
        for tower in self.towers:
            tower.draw()
    
    
