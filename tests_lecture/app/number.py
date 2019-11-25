from random import randrange

class Number:

    lower_bound = 0
    upper_bound = 100

    def __init__(self, value=0):
        self.value = value
    
    @classmethod
    def random(cls):
        return cls(randrange(cls.lower_bound, cls.upper_bound))
    
    def __repr__(self):
        return f"<Number {self.value}>"