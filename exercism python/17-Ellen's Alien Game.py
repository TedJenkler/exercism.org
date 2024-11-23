"""Solution to Ellen's Alien Game exercise."""


class Alien:

    total_aliens_created = 0
    
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        
        self.health = 3

        Alien.total_aliens_created += 1

    def hit(self):
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other_object):
       
        pass

    

def new_aliens_collection(coordinates):
    return [Alien(x, y) for x, y in coordinates]