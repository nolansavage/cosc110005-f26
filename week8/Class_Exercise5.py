# MAIN INFORMATION
# Course: COSC 1100-05
# Name: Class Exercise #5 - Arrays
# Author: Nolan Savage
# Date: 2026-11-3
# Group: (individual)


# ---------------------------- PROGRAM DESCRIPTION -----------------------------------

# I have now progressed beyond the midpoint of this course and would like to
# write a program to calculate your midterm mark. The description on how your
# midterm mark was calculated is in the course outline. 
# My program will ask the user for their marks for each assessment, ordered by
# type. The assessments include the Pre-Class Activities, Class Exercises and the first
# Test. Once the user finishes their entry, calculate and display the user’s grade as
# a percentage and their percentage for each type of assessment.
# The user may not always enter the correct details when asked. My program will
# identify that and guide the user on entering valid data.

# ----------------------------------------------------------------------------------------



# --------------------------------------- MY PLAN ----------------------------------------
# I know that I will need to have 3 seperate lists for the user to enter marks into. One that is
# In-Class Assignments, another that is Assignments and the last one is the first test.
# I will have to request the user to enter their marks in for the appropriate sections. Which means 
# I will need to tell the user what section they are entering information in for. 

# There are 5 In-Class Assignments, so that means the first list "In-Class Assignments" will have 5 elements

# There is only 1 Assignment. There will be 1 element in the second list.

# There has only been one test so far but there was a practical and a theory portion of it. Therefore, the
# last list will have 2 elements.

# I will need to take all the inputs and validate them to see if they make sense, and then convert them into
# a percentage.


# VALIDATION RULES
# 1 - The input must be numerical.
# 2 - The mark cannot be negative.
# 3 - The mark cannot exceed the maximum possible mark for that assessment.

# -------------------------------------------------------------------------------



# -------------------------------- INPUT -----------------------------------------

# I am going to collect the values for each list. Starting with In-Class Exercises.

# Program Introduction
print()
print("Hello! In this program I will be calculating a midterm mark based on your inputs.")
print("However, your input must be Valid. In order for the input to be valid, the inputs must be;")
print("Numerical, cannot be a negative number and can also not exceed the maximum number for that assesment.")

# In-Class Exercises (5 total)
valid_mark = False

while valid_mark == False:
    try:
        in_class_exercise_1 = float(input("Please enter the Planning an Application mark: "))

        if in_class_exercise_1 < 0:
            print("Your mark cannot be negative.")
        elif in_class_exercise_1 > 100:
            print("Your mark cannot exceed 100.")
        else:
            valid_mark = True

    except ValueError:
        print("Please enter a numerical value.")


valid_mark = False

while valid_mark == False:
    try:
        in_class_exercise_2 = float(input("Please enter the Numeric and String Data mark: "))

        if in_class_exercise_2 < 0:
            print("Your mark cannot be negative.")
        elif in_class_exercise_2 > 100:
            print("Your mark cannot exceed 100.")
        else:
            valid_mark = True

    except ValueError:
        print("Please enter a numerical value.")


valid_mark = False

while valid_mark == False:
    try:
        in_class_exercise_3 = float(input("Please enter the Selection mark: "))

        if in_class_exercise_3 < 0:
            print("Your mark cannot be negative.")
        elif in_class_exercise_3 > 100:
            print("Your mark cannot exceed 100.")
        else:
            valid_mark = True

    except ValueError:
        print("Please enter a numerical value.")


valid_mark = False

while valid_mark == False:
    try:
        in_class_exercise_4 = float(input("Please enter the Iteration mark: "))

        if in_class_exercise_4 < 0:
            print("Your mark cannot be negative.")
        elif in_class_exercise_4 > 100:
            print("Your mark cannot exceed 100.")
        else:
            valid_mark = True

    except ValueError:
        print("Please enter a numerical value.")


valid_mark = False

while valid_mark == False:
    try:
        in_class_exercise_5 = float(input("Please enter the Arrays mark: "))

        if in_class_exercise_5 < 0:
            print("Your mark cannot be negative.")
        elif in_class_exercise_5 > 100:
            print("Your mark cannot exceed 100.")
        else:
            valid_mark = True

    except ValueError:
        print("Please enter a numerical value.")

# In-Class Exercise List
in_class_exercise_list = [in_class_exercise_1, in_class_exercise_2, in_class_exercise_3, in_class_exercise_4, in_class_exercise_5]



# Class Assignment (1 total)
print("Now please enter your Assignment 1: Iteration mark.")

valid_mark = False

while valid_mark == False:
    try:
        assignment_1 = float(input("Please enter your Assignment 1: Iteration mark: "))

        if assignment_1 < 0:
            print("Your mark cannot be negative.")
        elif assignment_1 > 100:
            print("Your mark cannot exceed 100.")
        else:
            valid_mark = True

    except ValueError:
        print("Please enter a numerical value.")

# Assignment 1 List
assignment_1_list = [assignment_1]



# Test marks (2 total, Practical and Theory)
print("Now please enter your Midterm test grades.")


# Test Theory
valid_mark = False

while valid_mark == False:
    try:
        test_theory = float(input("Please enter your mark for test one Theory: "))

        if test_theory < 0:
            print("Your mark cannot be negative.")
        elif test_theory > 100:
            print("Your mark cannot exceed 100.")
        else:
            valid_mark = True

    except ValueError:
        print("Please enter a numerical value.")


# Test Practical
valid_mark = False

while valid_mark == False:
    try:
        test_practical = float(input("Please enter your mark for test one Practical: "))

        if test_practical < 0:
            print("Your mark cannot be negative.")
        elif test_practical > 100:
            print("Your mark cannot exceed 100.")
        else:
            valid_mark = True

    except ValueError:
        print("Please enter a numerical value.")

# Test List
test_list = [test_theory, test_practical]



# --------------------------------------------------------------------------------

# ------------------------------------- PROCESS ------------------------------------

# Getting the totals of each list
in_class_exercise_total = sum(in_class_exercise_list)

assignment_1_total = sum(assignment_1_list)

test_1_total = sum(test_list)


# Calculating the percentages
in_class_exercise_percentage = in_class_exercise_total / 5

assignment_1_percentage = assignment_1_total

test_1_percentage = test_1_total / 2


total_midterm_grade = ((in_class_exercise_percentage * 0.25) + (assignment_1_percentage * 0.08) + (test_1_percentage * 0.16)) / 49 * 100

# ----------------------------------------------------------------------------------


# ---------------------------------- OUTPUT ------------------------------------------

# Showing the user their percentage for each three sections and then a total percentage

print("---------------------------------------------------------------------------------------------------")
print(f"Your percentage for the in class exercises is {in_class_exercise_percentage:.2f}%.")
print(f"Your percentage for the assignments is {assignment_1_percentage:.2f}%.")
print(f"Your percentage for the tests is {test_1_percentage:.2f}%.")
print(f"Your total Midterm Grade is {total_midterm_grade:.2f}%. Good Job! Or maybe not and that's fine too!")
print("---------------------------------------------------------------------------------------------------")