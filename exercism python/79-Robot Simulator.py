
NORTH = 'NORTH'
EAST = 'EAST'
WEST = 'WEST'
SOUTH = 'SOUTH'

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, command):
        for letter in command:
            if letter == 'R':
                if self.direction == NORTH:
                    self.direction = EAST
                elif self.direction == EAST:
                    self.direction = SOUTH
                elif self.direction == SOUTH:
                    self.direction = WEST
                elif self.direction == WEST:
                    self.direction = NORTH

            elif letter == 'L':
                if self.direction == NORTH:
                    self.direction = WEST
                elif self.direction == WEST:
                    self.direction = SOUTH
                elif self.direction == SOUTH:
                    self.direction = EAST
                elif self.direction == EAST:
                    self.direction = NORTH

            elif letter == 'A':
                if self.direction == NORTH:
                    self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
                elif self.direction == EAST:
                    self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
                elif self.direction == SOUTH:
                    self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
                elif self.direction == WEST:
                    self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])
                