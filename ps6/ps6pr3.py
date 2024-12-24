#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:03:10 2024

@author: nicooo
"""

# 
# ps6pr3.py - Problem Set 6 Problem 3
#
# FFunctions that use loops
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# function 1
def repeat(s, n):
    """takes a string s and an integer n, and that uses a loop to create and return a string in which n copies of s have been concatenated together."""
    m = ''
    for x in range(n):
        m+=s
    return m


# function 2
def contains(s, c):
    """takes an arbitrary string s and a single-character c as inputs and uses a loop to determine if s contains the character c, returning True if it does and False if it does not"""
    for x in s:
        if x == c:
            return True
    return False


# function 3
def add(vals1, vals2):
    """takes as inputs two lists of numbers, vals1 and vals2, and that uses a loop to construct and return a new list in which each element is the sum of the elements at the corresponding positions in the original lists"""
    if len(vals1) < len(vals2):
        vals1 = ((len(vals2)-len(vals1)) * [0]) + vals1
    elif len(vals2) < len(vals1):
        vals2 = ((len(vals1)-len(vals2)) * [0]) + vals2
    for i in range(len(vals1)):
        vals2[i] += vals1[i]
    return vals2


# function 4
def replace(vals, old, new):
    """takes a list of integers called vals and two integers old and new, and that modifies the list so that all occurrences of old are replaced with new, and all other elements are left unchanged"""
    for i in range(len(vals)):
        if vals[i] == old:
            vals[i] = new