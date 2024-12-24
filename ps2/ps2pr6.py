#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 12:24:10 2024

@author: nicooo
"""

# 
# ps2pr6.py - Problem Set 2, Problem 6
#
# Fun with recursion, part 3
# name: Nicola Jackson
# email: nicolacj@bu.edu
#

# function 1
def letter_score(letter):
    """takes a lowercase letter as input and returns the value of that letter as a scrabble tile. If letter is not a lowercase letter from ‘a’ to ‘z’, the function should return 0"""
    assert(len(letter) == 1)
    if letter in ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']:
        return 1
    elif letter in ['d', 'g']:
        return 2
    elif letter in ['b', 'c', 'm', 'p']:
        return 3
    elif letter in ['f', 'h', 'v', 'w', 'y']:
        return 4
    elif letter in ['k']:
        return 5
    elif letter in ['j', 'x']:
        return 8
    elif letter in ['q', 'z']:
        return 10
    else:
        return 0
    
    
# function 2
def scrabble_score(word):
    """takes as input a string word containing only lowercase letters, and that uses recursion to compute and return the scrabble score of that string – i.e., the sum of the scrabble scores of its letters"""
    if word == '':
        return 0
    else:
        rest_score = scrabble_score(word[1:])
        return letter_score(word[0]) + rest_score
    
    
# function 3
def smaller_of(vals1, vals2):
    """takes as inputs two lists vals1 and vals2 and uses recursion to construct and return a new list in which each element is the the smaller of the corresponding elements from the original lists."""
    if vals1 == [] or vals2 == []:
        return []
    else: 
        rest_smaller = smaller_of(vals1[1:], vals2[1:])
        if vals1[0] < vals2[0]:
            return [vals1[0]] + rest_smaller
        else:
            return [vals2[0]] + rest_smaller
        
        
# function 4
def merge(s1, s2):
    """takes as inputs two strings s1 and s2 and uses recursion to determine and return a new string that is formed by “merging” together the characters in the strings s1 and s2 to create a single string."""
    if s1 == '': 
        return s2
    elif s2 == '':
        return s1
    else:
        rest_merge = merge(s1[1:], s2[1:])
        if s1[0] == s2[0]:
            return s1[0] + rest_merge
        else:
            return s1[0] + s2[0] + rest_merge