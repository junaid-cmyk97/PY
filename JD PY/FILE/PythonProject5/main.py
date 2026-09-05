class pet:
    def __init__(self, name,weight):
        self.name = name
        self.weight = 20

    def feed(self,w1):
        if w1 > self.weight:
            self.weight+1 = 20
