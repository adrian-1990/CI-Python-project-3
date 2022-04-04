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

class Ship:
    
    hit_count = 0
    num_of_ships = 0

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

class Fleet:
    """
    A Class to represent a fleet
    """

    fleet = []

    def get_ships_in_fleet(self):
        """Gets all ship objects in fleet
        """
        return self.fleet

    def get_num_afloat(self):
        """Gets the number of ship objects in fleet still afloat
        """
        number_of_ships = 0
        for ship in self.fleet:
            if ship.get_floatation_status() is True:
                number_of_ships += 1
        return number_of_ships

class GameFleet(Fleet):

    def __init__(self):
        self.ship1 = Carrier()
        self.ship2 = Battleship()
        self.ship3 = Destroyer()
        self.ship4 = Submarine()
        self.ship5 = PatrolBoat()
        self.fleet = [
            self.ship1,
            self.ship2,
            self.ship3,
            self.ship4,
            self.ship5
        ]