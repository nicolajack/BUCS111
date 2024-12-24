#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.

class Player: 
    """a data type for a connect four player"""
    def __init__(self, checker):
        """constructs a new Player object by initializing the following two attributes"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        """returns a string representing a Player object. The string returned should indicate which checker the Player object is using"""
        return 'Player ' + self.checker
    
    def opponent_checker(self):
        """returns a one-character string representing the checker of the Player object’s opponent"""
        if self.checker == 'O':
            return 'X'
        elif self.checker == 'X':
            return 'O'
        
    def next_move(self, b):
        """accepts a Board object b as a parameter and returns the column where the player wants to make the next move"""
        col = int(input('Enter a column: '))
        while col < 0 or col > (b.width - 1):
            print("Try again!")
            col = int(input('Enter a column: '))
        self.num_moves += 1
        return col
            
        