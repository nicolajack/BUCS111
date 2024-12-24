#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 17:03:04 2024

@author: nicooo
"""

# 
# ps4pr2.py - Problem Set 4, Problem 2
#
# Using your conversion functions
# name: Nicola Jackson
# email: nicolacj@bu.edu
#

from ps4pr1 import bin_to_dec
from ps4pr1 import dec_to_bin

# function 1
def pow_bin(b, e):
    """takes as inputs two strings b and e that represent binary integers. The function should determine the result of raising b to the e power and return the result in the form of a string that represents a binary number."""
    base = bin_to_dec(b)
    exp = bin_to_dec(e)
    pow = dec_to_bin(base ** exp)
    return pow


# function 2
def smallest_bin(binvals):
    """takes a list binvals of 1 or more strings – each of which represents a binary number – and that finds and returns the string in binvals that represents the smallest binary number."""
    decvals = [bin_to_dec(x) for x in binvals]
    smallest_dec = min(decvals)
    return dec_to_bin(smallest_dec)