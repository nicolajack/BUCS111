#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import load_pixels
from hmcpng import save_pixels
from hmcpng import compare_images

def create_green_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are colored green.
        inputs: height and width are non-negative integers
    """
    pixels = []

    for r in range(height):
        row = [[0, 255, 0]] * width
        pixels += [row]

    return pixels

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below
# function 1
def bw(pixels, threshold):
    """takes the 2-D list pixels containing pixels for an image, and that creates and returns a new 2-D list of pixels for an image that is a black-and-white version of the original image"""
    height = len(pixels)
    width = len(pixels[0])
    new_pixels = create_green_image(height, width)
    
    for r in range(height):
        for c in range(width):
            if brightness(pixels[r][c]) > threshold:
                new_pixels[r][c] = [255, 255, 255]
            else:
                new_pixels[r][c] = [0, 0, 0]
                
    return new_pixels


# function 2
def upside_down(pixels):
    """takes the 2-D list pixels containing pixels for an image, and that creates and returns a new 2-D list of pixels for an image in which the original image is “upside down”."""
    height = len(pixels)
    width = len(pixels[0])
    new_pixels = create_green_image(height, width)
    
    for r in range(height):
        for c in range(width):
            new_pixels[r][c] = pixels[height - r - 1][c]
    
    return new_pixels


# function 3
def reflect(pixels):
    """takes the 2-D list pixels containing pixels for an image, and that creates and returns a new 2-D list of pixels for an image in which the right half of original image is replaced by a “reflection” of the left half"""
    height = len(pixels)
    width = len(pixels[0])
    new_pixels = create_green_image(height, width)
    
    for r in range(height):
        for c in range(width):
            if c >= width // 2:
                new_pixels[r][c] = pixels[r][width - c - 1]
            else:
                new_pixels[r][c] = pixels[r][c]
                
    return new_pixels


# function 4 # fix this OKAY.
def shrink(pixels):
    """takes the 2-D list pixels containing pixels for an image, and that creates and returns a new 2-D list that represents an image that is half the size of the original image"""
    height = len(pixels)
    width = len(pixels[0])
    new_height = height//2
    new_width = width//2
    new_pixels = create_green_image(new_height, new_width)
    
    for r in range(0, height, 2):
        for c in range(0, width, 2):
            new_pixels[r//2][c//2] = pixels[r][c]
    return new_pixels
            