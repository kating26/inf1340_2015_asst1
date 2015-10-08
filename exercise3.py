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
    troubleshoot = raw_input("Is the car silent when you turn the key? ")
    if troubleshoot == "Y":
        positive_first_degree = raw_input("Are the battery terminals corroded? ")
        if positive_first_degree == "Y":
            print ("Clean terminals and try starting again.")
        if positive_first_degree == "N":
            print ("Replace cables and try again.")

#Start on the right side
    if troubleshoot == "N":
        negative_first_degree = raw_input("Does the car make a clicking noise?")
        if negative_first_degree == "Y":
            print ("Replace the battery.")
        if negative_first_degree == "N":
            negative_second_degree = raw_input("Does the car crank up but fail to start?")#Start of second level
            if negative_second_degree == "Y":
                print ("Check spark plug connections.")
            if negative_second_degree == "N":
                negative_third_degree = raw_input("Does the engine start and then die?")#Start of third level
                if negative_third_degree == "N":
                    print ("Engine is not getting enough fuel. Clean fuel pump.")
                if negative_third_degree == "Y":
                    negative_fourth_degree = raw_input("Does your car have fuel injection?")#Start of fourth level 
                    if negative_fourth_degree == "N":
                        print ("Check to ensure the choke is opening and closing.")
                    if negative_fourth_degree == "Y":
                        print ("Get it in for service.")
#diagnose_car()

