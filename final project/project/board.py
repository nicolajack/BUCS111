#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Nicola Jackson
# email: nicolacj@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(3):
            for c in range(3):
                self.tiles[r][c] = digitstr[3*r + c]
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c 


    ### Add your other method definitions below. ###
    def __repr__(self):
        """returns a string representation of a Board object"""
    
        board = ''
        
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    board += '_ '
                else:
                    board += self.tiles[r][c]
                    board += ' '
            board += '\n'
        
        return board
    
    
    def move_blank(self, direction):
        """takes as input a string direction that specifies the direction in which the blank should move, and that attempts to modify the contents of the called Board object accordingly"""
        if direction not in ['up', 'down', 'left', 'right']:
            return False
        if direction == 'up':
            new_blank_r = self.blank_r - 1
            new_blank_c = self.blank_c
        elif direction == 'down':
            new_blank_r = self.blank_r + 1
            new_blank_c = self.blank_c
        elif direction == 'left':
            new_blank_r = self.blank_r
            new_blank_c = self.blank_c - 1
        elif direction == 'right':
            new_blank_r = self.blank_r 
            new_blank_c = self.blank_c + 1
        if new_blank_r not in range(3):
            return False
        elif new_blank_c not in range(3):
            return False
        else:
            new_blank = self.tiles[new_blank_r][new_blank_c]
            old_blank = self.tiles[self.blank_r][self.blank_c]
            self.tiles[self.blank_r][self.blank_c] = new_blank
            self.tiles[new_blank_r][new_blank_c] = old_blank
            self.blank_r = new_blank_r
            self.blank_c = new_blank_c
            return True
        
        
    def digit_string(self):
        """creates and returns a string of digits that corresponds to the current contents of the called Board object’s tiles attribute"""
        digitstr = ''
        for r in range(3):
            for c in range(3):
                digitstr += self.tiles[r][c]
        return digitstr
    
    
    def copy(self):
        """returns a newly-constructed Board object that is a deep copy of the called object (i.e., of the object represented by self)"""
        new_digitstr = self.digit_string()
        new_board = Board(new_digitstr)
        return new_board
    
    
    def num_misplaced(self):
        """counts and returns the number of tiles in the called Board object that are not where they should be in the goal state. You should not include the blank cell in this count, even if it’s not where it should be in the goal state."""
        out_of_place = 0
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != GOAL_TILES[r][c] and self.tiles[r][c] != '0':
                    out_of_place += 1
        return out_of_place
    
    
    def __eq__(self, other):
        """can be called when the == operator is used to compare two Board objects. The method should return True if the called object (self) and the argument (other) have the same values for the tiles attribute, and False otherwise."""
        if self.tiles == other.tiles:
            return True
        else:
            return False