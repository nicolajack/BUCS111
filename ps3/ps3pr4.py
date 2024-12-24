#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 18:24:27 2024

@author: nicooo
"""

#
# ps3pr4.py (Problem Set 3, Problem 4)
#
# More algorithm design!
#

# function 1
def rem_first(c, s):
    """ takes as inputs a single character c and an arbitrary string s and that uses recursion to create and return a version of s in which only the first occurrence of c (if any) has been removed. """
    if s == '':
        return ''
    else:
        rem_rest = rem_first(c, s[1:])
        if s[0] == c:
            return s[1:]
        else: 
            return s[0] + rem_rest
            

# function 2
def jscore(s1, s2):
    """takes two strings s1 and s2 as inputs and that uses recursion to compute and return the Jotto score of s1 compared with s2 – i.e., the number of characters in s1 that are shared by s2"""
    if s1 == '' or s2 == '':
        return 0
    else:
        if s1[0] in s2:
            rest_jscore = jscore(s1[1:], rem_first(s1[0], s2))
            return 1 + rest_jscore
        else:
            rest_jscore = jscore(s1[1:], s2)
            return rest_jscore
    
    
# function 3
def locate_first(elem, seq):
    """takes as inputs an element elem and a sequence seq, and that uses recursion (i.e., that calls itself recursively) to find and return the index of the first occurrence of elem in seq"""
    if elem == '':
        return -1
    elif seq == '' or seq == []:
        return -1
    else:
        rest_locate = locate_first(elem, seq[1:])
        if seq[0] == elem:
            return 0
        elif rest_locate != -1:
            return 1 + rest_locate
        else:
            return -1
    
# function 4
def double_final(n, values):
    """takes as inputs an integer n and an arbitrary list of integers values and that uses recursion to create and return a version of values in which only the final occurrence of n (if any) has been doubled."""
    if n == None:
        return values
    elif values == []:
        return values
    elif n not in values:
        return values
    else:
        rest_double = double_final(n, values[:-1])
        if n == values[-1]:
            return values[:-1] + [n * 2]
        else:
            return rest_double + [values[-1]]