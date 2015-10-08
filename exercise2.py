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

    Inputs:

    Expected Outputs:

    Errors:

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