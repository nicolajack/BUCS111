#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:26:40 2024

@author: nicooo
"""

# 
# ps1pr5.py - Problem Set 1, Problem 5
#
# Functions on strings and lists, part 1
#
# name: Nicola Jackson
# email: nicolacj@bu.edu
#

# function 1
def first_and_last(values):
    """ takes a list 'values' and returns a new list containing the first value of the original list followed by the last value of the original list """
    first = values[0]
    last = values[-1]
    return [first, last]


# function 2
def longer_len(s1, s2):
    """takes as inputs two string values s1 and s2, and that returns the length of the longer string"""
    if len(s1) > len(s2):
        longer = len(s1)
    elif len(s2) > len(s1):
        longer = len(s2)
    else:
        longer = ('same length:', len(s1))
    return longer


# function 3
def move_to_end(s, n):
    """takes as inputs a string value s and an integer n, and that returns a new string in which the first n characters of s have been moved to the end of the string"""
    if n >= len(s):
        answer = s
    else:
        answer = s[n:] + s[:n]
    return answer