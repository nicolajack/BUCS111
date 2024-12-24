#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """a new class that will smartly choose moves"""
    def __init__(self, checker, tiebreak, lookahead):
        """constructs a new ai player object"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """returns a string representing an AIPlayer object"""
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        """takes a list scores containing a score for each column of the board, and that returns the index of the column with the maximum score"""
        max_scores = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                max_scores += [i]
        if self.tiebreak == 'RIGHT':
            return max_scores[-1]
        elif self.tiebreak == 'LEFT':
            return max_scores[0]
        elif self.tiebreak == 'RANDOM':
            return random.choice(max_scores)
        
    def scores_for(self, b):
        """takes a Board object b and determines the called AIPlayer‘s scores for the columns in b"""
        scores = [7] * b.width
        for col in range(b.width):
            if b.is_full() == True:
                scores[col] = -1
            elif b.is_win_for(self.checker):
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            elif not b.can_add_to(col):
                scores[col] = -1
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(b)
                if max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 100:
                    scores[col] = 0
                else:
                    scores[col] = 50
                b.remove_checker(col)
                
        return scores
    
    def next_move(self, b):
        """overrides (i.e., replaces) the next_move method that is inherited from Player"""
        scores = self.scores_for(b)
        best_move = self.max_score_column(scores)
        return best_move
                