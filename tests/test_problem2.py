# MAIN INFORMATION
# Course: Just for fun
# Name: Test Problem
# Author: Nolan Savage
# Date: 2026-09-24

# Practice Problem: Pizza Party
# Description

# A group of friends orders pizzas for a party.

# Each pizza has 8 slices.

# Ask the user:

# How many pizzas were ordered?
# How many people are attending?

# Calculate:

# Total slices available.
# How many slices each person gets.
# Display the result rounded to two decimal places.

pizza = 8

pizza_amount = int(input('How many pizzas would you like to order? '))
people = int(input('How many people are attending the party? '))

slices_available = pizza_amount * 8
slices_to_eat = slices_available / people


print(f"each person will get {slices_to_eat:.2f} slices of pizza:)")