"""
Creates the class for ship
Each player will have 5 ships
The ships follow the Hasbro version of the board game:
Carrier
Battleship
Desrtoyer
Submarine
Patrol Boat
"""
# The length of each ship
SHIPS_LENGTH = [2, 3, 3, 4, 5]

class Ship:

    def __init__(self, name, symbol, length):
        self.name = name
        self.symbol = symbol
        self.length = length

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def get_length(self):
        return self.length

    def increment_hit_counter(self):
        self.hit_count += 1

    def get_flotation_status(self):
        return False if self.hit_count == self.get_length() else True


"""
Creates a class for each ship
Access the parent class Ship
Use super() keyword to allow child class to access parent class
"""

class Carrier(Ship):
    def __init__(self):
        super().__init__("Carrier", "C", 5)

class Battleship(Ship):
    def __init__(self):
        super().__init__("Battleship", "B", 4)

class Destroyer(Ship):
    def __init__(self):
        super().__init__("Destroyer", "D", 3)

class Submarine(Ship):
    def __init__(self):
        super().__init__("Submarine", "S", 3)

class PatrolBoat(Ship):
    def __init__(self):
        super().__init__("Patrol Boat", "P", 2)