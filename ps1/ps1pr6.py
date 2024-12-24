#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:57:00 2024

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
def mirror(s):
    """takes as input a string s and returns a mirrored version of s that is twice the length of the original string"""
    return s + s[::-1]


# function 2
def ends_match(s):
    """takes a string input s and returns True if the first character in s matches the last character in s, and False otherwise"""
    return s[0] == s[-1]


# function 3
def replace_end(values, new_end_vals):
    """takes as inputs a list values and another list new_end_vals, and that returns a new list in which the elements in new_end_vals have replaced the last n elements of the list values, where n is the length of new_end_vals"""
    n = len(new_end_vals)
    if len(new_end_vals) >= len(values):
        answer = new_end_vals
    else:
        answer = values[:-n] + new_end_vals
    return answer


# function 4
def repeat_elem(values, index, num_times):
    """takes as inputs a list values, an integer index (which you may assume is a valid index for one of the elements in values), and a positive integer num_times, and that returns a new list in which the element of values at position index has been repeated num_times times"""
    return values[:index] + values[index:index+1] * num_times + values[index+1:]