#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():

    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs: Users enters a number from 3 to 10 (inclusive). Numbers, characters and symbols
    can be entered as well.

    Expected Outputs: The outputs are 3 results in a triangle; 4, a quadrilateral;
    5, a pentagon; 6, a hexagon; 7, a heptagon; 8, a octagon; 9, a nonagon; and
    10, a decagon.

    Errors: Any characters, symbols or numbers outside this range will result in an 'error'
    message.
    """

    shape = raw_input("Enter the number of sides for your shape: ")

    if shape == "3":
        print ('triangle')
    elif shape == "4":
        print ('quadrilateral')
    elif shape == "5":
        print ('pentagon')
    elif shape == "6":
        print ('hexagon')
    elif shape == "7":
        print ('heptagon')
    elif shape == "8":
        print ('octagon')
    elif shape == "9":
        print ('nonagon')
    elif shape == "10":
        print ('decagon')
    else:
        print ('Error')

# name_that_shape()