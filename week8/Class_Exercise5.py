# MAIN INFORMATION
# Course: COSC 1100-05
# Name: Class Exercise #5 - Arrays
# Author: Nolan Savage
# Date: 2026-11-3
# Group: (individual)


# ---------------------------- PROGRAM DESCRIPTION -----------------------------------

# You have now progressed beyond the midpoint of this course and would like to
# write a program to calculate your midterm mark. The description on how your
# midterm mark was calculated is in the course outline. Please refer back to the
# course outline for details.
# Your program must ask the user for their marks for each assessment, ordered by
# type. The assessments include the Pre-Class Activities, Class Exercises, the first
# Test. Once the user finishes their entry, calculate and display the user’s grade as
# a percentage and their percentage for each type of assessment.
# Your user may not always enter the correct details when asked. Ensure your
# program can identify that and guide the user on entering valid data.

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
print("We will start by entering the user's In-Class Assignment Marks.")

in_class_exercise_1 = float(input("Please enter the In-Class Exercise 1 mark: "))
in_class_exercise_2 = float(input("Please enter the In-Class Exercise 2 mark: "))
in_class_exercise_3 = float(input("Please enter the In-Class Exercise 3 mark: "))
in_class_exercise_4 = float(input("Please enter the In-Class Exercise 4 mark: "))
in_class_exercise_5 = float(input("Please enter the In-Class Exercise 5 mark: "))

# In-Class Exercise List
in_class_exercise_list = [in_class_exercise_1, in_class_exercise_2, in_class_exercise_3, in_class_exercise_4, in_class_exercise_5]



# Class Assignment (1 total)
print("Now please enter your Assignment 1 mark.")

assignment_1 = float(input("Please enter your Assignment 1 mark: "))

# Assignment 1 List
assignment_1_list = [assignment_1]



# Test marks (2 total, Practical and Theory)
print("Now please enter your Midterm test grades.")

test_theory = float(input("Please enter your mark for test one Theory: "))
test_practical = float(input("Please enter your mark for test one Practical: "))

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


# Calculating the weighted midterm grade
total_midterm_grade = (in_class_exercise_percentage * 0.25) + (assignment_1_percentage * 0.08) + (test_1_percentage * 0.16)

# ----------------------------------------------------------------------------------


# ---------------------------------- OUTPUT ------------------------------------------

# Showing the user their percentage for each three sections and then a total percentage

print(f"Your percentage for the in class exercises is %{in_class_exercise_percentage}.")
print(f"Your percentage for the assignments is %{assignment_1_percentage}.")
print(f"Your percentage for the tests is %{test_1_percentage}.")
print(f"Your total Midterm Grade is %{total_midterm_grade}. Good Job! Or maybe not and that's fine too!")