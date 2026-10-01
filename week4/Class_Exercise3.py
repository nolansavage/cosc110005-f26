# MAIN INFORMATION
# Course: COSC 1100-05
# Name: In-Class Exercise #3: Attributes
# Author: Nolan Savage
# Date: 2026-09-29
# Group: (individual)

# -------------------------------------------------------------------------------------- #

# Description:
# In this Exercise we will be choosing 4 of the 6 attributes provided by the professor
# and then we will be adding a validation for each attribute selected.

# -------------------------------------------------------------------------------------- #

# My plan:
# is to get the inputs for 4 different questions and then give the output
# all at once at the end of the program, but if they dont enter the correct value on each
# of the attributes, they will get and error message and the program will end.

# -------------------------------------------------------------------------------------- #

# CONSTANTS
# None

# -------------------------------------------------------------------------------------- #

# INPUT

# This is the Attribute that will store the Student Name.
# The validation checks to see if the inputted value is blank or not indicating that
# the user cannot have nothing as a name.
# Student Name
name = input("Enter student name: ")

if name == "":
    print("ERROR: Student name cannot be blank.")
    exit()



# This is the variable for the Student ID.
# The user types in a 9 digit number and the len function is the validation that will check
# if the length of the input from the user is 9 digits or not, if not then the user will
# get an error message and the program will end.
# Student ID
student_ID = input("Please enter your 9 digit Student ID Number: ")

if len(student_ID) != 9:
    print("You didnt enter a valid Student ID Number.")
    exit()



# This is the variable for the number of courses the user is in, 1-8.
# It will validate by checking if the user has entered a number from 1-8 by seeing if they
# entered a number 'lower than' 1, and if the number is 'greater than' 8. If they dont enter
# the correct number the program will end.
# Course Amount
course_amount = int(input("Please enter amount of courses you are taking 1-8: "))

if course_amount < 1 or course_amount > 8:
    print("You didnt enter a proper amount of courses.")
    exit()



# This is the variable for the exercise mark that will be from 0-100. It will do this by
# checking if the number is 'less than zero' or 'greater than' 100. If they don't enter
# the right number then the program will end.
# Exercise Mark
exercise_mark = int(input("Please enter your Exercise Mark from 0-100: "))

if exercise_mark < 0 or exercise_mark > 100:
    print("You did not enter in a valid number from 0-100.")
    exit()

# -------------------------------------------------------------------------------------- #

# PROCESS
# I will get the inputs from the user and calculate with the program if the values
# align with each validation. If they do not pass validation then they will get an error
# message. 
# First Attribute Validation: Checks if the input has characters entered and if not it ends.
# Second Attribute Validation: Checks if the input is not equal to 9 digits in length with
# the len function.
# Third Attribute Validation: Checks if the input is 'less than' 1, or 'greater than' 8.
# Fourth Attribute Validation: Checks if the input is 'less than 0 or 'greater than' 100.

# -------------------------------------------------------------------------------------- #

# OUTPUT
# My output will tell the user their 
# Student name
# Student ID
# The number of Courses that are being taken 1-8
# The student's Exercise number 0-100

print("------ Your Student Information -------")
print(f"Your Student Name is {name}")
print(f"Your Student ID is {student_ID}")
print(f"The amount of Courses you are taking is {course_amount}")
print(f"Your Student Exercise Mark is {exercise_mark}")
print("------ Your Student Information -------")

