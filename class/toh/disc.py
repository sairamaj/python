class Disc:
    def __init__(self, size):
        self.size = size

    def getSize(self):
        return self.size

    def draw(self):
        n = 0
        print(''.rjust(20),end='')
        while n<self.size:
            print('_', end='')
            n = n+1
        print()
