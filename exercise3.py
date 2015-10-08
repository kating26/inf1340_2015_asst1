#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
#Start on the left side
    troubleshoot = raw_input("Is the car silent when you turn the key?")
    if troubleshoot == " yes": #Added a space for aesthetics
        positive_first_degree = raw_input("Are the battery terminals recorded?")
        print (positive_first_degree)
        if positive_first_degree == " yes": #I don't understand why I'm getting a double yes
            print ("Clean terminals and try starting again.")
        if positive_first_degree == " no": #there is another no
            print ("Replace cables and try again.")
#Start on the right side
    if troubleshoot == " no":
        negative_first_degree = raw_input("Does the car make a clicking noise?")
        print(negative_first_degree)
        if negative_first_degree == " yes":
            print ("Replace the battery.")
        if negative_first_degree == " no": #This is a bit tricky







diagnose_car()

