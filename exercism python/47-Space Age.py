import math

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.minutes = self.seconds / 60
        self.hours = self.minutes / 60
        self.days = self.hours / 24

    def on_earth(self):
        return math.ceil((self.days / 365.25) * 100) / 100

    def on_mercury(self):
        return math.floor((self.on_earth() / 0.2408467) * 100) / 100

    def on_venus(self):
        return math.floor((self.on_earth() / 0.61519726) * 100) / 100

    def on_mars(self):
        return math.floor((self.on_earth() / 1.8808158) * 100) / 100

    def on_jupiter(self):
        return math.ceil((self.on_earth() / 11.862615) * 100) / 100

    def on_saturn(self):
        return math.floor((self.on_earth() / 29.447498) * 100) / 100

    def on_uranus(self):
        return math.ceil((self.on_earth() / 84.016846) * 100) / 100

    def on_neptune(self):
        return math.floor((self.on_earth() / 164.79132) * 100) / 100
     