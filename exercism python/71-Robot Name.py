import string
import random

used_names = set()

ALPHABET = list(string.ascii_uppercase)

class Robot:
    def __init__(self):
        self.reset()

    def set_name(self):
         while True:
            name = ''.join(random.choices(ALPHABET, k=2)) + ''.join(random.choices('0123456789', k=3))
            if name not in used_names:
                used_names.add(name)
                return name

    def reset(self):
        self.name = self.set_name()