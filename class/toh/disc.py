class Disc:
    def __init__(self, size):
        self.size = size

    def draw(self):
        n = 0
        while n<self.size:
            print('_', end='')
            n = n+1
        print()
