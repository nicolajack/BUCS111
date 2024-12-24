#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:46:07 2024

@author: nicooo
"""

def negate_evens(vals):
    if vals == []:
        return []
    else:
        rest_negated = negate_evens(vals[1:])
        if vals[0] % 2 == 0:
            return [-vals[0]] + rest_negated
        else:
            return [vals[0]] + rest_negated
        # add code that handles vals[0] and that returns a value
        # that is based on the result of the recursive call
        
def mult10(x):
    return x*10

def mult_neg(x):
    if x % 2 == 0:
        return -x
    else:
        return x

def negate_evens_lc(vals):
    """ uses a list comprehension to return a version of the 
        list vals in which all even numbers have been 
        multiplied by -1.
        input: vals is a list of arbitrary of integers
    """
    lc = [mult_neg(x) for x in vals]
    return lc
    
        
def mystery1(wordlist):
    """ takes a list of words and does something with them """
    scored_words = [[w[-1], w] for w in wordlist]
    best_pair = max(scored_words) 
    return best_pair[1]

print(mystery1(['do', 'you', 'comprehend', 'this']))