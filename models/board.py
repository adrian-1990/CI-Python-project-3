import random
from ship import Ship

"""
The code for creating the players board was used after
finding a solution on the web.
Credit: https://bigmonty12.github.io/battleship
"""

# Used dims to create the boards dimensions
def build_board(dims):
    return [['.' for count in range(dims)] for count in range(dims)]
#The * symbol is use to print the list elements in a single line with a space
def print_board(board):
    for b in board:
        print(*b)
# Print the board 10 rows x 10 columns to match the original battleship game
board = build_board(10)
print_board(board)

def place_ships(self, automate_placement=False):
    """
    Place ships on the board
    Args:
        automate_placement (bool, optional): If the option argument is
            passed as True the board actions will be silent (no printout) &
            automated. Defaults to False.
    """
    fleet = self.fleet.get_ships_in_fleet()
    ship_placements_remaining = len(fleet)
    clear_console()
    for ship in fleet:
        while True:
            # If board functions (or specifically the placement of ships)
            # are automated then generate random input, else display board
            # and prompt for input.
            if self.board_is_automated or automate_placement:
                direction = random.choice(["h", "v"])
                (
                    start_x_coord,
                    start_y_coord,
                ) = self.generate_random_coordinates()
