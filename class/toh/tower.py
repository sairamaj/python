import disc

class Tower():
    def __init__(self, name):
        self.name = name
        self.discs = []
    
    def __str__(self):
        return "Tower"

    def draw(self):
        self.drawPole()
        for disc in self.discs[::-1]:
            disc.draw()
        print(f"Tower-{self.name}")
    
    def addDisc(self,disc):
        self.discs.append(disc)

    def drawPole(self):
        line = "|"
        n = 0
        while n<4:
            print(line.rjust(5))
            n = n+1

    def removeTopDisc(self):
        return self.discs.pop()

    def getDiscCount(self):
        return len(self.discs)
    
