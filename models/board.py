import random
from utils import clear_console

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