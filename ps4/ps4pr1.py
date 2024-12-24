#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:44:42 2024

@author: nicooo
"""
# 
# ps4pr1.py - Problem Set 4, Problem 1
#
# From binary to decimal and back!
# name: Nicola Jackson
# email: nicolacj@bu.edu
#


def dec_to_bin(n):
    """takes a non-negative integer n and uses recursion to convert it from decimal to binary – constructing and returning a string version of the binary representation of that number"""
    if n == '':
        return ''
    elif n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        rest_dec = dec_to_bin(n//2)
        if n % 2 == 0:
            return rest_dec + '0'
        else:
            return rest_dec + '1'
        
def bin_to_dec(s):
    """takes a string b that represents a binary number and uses recursion to convert the number from binary to decimal, returning the resulting integer"""
    if s == '':
        return 0
    elif s == '1':
        return 1
    elif s == '0':
        return 0
    else:
        rest_bin = bin_to_dec(s[:-1])
        if s[-1] == '1':
            return (2*rest_bin) + 1
        else:
            return (2*rest_bin)