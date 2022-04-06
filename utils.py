import os
# Solution to clear console was found on stackoverflow
# URL: https://stackoverflow.com/questions/2084508/clear-terminal-in-python
def clear_console():
    os.system('cls' if os.name =='nt' else 'clear')


