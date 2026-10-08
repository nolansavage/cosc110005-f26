# MAIN INFORMATION
# Course: COSC 1100-05
# Name: In-Class Exercise #4: Iteration
# Author: Nolan Savage, Usman Shamroz
# Date: 2026-10-08


# Plan
# The plan is to open the program by sending John a welcome message when opening the program.
# The opening message will explain what John's options are.. John's options are 1-4, 1-3 being the
# hotdog inputs so he can enter the number of hotdogs sold. The 4th option will let John tally up
# the total amount of hot dogs sold so that he can see which hotdogs performed the best.Our program will
# also loop whenever he chooses to input hotdog's until he chooses the fourth "tally" option.

# """
# OUTPUT: What will the program show?
# Number of Traditional hot dogs sold
# Number of Veggie hot dogs sold
# Number of Veggie hot dogs sold
# Number of Curry hot dogs sold
# Total hot dogs sold 
# Percentage of each type sold 
# Which type was the most popular
# The exit the Program

# """


# """
# INPUT: What does John enter?
# 1.Tradtional hot dogs
# 2.Veggie hot dogs
# 3.Curry hot dogs
# 4.Tally option then Exit

# John wont always hit these keys so we need to dela with the invalid input when there are too many customers.
# """


# """
# Process: How will the program work? 
# All the hot dogs sold will be set as 0 

# Display menu 

# repeat until the user enters 4 to exit
#     Get the user's menu choice 

#     If choice is 1
#         Ask for the number of traditional hot dogs sold
#         Add the number to the total of traditional hot dogs sold

#     If choice is 2
#         Ask for the number of veggie hot dogs sold
#         Add the number to the total of veggie hot dogs sold

#     If choice is 3
#         Ask for the number of curry hot dogs sold
#         Add the number to the total of curry hot dogs sold

#     If choice is 4
#         Calculate total hot dogs sold
#         Calculate percentage 
#         Display totals and percentages
#         Exit

# Program will keep looping until John chooses 4
# """

# These are the variables that will store the number of hotdogs sold.
# The hot dog counter
traditional = 0
curry = 0 
veggie = 0

# This is the choice variable
choice = 0

# Welcome message
print('''Hello John! This program is designed to help you
tally up the number of hotdogs sold for each type of hotdog''')


# This will tell the program that if the input IS NOT 4 then to keep looping inside of the while loop
# until finished and ready to tally up the totals.
while choice != 4:

    # This is the main Hotdog Menu
    print("---- HOTDOG MENU ----")
    print("Please choose which hotdog you would like to edit number sold.")
    print("1. Traditional Hotdog")
    print("2. Veggie Hotdog")
    print("3. Curry Hotdog")
    print("4. Tally up the totals and then exit")
    print("---- HOTDOG MENU ----")


    # This section is for option selection and inputs
    choice = ("Which option would you like to select 1-4?")

    if choice == 1:
        amount = int(input("How many Traditional Hotdogs were sold this week: "))
        traditional += amount 

    elif choice == 2:
        amount = int(input("How many Veggie Hotdogs were sold this week: "))
        veggie += amount

    elif choice == 3:
        amount = int(input("How many Curry Hotdogs were sold this week: "))
        curry += amount

    elif choice == 4:
        int(input("Tallying up the totals"))

    # This will catch an error if a wrong number was typed in
    else:
        print("Please enter a valid option. Enter a number 1-4 only.")



    # Calculating the totals
print("--------- The Hotdog Tally ----------")
print(f"The total amount of Traditional Hot Dogs sold is {traditional}.")
print(f"The total amount of Veggie Hotdogs sold is {veggie}.")
print(f"The total amount of Curry Hotdogs sold is {curry}.")













