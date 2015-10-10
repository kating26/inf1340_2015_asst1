#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Sets the values for Lakshmi's buying and selling of stocks.

stock = 2000
bought = 900.00
commission = .03
share_sold = 942.75

# Calculates initial total cost for all shares with the stockbroker's 3% commission.

purchase_commission = stock * bought * commission
initial_total = stock * bought + purchase_commission
print("Lakshmi's initial stock price was ""%.2f" % initial_total)

# Calculates the price the stocks sold for minus the stockbroker's 3% commission.

sales_commission = stock * share_sold * commission
final_total = stock * share_sold - sales_commission
print ("Lakshmi's final stock price 2 weeks later was ""%.2f" % final_total)

# Calculates if Lakshmi's stocks had a profit (positive value) or a loss (negative value).

net_value = final_total - initial_total
print ("The overall difference between her purchase and sell prices is ""%0.2f" % net_value)

