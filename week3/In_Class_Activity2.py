# MAIN INFORMATION
# Course: COSCO 1100
# Name: Rubber Ducky in-class assignment #2
# Author: Nolan Savage
# Date: 2026-09-24
# Group: 2 (individual)

# Description:
# As an estimate, we all will use the value 5000sqm (Square Meters) as
# the reservoir size. You may find a rubber duck 
# of any acceptable size and use those dimensions to help 
# complete the activity. 


# My plan is to first get the square footage of a generic rubber ducky
# from google and store that squared area so that I can
# then use to divide the duck area of the resevoir area.
# I will have to first convert the dimensions of the duck from cm to m
# before any further calculation
# I have found a duck on amazon with the dimensions of 9.8cm x 7.5cm



# CONSTANTS
# This is the total square footage of the resevoir that is 5000m^2
# This number will not change so I chose to make it a CONSTANT
RESEVOIR = 5000


# INPUT
# The input will be the two dimensions of the duck (l x w) in order to get
# the square cm area of the rubber duck.

# Duck Length
dimension_1 = float(input("Please enter first dimension: "))
# Duck Width
dimension_2 = float(input("Please enter second dimension: "))
# Duck area squared
duck_dimensions = float(dimension_1 * dimension_2)


# PROCESS
# I need to take the duck area dimensions from cm to m by dividing the duck dimensions by 100
# Calculating the area of the rubber duck from the dimensions inputted by the user to get 
# the area of the duck
duck_area = float(duck_dimensions / 100)


# Dividing the full area of the resevoir by the duck dimensions will tell me how many ducks
# can fit into the resevoir total
filled_resevoir = RESEVOIR / duck_dimensions


# OUTPUT
# My output will tell the user how many rubber ducks will fit into
# a resevoir of 5000m^2

duck_amount = RESEVOIR / duck_area

# Telling the user in plain english how many ducks will fit in the resevoir
print(f'The resevoir can hold: {duck_amount:.2f} Ducks')


