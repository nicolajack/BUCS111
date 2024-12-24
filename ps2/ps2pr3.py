#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 10:35:12 2024

@author: nicooo
"""

# 
# ps1pr2.py - Problem Set 2, Problem 3
#
# More practice writing non-recursive functions
# name: Nicola Jackson
# email: nicolacj@bu.edu
#

# function 1
def len_diff(s1, s2):
    """takes as inputs two string values s1 and s2, and that returns the the difference between their lengths as a non-negative number"""
    if len(s1) >= len(s2):
        return len(s1)-len(s2)
    else:
        return len(s2)-len(s1)
    
    
# function 2
def combine(s1, s2, n):
    """takes as inputs two strings s1 and s2 and an integer n, and that returns a new string in which the first n characters of s1 are followed by the last n characters of s2"""
    return s1[:n] + s2[-n:]


# function 3
def reverse_last(vals, n):
    """takes as inputs a list vals and an integer n, and that constructs and returns a new list in which the last n values of vals are reversed and all other values from vals remain in their original positions"""
    values_first = vals[:-n]
    values_last = vals[-n:]
    values_reverse = values_last[::-1]
    if n >= len(vals):
        return vals[::-1]
    else:
        return values_first + values_reverse