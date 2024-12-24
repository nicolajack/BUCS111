# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

# function 1
def cube(x):
    """ takes a number x as its input and returns the cube of its input """
    return x**3


# function 2
def convert_to_inches(yards, feet):
    """takes two numeric inputs yards and feet that together represent a single length broken up into yards and feet, and that returns the corresponding length in inches"""
    if yards<0:
        yards = 0
    if feet<0:
        feet = 0
    yards = yards * 36
    feet = feet * 12
    return yards + feet

# function 3
def area_sq_inches(height_yds, height_ft, width_yds, width_ft):
    """the function takes four numeric inputs and returns the area of the rectangle in square feet"""
    height = convert_to_inches(height_yds, height_ft)
    width = convert_to_inches(width_yds, width_ft)
    return height * width
       

# function 4
def median(a, b, c):
    """takes three numeric inputs a, b, and c, and than returns the median of the three inputs"""
    if a > b:
        if a < c:
            median_value = a
        elif b > c:
            median_value = b
        else:
            median_value = c
    else:
        if a > c:
            median_value = a
        elif b < c:
            median_value = b
        else:
            median_value = c
    return median_value

           
    
# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))

    # optional but encouraged: add test calls for your functions below
