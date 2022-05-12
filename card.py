import random
class Card:

    def __init__(self):
        self.value = 0

    def roll(self):
        self.value = random.randrange(1,13)
    
    def get_value(self):
        return self.value