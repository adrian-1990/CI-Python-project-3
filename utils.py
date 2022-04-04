import os
# Solution to clear console was found on stackoverflow
# URL: https://stackoverflow.com/questions/2084508/clear-terminal-in-python
def clear_console():
    os.system('cls' if os.name =='nt' else 'clear')

class validate_coordinates():

    def valid_coord_input(self, input):
        """
        Checks coordinates entered by user and
        checks they pass conditions.
        """
        valid_input = False
        while not valid_input:
            try:

                if len(input) < 2 or len(input) > 3:
                    raise ValueError
                elif len(input) == 2:
                    input = (tuple(int(i) for i in input))
                    return input

                elif len(input) < 4:
                    if "," in input:
                        input = input.split(",")
                        input = (tuple(int(i) for i in input))
                        return input
                    else:
                        input = self.coord_error_msg()
                        continue

            except ValueError:
                input = self.coord_error_msg()

    @staticmethod
    def coord_error_msg():
        """"
        Advices input is invalid,
        Requests new input and offers guidance on
        what qualifies as a valid input
        """
        new_guess = input("You input is invalid. Please use two "
                          "numbers between 0 and 9 (row then column)\n"
                          "i.e 4,5 or 45: \n").strip(" ")
        return new_guess


