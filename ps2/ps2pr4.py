#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 15:07:47 2024

@author: nicooo
"""

# 
# ps1pr2.py - Problem Set 2, Problem 4
#
# Fun with recursion, part 1
# name: Nicola Jackson
# email: nicolacj@bu.edu
#

# function 1
def total_len(words):
    """takes as input a list of 0 or more strings words and uses recursion to compute and return the value obtained by adding together the lengths of all of the strings in the list"""
    if words == '' or words == []:
        return 0
    else:
        word_count = total_len(words[1:])
        return len(words[0]) + word_count
    

# function 2
def exclaim(s):
    """takes an arbitrary string s as input and uses recursion to form and return the string formed by adding an exclamation point (i.e., the character '!') after each character in the string"""
    if s == '':
        return ''
    else:
        exclaim_rest = exclaim(s[1:])
        return s[0] + '!' + exclaim_rest
    