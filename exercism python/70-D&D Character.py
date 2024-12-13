import random
import math

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()

        self.hitpoints = self.calculate_hitpoints()

    def ability(self):
        rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(rolls)[1:])

    def calculate_hitpoints(self):
        return 10 + modifier(self.constitution)

def modifier(value):
     return math.floor((value - 10) / 2)