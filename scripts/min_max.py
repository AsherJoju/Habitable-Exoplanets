from math import inf


class MinMax:
    
    def __init__(self):
        self.min = inf
        self.max = 0.0
    
    
    def add_value(self, value: float):
        if value > self.max:
            self.max = value
        if value < self.min:
            self.min = value
    
    
    def tuple(self):
        return (self.min, self.max)
