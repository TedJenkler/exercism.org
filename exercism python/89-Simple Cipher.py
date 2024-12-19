import random
import string

class Cipher:
    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))

    def helper(self, text, type):
        result = []
        for i, char in enumerate(text):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shift = ord(self.key[i % len(self.key)]) - ord('a')
                if type == "encode":
                    shifted = (ord(char) - base + shift) % 26 + base
                else:
                    shifted = (ord(char) - base - shift) % 26 + base
                result.append(chr(shifted))
            else:
                result.append(char)
        return ''.join(result)        
    
    def encode(self, text):
        return self.helper(text, "encode")

    def decode(self, text):
        return self.helper(text, "decode")