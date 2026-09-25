# MAIN INFORMATION
# Course: Just for fun
# Name: Test Problem
# Author: Nolan Savage
# Date: 2026-09-24

# Practice Problem: Road Trip

# A car gets 12 kilometers per liter of gas.

KM_PER_LITER = 12

# INPUT
kilometres_driven = float(input("How many kilometres would you like to drive? "))
gas_price = float(input("What is the price of gas per liter? "))

# PROCESS
liters_needed = kilometres_driven / KM_PER_LITER

trip_cost = liters_needed * gas_price

# OUTPUT
print(f"Liters needed: {liters_needed:.2f}")
print(f"Trip cost: ${trip_cost:.2f}")