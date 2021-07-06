class House:
    def __init__(self, size, color='white'):
        self.size = size
        self.color = color

    def build_expansion(self, size):
        self.size += size


home = House(2000)