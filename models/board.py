import random
from .ship import Ship, GameFleet
from utils import clear_console

grid = [[]]
ship_positions = [[]]

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

def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid

def validate_ship_placement(row, col, direction, length):
    """Based on direction will call helper method to try and place a ship on the board"""
    board

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)

def place_ships():
    
    random.seed(time.time())

    rows, cols = (board)

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        grid.append(row)

    num_of_ships_placed = 0

    ship_positions = []

    while num_of_ships_placed != GameFleet():
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = GameFleet.length()
        if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1