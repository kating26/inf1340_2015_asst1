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
    """ For a given number of sides in a regular polygon, returns the shape name"""
    return
    shape = raw_input("Input the number of sides for your shape: ")
    if shape == "3":
        print ("Your shape is a triangle")
    elif shape == "4":
        print ("Your shape is a quadrilateral")
    elif shape == "5":
        print ("Your shape is a pentagon")
    elif shape == "6":
        print ("Your shape is a hexagon")
    elif shape == "7":
        print ("Your shape is a heptagon")
    elif shape == "8":
        print ("Your shape is an octagon.")
    elif shape == "9":
        print ("Your shape is an enneagon.")
    elif shape == "10":
        print ("Your shape is a decagon")
    else:
        print ("Error")


"""
def name_that_shape():
    if shape == "3":
        print 'Triangle'
"""
"""

Inputs:

Expected Outputs:

Errors:

"""






