# MAIN INFORMATION
# Course: COSC 1100-05
# Name: Class Exercise #6 - Functions
# Author: Nolan Savage
# Date: 2026-11-10
# Group: (individual)


# ---------------------------- PROGRAM DESCRIPTION -----------------------------------

# I have to take the existing code from class exercise #5 and shorten it with functions by getting rid 
# of all of the redundant code and simplifying it with functions.

# ----------------------------------------------------------------------------------------



# --------------------------------------- MY PLAN ----------------------------------------
# I know that I will need to create new functions to get rid of the redundancies in my code. I will do that
# by adding new functions for validations and lists. For my mental visual on this I will create a NEW
# section called "Functions"

# VALIDATION RULES
# 1 - The input must be numerical.
# 2 - The mark cannot be negative.
# 3 - The mark cannot exceed the maximum possible mark for that assessment.

# --------------------------------------------------------------------------------------


# ---------------------------------------- Functions ------------------------------------------

# Function #1 - Getting Valid Grade
def getting_valid_grade(assignment_name):

    valid_mark = False

    while valid_mark == False:
        try:
            mark = float(input(f"Please enter your {assignment_name} mark: "))

            if mark < 0:
                print("Your mark cannot be negative.")

            elif mark > 100:
                print("Your mark cannot exceed 100.")

            else:
                valid_mark = True

        except ValueError:
            print("Please enter a valid numerical mark.")

    return mark

# Function #2 - Percentage Calculation
def percentage_calculation(grade_list):

    grade_total = sum(grade_list)

    grade_percentage = grade_total / len(grade_list)

    return grade_percentage


# ------------------------------------------------------------------------------------------




# -------------------------------- INPUT -----------------------------------------------

# I am going to collect the values for each list. Starting with In-Class Exercises.

# Program Introduction
print()
print("Hello! In this program I will be calculating a midterm mark based on your inputs.")
print("However, your input must be Valid. In order for the input to be valid, the inputs must be;")
print("Numerical, cannot be a negative number and can also not exceed the maximum number for that assesment.")


# In-Class Exercises (5 total)

in_class_exercise_1 = getting_valid_grade("Planning an Application")

in_class_exercise_2 = getting_valid_grade("Numeric and String Data")

in_class_exercise_3 = getting_valid_grade("Selection")

in_class_exercise_4 = getting_valid_grade("Iteration")

in_class_exercise_5 = getting_valid_grade("Arrays")

# In-Class Exercise List
in_class_exercise_list = [in_class_exercise_1, in_class_exercise_2, in_class_exercise_3, in_class_exercise_4, in_class_exercise_5]




# Class Assignment (1 total)
print("Now please enter your Assignment 1: Iteration mark.")

assignment_1 = getting_valid_grade("Assignment 1: Iteration")

# Assignment 1 List
assignment_1_list = [assignment_1]




# Test marks (2 total, Practical and Theory)
print("Now please enter your Midterm test grades.")
# Test Theory
test_theory = getting_valid_grade("Test One Theory")

# Test Practical
test_practical = getting_valid_grade("Test One Practical")

# Test List
test_list = [test_theory, test_practical]

# --------------------------------------------------------------------------------

# ------------------------------------- PROCESS ------------------------------------


# Calculating the percentages
in_class_exercise_percentage = percentage_calculation(in_class_exercise_list)

assignment_1_percentage = percentage_calculation(assignment_1_list)

test_1_percentage = percentage_calculation(test_list)

total_midterm_grade = ((in_class_exercise_percentage * 0.25) + (assignment_1_percentage * 0.08) + (test_1_percentage * 0.16)) / 49 * 100

# ----------------------------------------------------------------------------------


# ---------------------------------- OUTPUT ------------------------------------------

# Showing the user their percentage for each three sections and then a total percentage

print("---------------------------------------------------------------------------------------------------")
print("--------------------------------------- YOUR MARKS :) ---------------------------------------------")
print(f"Your percentage for the in class exercises is {in_class_exercise_percentage:.2f}%.")
print(f"Your percentage for the assignments is {assignment_1_percentage:.2f}%.")
print(f"Your percentage for the practical and theory test is {test_1_percentage:.2f}%.")
print(f"Your total Midterm Grade is {total_midterm_grade:.2f}%. Good Job! Or maybe not, and that's fine too!")
print("----------------------------------------YOUR MARKS :) ---------------------------------------------")
print("---------------------------------------------------------------------------------------------------")



# ------------------------------------ Desk Checks -----------------------------------------------

# -------------------------------- DESK CHECKS --------------------------------

# FUNCTION #1 - getting_valid_grade()

# Purpose:
# - Gets a grade from the user.
# - Makes sure the input is not invalid before it gets accepted
#
# Desk Check:
# - User enters "peaches"
#   - It Cant convert the input into a number.
#   - ValueError occurs and an error message is displayed.
#
# - User enters -5
#   - The mark cant be less than 0
#   - Displays the negative mark error message.
#
# - User enters 101
#   - Mark is above 100.
#   - Displays the maximum mark error message.
#
# - User enters 85
#   - Mark is between 0 and 100.
#   - valid_mark becomes True.
#   - Function returns 85.0.
#   - This is how the program should be treated.
#
# Expected Outcome:
# - Function keeps asking until a valid grade is entered.
# - Only accepts numbered grades between 0 and 100.


# FUNCTION #2 - percentage_calculation()

# Purpose:
# - Calculates the average percentage from a list of grades.
#
# Desk Check:
# - Input list: [76, 89, 93]
# - grade_total = 76 + 89 + 93
# - grade_total = 258
# - len(grade_list) = 3
# - grade_percentage = 258 / 3
# - grade_percentage = 86
# - Function returns 86.
#
# Expected Outcome:
# - Adds all grades in the list together.
# - Divides the total by the number of grades.
# - Returns the average percentage.



# ---------------------------------------------------- END OF PROGRAM ------------------------------------------------------- #