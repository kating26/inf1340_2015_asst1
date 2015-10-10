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

    # Diagnostic program determines what to do if car remains silent after ignition.

    troubleshoot = raw_input("Is the car silent when you turn the key? (Y/N) ")
    if troubleshoot == "Y":
        positive_first_degree = raw_input("Are the battery terminals corroded? (Y/N) ")
        if positive_first_degree == "Y":
            print ("Clean terminals and try starting again.")
        if positive_first_degree == "N":
            print ("Replace cables and try again.")

    # Diagnostic program determines what to do if the car starts.

    if troubleshoot == "N":
        negative_first_degree = raw_input("Does the car make a clicking noise? (Y/N) ")
        if negative_first_degree == "Y":
            print ("Replace the battery.")
        if negative_first_degree == "N":
            negative_second_degree = raw_input("Does the car crank up but fail to start? (Y/N) ")

            # It prescribes a solution or asks another question.

            if negative_second_degree == "Y":
                print ("Check spark plug connections.")
            if negative_second_degree == "N":
                negative_third_degree = raw_input("Does the engine start and then die?  (Y/N) ")

                # It prescribes another solution or asks another question.

                if negative_third_degree == "N":
                    print ("Engine is not getting enough fuel. Clean fuel pump.")
                if negative_third_degree == "Y":
                    negative_fourth_degree = raw_input("Does your car have fuel injection? (Y/N) ")

                    # It prescribes a final fix or take it in for professional service.

                    if negative_fourth_degree == "N":
                        print ("Check to ensure the choke is opening and closing.")
                    if negative_fourth_degree == "Y":
                        print ("Get it in for service.")

# diagnose_car()

