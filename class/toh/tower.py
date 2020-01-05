class Tower():
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "Tower"

    def draw(self):
        line = "|"
        n = 0
        while n<4:
            print(line.rjust(5))
            n = n+1
        print(f"Tower-{self.name}")
    
