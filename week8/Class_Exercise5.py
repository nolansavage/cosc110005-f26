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
# Pre-Class Activities, another that is Class Exercises and the last one is the first test.
# I will have to request the user to enter their marks in for the appropriate sections. Which means 
# I will need to tell the user what section they are entering information in for. 

# There are 5 preparatory quizzes so that means the first list "Pre-Class Activities" will have 5 elements

# There are currently 5 Class Exercises including this one. There will be 5 elements in the second list.

# There has only been one test so far but there was a practical and a theory portion of it. Therefore, the
# last list will have 2 elements.


# -------------------------------------------------------------------------------



# -------------------------------- INPUT -----------------------------------------

# I am going to collect the values for each list. Starting with pre-class activities.

# Program Introduction
print()
print("Hello! In this program I will be calculating a midterm mark based on your inputs.")

# Pre Class Activities List (5 total)
print("We will start by entering the user's Preparatory Quiz Marks.")

preparatory_quiz_1 = input("Please enter the Preparatory Quiz 1 mark: ")
preparatory_quiz_2 = input("Please enter the Preparatory Quiz 2 mark: ")
preparatory_quiz_3 = input("Please enter the Preparatory Quiz 3 mark: ")
preparatory_quiz_4 = input("Please enter the Preparatory Quiz 4 mark: ")
preparatory_quiz_5 = input("Please enter the Preparatory Quiz 5 mark: ")

preparatory_quiz_list = [preparatory_quiz_1, preparatory_quiz_2, preparatory_quiz_3, preparatory_quiz_4, preparatory_quiz_5]

# Class Exercises List (5 total)
print("Now please enter your In-Class Exercise marks.")

in_class_exercise_1 = input("Please enter your In-Class Exercise 1 mark: ")
in_class_exercise_2 = input("Please enter your In-Class Exercise 2 mark: ")
in_class_exercise_3 = input("Please enter your In-Class Exercise 3 mark: ")
in_class_exercise_4 = input("Please enter your In-Class Exercise 4 mark: ")
in_class_exercise_5 = input("Please enter your In-Class Exercise 5 mark: ")



# Test Grades (2 total, Practical and Theory)
print("Now please enter your Midterm test grades.")

test_theory = input("Please enter your mark for test one Theory: ")
test_practical = input("Please enter your mark for test one Practical: ")


# --------------------------------------------------------------------------------

# ------------------------------------- PROCESS ------------------------------------

# Getting the percentages of each list

preparatory_quiz_list_percentage = preparatory_quiz_list / 5 * 100

print(f"Your percentage for the preparatory quizzes is %{preparatory_quiz_list_percentage}.")


# ----------------------------------------------------------------------------------


# ---------------------------------- OUTPUT ------------------------------------------

# Showing the user their percentage for each three sections and then a total percentage



















