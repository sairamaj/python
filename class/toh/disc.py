class Disc:
    def __init__(self, size, referenceX):
        self.size = size
        self.referenceX = referenceX

    def getSize(self):
        return self.size

    def draw(self):
        n = 0
        startPos = int(self.referenceX - (self.size/2))
        print(''.rjust(startPos),end='')
        while n<self.size:
            print('_', end='')
            n = n+1
        print()
