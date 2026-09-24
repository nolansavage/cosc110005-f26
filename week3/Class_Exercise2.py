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
RESERVOIR = 5000


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
# I need to take the duck length and width dimensions from cm to m by dividing the duck dimensions by 10000
# Calculating the area of the rubber duck from the dimensions inputted by the user to get 
# the meter area of the duck
duck_area = float(duck_dimensions / 10000)


# OUTPUT
# My output will tell the user how many rubber ducks will fit into
# a resevoir of 5000m^2 to the second decimal point

# This is the math for caluclating the amount of ducks that can fit using the reservoir
# size by the duck area. 
duck_amount = RESERVOIR / duck_area


# Telling the user in plain english how many ducks will fit in the resevoir
print(f'The resevoir can hold: {duck_amount:.2f} Ducks')


# Desk Check #1
# Input:
# dimension_1 = 10
# dimension_2 = 10
#
# duck_dimensions = 10 * 10
#                 = 100 cm^2
#
# duck_area = 100 / 10000
#           = 0.01 m^2
#
# duck_amount = 5000 / 0.01
#             = 500000.00
#
# Output:
# The resevoir can hold: 500000.00 Ducks

# ------------------------------------------------- #

# Desk Check #2
# Input:
# dimension_1 = 15
# dimension_2 = 8
#
# duck_dimensions = 15 * 8
#                 = 120 cm^2
#
# duck_area = 120 / 10000
#           = 0.012 m^2
#
# duck_amount = 5000 / 0.012
#             = 416666.67
#
# Output:
# The resevoir can hold: 416666.67 Ducks