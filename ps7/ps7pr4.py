#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:14:59 2024

@author: nicooo
"""
#
# ps7pr4.py  (Problem Set 7, Problem 4)
#
# Creating a simple database program using file processing
#
# Computer Science 111
# 

def main():
    """ the main user-interaction loop
    """
    filename = input('Enter the name of data file: ')
    while True:    
        city_name = input('city: ')
        if city_name == 'quit':
            break
        state_name = input('state abbreviation: ')
        city_pop(filename, city_name, state_name)
            
def city_pop(filename, city, state):
    """Find all records in the file for the city/state combination entered by the user, and output the year, rank, and population from each matching record.
    """
    file = open(filename)
    
    count = 0
    for line in file:
        line = line[:-1]
        fields = line.split(',')
        
        if fields[2] == city and fields[3] == state:
            pop = int(1000 * float(fields[-1]))
            print(fields[0] + '\t' + fields[1] + '\t' + format(pop, '10,d'))
            count += 1
    if count == 0: 
        print('no results found for', city + ',', state)
            
    file.close()