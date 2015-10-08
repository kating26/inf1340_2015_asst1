#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

stock = 2000
bought = 900.00
commission = .03
share_sold = 942.75

# Calculate initial total cost for shares by subtracting  subtract the stockbroker's 3% commission

share_cost = stock * bought * commission
initial_total = stock * bought + share_cost
print("Lakshmi's initial stock price was $""%.2f" % initial_total)

final_price_sold = stock * share_sold * commission
final_total = stock * share_sold - final_price_sold
print ("Lakshmi's final stock price 2 weeks later was $""%.2f" % final_total)

# Calculate if Lakshmi had a profit (positive value) or loss (negative value)

net_value = final_total - initial_total
print ("The overall difference between her purchase and sell prices is $""%0.2f" % net_value)

