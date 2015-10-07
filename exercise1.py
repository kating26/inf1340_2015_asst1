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

#first half of the question
initial_purchase = stock * bought
print (initial_purchase)
initial_sales_commission = initial_purchase*commission
print (initial_sales_commission)
initial_amount_of_money = initial_sales_commission + initial_purchase
print (initial_amount_of_money)

#second half
stock_sold = stock * share_sold
print (stock_sold)
final_sales_commission = stock_sold * commission
print (final_sales_commission)
overall_cost = initial_amount_of_money + final_sales_commission
print (overall_cost)
#Using the overall cost and comparing with stock sold to se it Lakshmi profited or lost money
result = stock_sold - overall_cost
print (result)
#with -$25,065, Lakshmi lost money