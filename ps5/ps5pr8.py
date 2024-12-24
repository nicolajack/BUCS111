#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 13:43:30 2024

@author: nicooo
"""

# 
# ps5pr8.py - Problem Set 5, Problem 8
#
# Processing sequences with loops
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# function 1
def total_len(words):
    """takes as input a list of 0 or more strings words and uses a loop to compute and return the value obtained by adding together the lengths of all of the strings in the list"""
    total = 0
    for i in words:
        total += len(i)
    return total


# function 2
def exclaim(s):
    """takes an arbitrary string s as input and uses a loop to form and return the string formed by adding an exclamation point (i.e., the character '!') after each character in the string s"""
    result = ''
    for i in range(len(s)):
        result += s[i] + '!'
    return result


# function 3
def process(vals):
    """takes as input a list of 0 or more integers vals and uses a loop to create and return a new list in which each even element of the original list has been tripled and each odd element has been left unchanged"""
    result = []
    for i in vals:
        if i % 2 == 0:
            result += [i * 3]
        else:
            result += [i]
    return result
            
            
# function 4
def merge(s1, s2):
    """takes as inputs two strings s1 and s2 and uses a loop to determine and return a new string that is formed by “merging” together the characters in the strings s1 and s2 to create a single string"""
    result = ''
    len_shorter = min(len(s1), len(s2))
    for i in range(len_shorter):
        if s1[i] == s2[i]:
            result += s1[i]
        else:
            result += s1[i] + s2[i]
            
    if len(s1) > len(s2):
        return result + s1[-(len(s1)-len(s2)):]
    elif len(s2) > len(s1):
        return result + s2[-(len(s2)-len(s1)):]
    else:
        return result
    