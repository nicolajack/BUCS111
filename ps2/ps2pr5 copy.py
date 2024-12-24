#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:53:11 2024

@author: nicooo
"""

# 
# ps2pr5.py - Problem Set 2, Problem 5
#
# Fun with recursion, part 2
# name: Nicola Jackson
# email: nicolacj@bu.edu
#

# function 1
def add(vals1, vals2):
    """takes as inputs two lists of numbers, vals1 and vals2, and that uses recursion to construct and return a new list in which each element is the sum of the elements at the corresponding positions in the original lists"""
    if len(vals1) != len(vals2):
        return []
    elif len(vals1) == 0 or len(vals2) == 0:
        return []
    else:
        add_rest = add(vals1[1:], vals2[1:])
        return [vals1[0] + vals2[0]] + add_rest
    
    
# function 2
def contains(s, c):
    """takes an arbitrary string s and a single-character c as inputs and uses recursion to determine if s contains the character c, returning True if it does and False if it does not"""
    if s == '':
        return False
    elif s[0] == c:
        return True
    else:
        contains_rest = contains(s[1:], c)
        return contains_rest


# function 3
def process(vals):
    """takes as input a list of 0 or more integers vals and uses recursion to create and return a new list in which each even element of the original list has been tripled and each odd element has been left unchanged"""
    if vals == []:
        return []
    else:
        process_rest = process(vals[1:])
        if vals[0] % 2 == 0:
            return [vals[0] * 3] + process_rest
        else:
            return [vals[0]] + process_rest