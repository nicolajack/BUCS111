#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:42:36 2024

@author: nicooo
"""

# 
# ps3pr2.py - Problem Set 3, Problem 2
#
# Algorithm design
# name: Nicola Jackson
# email: nicolacj@bu.edu
#

# function 1
def abs_list_lc(values):
    """takes as input a list of numbers called values, and that uses a list comprehension to create and return a list containing the absolute values of the numbers in values."""
    lc = [abs(x) for x in values]
    return lc


# function 2
def abs_list_rec(values):
    """takes as input a list of numbers called values, and that uses recursion to create and return a list containing the absolute values of the numbers in values"""
    if values == []:
        return []
    else:
        rest_abs = abs_list_rec(values[1:])
        if values[0] >= 0:
            return [values[0]] + rest_abs
        else:
            return [-values[0]] + rest_abs
        
        
# function 3
def num_mult_lc(m, values):
    """takes an integer m and a list of integers values and that uses a list comprehension to compute and return the number of integers in values that are multiples of m"""
    lc = [1 for x in values if x % m == 0]
    return sum(lc)


# function 4
def num_mult_rec(m, values):
    """takes an integer m and a list of integers values and that uses recursion to compute and return the number of integers in values that are multiples of m"""
    if values == []:
        return 0
    else:
        rest_num_mult = num_mult_rec(m,values[1:])
        if values[0] % m == 0:
            return 1 + rest_num_mult
        else:
             return rest_num_mult
         
            
# function 5
def num_vowels(s):
    """ returns the number of vowels in the string s input: s is a string of 0 or more lowercase letters """
    if s == '':
        return 0
    else:
        num_in_rest = num_vowels(s[1:])
        if s[0] in 'aeiou':
            return 1 + num_in_rest
        else:
            return 0 + num_in_rest
        
        
def most_vowels(words):
    """takes a list of one or more strings called words and returns the string in the list with the most vowels"""
    vowels = [[num_vowels(w), w] for w in words]
    best_pair = max(vowels)
    return best_pair[1]