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
    shape = raw_input("Let's name that shape")
    if shape ==" 3":
        print ('triangle')
    if shape ==" 4":
        print ('quadrilateral')
name_that_shape()




