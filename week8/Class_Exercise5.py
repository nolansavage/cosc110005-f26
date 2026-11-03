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

# -------------------------------------------------------------------------------



# -------------------------------- INPUT -----------------------------------------

# I am going to collect the values for each list. Starting with In-Class Exercises.

# Program Introduction
print()
print("Hello! In this program I will be calculating a midterm mark based on your inputs.")

# Pre Class Activities List (5 total)
print("We will start by entering the user's In-Class Assignment Marks.")

in_class_exercise_1 = input("Please enter the In-Class Exercise 1 mark: ")
in_class_exercise_2 = input("Please enter the In-Class Exercise 2 mark: ")
in_class_exercise_3 = input("Please enter the In-Class Exercise 3 mark: ")
in_class_exercise_4 = input("Please enter the In-Class Exercise 4 mark: ")
in_class_exercise_5 = input("Please enter the In-Class Exercise 5 mark: ")

# In-Class Exercise List
in_class_assignemnt_list = [in_class_exercise_1, in_class_exercise_2, in_class_exercise_3, in_class_exercise_4, in_class_exercise_5]



# Class Assignment List (1 total)
print("Now please enter your Assignment 1 mark.")

Assignment_1 = input("Please enter your Assignment 1 mark: ")

# Assignment 1 List
Assignment_1_list = [Assignment_1]



# Test Grades (2 total, Practical and Theory)
print("Now please enter your Midterm test grades.")

test_theory = input("Please enter your mark for test one Theory: ")
test_practical = input("Please enter your mark for test one Practical: ")

# Test List

test_list = [test_theory, test_practical]


# --------------------------------------------------------------------------------

# ------------------------------------- PROCESS ------------------------------------

# Getting the percentages of each list

# Preparatory Quiz Percentage
preparatory_quiz_list_percentage = preparatory_quiz_list / 5 * 100

print(f"Your percentage for the preparatory quizzes is %{preparatory_quiz_list_percentage}.")


# In-Class Exercise Percentage



# ----------------------------------------------------------------------------------


# ---------------------------------- OUTPUT ------------------------------------------

# Showing the user their percentage for each three sections and then a total percentage



















