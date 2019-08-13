#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 20:14:29 2019

@author: tylersschwartz
"""
def get_start_balance():
    """Requests the user's current loan balance, returns an int."""
    while True:
        try:
            balance = int(input("Enter your starting balance: "))
            if balance > 0:
                return balance
            else:
                print("Starting balance must be greater than zero.")
        except ValueError:
            print("Starting balance must be an integer.")


def get_annual_interest():
    """Requests the user's annual interest rate, returns a float."""
    while True:
        try:
            annual_interest_rate = float(input("Enter your annual interest rate percentage: "))
            if annual_interest_rate > 0:
                return annual_interest_rate
            else:
                print("Interest rate must be more than zero.")
        except ValueError:
            print("Interest rate must be a percentage, ie: 0.25.")


def calc_lowest_payment(balance: int, annual_interest_rate: float):
    """Calculates the lowest payment required to pay off the balance in 12 months,
    factoring in compound interest. Takes in an int and a float. Returns a float."""
    lowest_pay = 0
    balance_left = balance
    low = balance / 12
    high = (balance * (1 + annual_interest_rate) ** 12) / 12
    while abs(balance_left) >= 0.01:
        balance_left = balance
        for i in range(12):
            balance_left = balance_left - (lowest_pay)
            balance_left = balance_left + (balance_left * annual_interest_rate / 12)
        if balance_left < 0.01:
            high = lowest_pay
        else:
            low = lowest_pay
        lowest_pay = (high + low) / 2.0
    return lowest_pay


balance = get_start_balance()
annual_interest_rate = get_annual_interest()
lowest_pay = calc_lowest_payment(balance, annual_interest_rate)

print("Your minimum monthly payment to payoff balance in 12 months is:" , round(lowest_pay, 2))
