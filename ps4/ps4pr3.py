#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 08:39:53 2024

@author: nicooo
"""

# 
# ps4pr3.py - Problem Set 4, Problem 3
#
# Functions that process binary numbers
# name: Nicola Jackson
# email: nicolacj@bu.edu
#

# function 1
def double_rec(binvals):
    """takes a list binvals of 0 or more strings – each of which represents a binary number – and that uses recursion to compute and return a new list in which all of the binary numbers have been doubled"""
    if binvals == '':
        return []
    elif binvals == []:
        return []
    else:
        rest_double = double_rec(binvals[1:])
        return [(binvals[0]) + '0'] + rest_double

    

# function 2
def double_lc(binvals):
    """takes a list binvals of 0 or more strings – each of which represents a binary number – and that uses a list comprehension to compute and return a new list in which all of the binary numbers have been doubled"""
    return [x + '0' for x in binvals]


# function 3
def add_bitwise(b1, b2):
    """Write a function called add_bitwise(b1, b2) that adds two binary numbers. This function must use recursion to perform the bitwise, “elementary-school” addition algorithm that we discussed in lecture, and it should return the result. It must not perform any base conversions.

Your function should add one pair of bits at a time, working from right to left and including any necessary “carry” bits"""
    
    if b1 == '':
        return b2
    elif b2 == '':
        return b1   
    else: 
        rest_add = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1] == '0' and b2[-1] == '0':
            return rest_add + '0'
        elif b1[-1] == '0' and b2[-1] == '1':
            return rest_add + '1'
        elif b1[-1] == '1' and b2[-1] == '0':
            return rest_add + '1'
        else:
            carry_case = add_bitwise('1', rest_add)
            return carry_case + '0'