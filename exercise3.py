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
    troubleshoot = raw_input("Is the car silent when you turn the key (Y/N)? ")
    if troubleshoot == "Y": #Added a space for aesthetics
        positive_first_degree = raw_input("Are the battery terminals corroded (Y/N)? ")
        if positive_first_degree == "Y":
            print ("Clean terminals and try starting again.")
        if positive_first_degree == "N": #there is another no
            print ("Replace cables and try again.")

#Start on the right side
    if troubleshoot == "N":
        negative_first_degree = raw_input("Does the car make a clicking noise?")
        print(negative_first_degree)
        if negative_first_degree == "Y":
            print ("Replace the battery.")
        if negative_first_degree == "N":
            negative_second_degree = raw_input("Does the car crank up but fail to start?")
            print (negative_second_degree)
            if negative_second_degree == "Y":
                print ("Check spark plug connection")
            if negative_second_degree == "N":
                negative_third_degree = raw_input("Does the engine start and then die?")
                print (negative_third_degree)
                if negative_third_degree == "Y":
                    negative_fourth_degree = raw_input("Does your car have fuel injection?")









diagnose_car()

