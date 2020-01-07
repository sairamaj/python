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
        print(f"Tower-{self.name}".rjust(30))

    def addDisc(self, disc):
        self.validateForAdd(disc)
        self.discs.append(disc)

    def drawPole(self):
        line = "|"
        n = 0
        while n < 4:
            print(line.rjust(25))
            n = n+1

    def removeTopDisc(self):
        return self.discs.pop()

    def getDiscCount(self):
        return len(self.discs)

    def validateForAdd(self, disc):
        if len(self.discs) == 0:
            return  # no disc means disc can be added

        topDisc = self.discs[-1]
        if topDisc.getSize() > disc.getSize():
            return # coming disc is smaller than top of the disc
        
        raise Exception(f"Disc {disc.getSize()} is not allowed on disc:{topDisc.getSize()}")