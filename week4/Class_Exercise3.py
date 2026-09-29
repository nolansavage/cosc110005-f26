# MAIN INFORMATION
# Course: COSC 1100-05
# Name: in-class assignment #3: Attributes
# Author: Nolan Savage
# Date: 2026-09-29
# Group: (individual)

# -------------------------------------------------------------------------------------- #

# Description:
# In this Exercise we will be choosing 4 of the 6 attributes provided by the professor
# and then we will be adding a validation for each attribute selected.

# -------------------------------------------------------------------------------------- #

# My plan is to get the inputs for 4 different questions and then give the output
# all at once at the end of the program, but if they dont enter the correct value,
# the the 

# -------------------------------------------------------------------------------------- #

# CONSTANTS
# None

# -------------------------------------------------------------------------------------- #

# INPUT

# This is the variable that will store the Student Name.
# The validation checks to see if the inputted value is blank or not indicating that
# the user cannot have nothing as a name.
# Student Name
name = input("Enter student name: ")

if name == "":
    print("ERROR: Student name cannot be blank.")



# This is the variable for the Student ID.
# The user types in a 9 digit number and the len function is the validation that will check
# if the length of the input from the user is 9 digits or not, if not then the user will
# get an error message
student_ID = input("Please enter your 9 digit Student ID Number: ")

if len(student_ID) != 9:
    print("You didnt enter a valid Student ID Number.")



# This is the variable for the number of courses the user is in, 1-8.
# It will validate by checking if the user has entered a number from 1-8 by seeing if they
# entered a number 'lower than' 1, and if the number is 'greater than' 8.
course_amount = int(input("Please enter amount of courses you are taking 1-8: "))

if course_amount < 1 or course_amount > 8:
    print("You didnt enter a proper amount of courses.")



# This is the variable for the exercise mark that will be from 0-100. It will do this by
# checking if the number is 'less than zero' or 'greater than' 100.

exercise_mark = input("Please enter your Exercise Mark from 0-100: ")

if exercise_mark < 0 or exercise_mark > 100:
    print("You did not enter in a valid number from 0-100.")


# -------------------------------------------------------------------------------------- #

# PROCESS
# I will get the inputs from the user and calculate with the program if the values
# align with each validation. If they do not pass validation then they will get an error
# message.




# OUTPUT
# My output will tell the user their 
# Student name
# Student ID
# The number of Courses that are being taken 1-8
# The student's Exercise number 0-100


