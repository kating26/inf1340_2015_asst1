#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# User inputs the number of sides and returns shapes.
shape = raw_input("Enter the number of sides for your shape: ")

def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs: Integers from 3 to 10. Users can enter other characters and numbers.

    Expected Outputs: Name of each shape based on the number of sides input by user from 3 to 10.
    3 - triangle, 4 - quadrilateral, 5 - pentagon, 6 - hexagon, 7 - heptagon, 8 - octagon,
    9 - nonagon, 10 - decagon

    Errors: Any number outside the range of 3-10 (inclusive) as well as symbol and characters
    will result in an "error".
    """

if shape =="3":
    print ('You have a triangle.')
elif shape == "4":
    print ('You have a quadrilateral.')
elif shape == "5":
    print ('You have a pentagon.')
elif shape == "6":
    print ('You have a hexagon.')
elif shape == "7":
    print ('You have a heptagon.')
elif shape == "8":
    print ('You have an octagon.')
elif shape == "9":
    print ('You have a nonagon.')
elif shape == "10":
    print ('You have a decagon.')
else:
    print ('Error')