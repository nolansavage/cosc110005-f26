
# MAIN INFORMATION
# Course: COSC 1100-05
# Name: Assignment 1
# Author: Nolan Savage
# Date: 2026-10-30
# Group: (individual)



# --------------------------------- THE PLAN ----------------------------------- #
# The program will let the user enter a bottom and top number in order to get the sqaure roots of those
# numbers within a range. The program will check for correctness including checking if the user enters
# whole numbers, if the numbers are within the range specified. Once the input has been validated then 
# and only then will the program will calculate and show the user the square numbers between the two limits
# as well as their square roots.

# ----------------------------------------------------------------------------- #




# --------------------------------- INPUT -------------------------------------- #
# The input will be the user entering in the bottom limit and the top limit.
# The bottom limit is a whole number between 1 and 10000 and the top limit is a whole number that is
# greater than the bottom limit, is still a whole number and is also between the bottom limit and 10000
# If the user does not enter a whole number or just an invalid entry, the user will be given an error
# message and be told to re enter the appropriate and correct values.

# Program Header
print("===================================================")
print("            Square Number Calculator")
print("===================================================")

# ------------------------------------------------------------------------------ #





# --------------------------------- PROCESS -------------------------------------- #
# In this section is where we will 
# 1 - Validate if the bottom number is between 1 and 10000 and also check if its a whole number
# 2 - Validate the top number to see if it is a whole number and between the bottom limit and the top limit
# 3 - Repeat the question and input if the user enters in the wrong number they can try again
# 4 - I will use loops to calculate square numbers by multiplying the whole numbers by itself
# 5 - Also check if the calculated is within the specified limits
# 6 - Finally we will show the user the square numbers that are within the range determined by the user
# along with the square roots

# Asking the user if they want to use the calculator again
try_again = "y"

while try_again.lower() == "y":

    # Asking the user for the top number and the bottom number between the limits.
    bottom_limit = input("Please enter the bottom limit number (1-10000): ")
    top_limit = input("Please enter in a top limit number (bottom limit-10000): ")

    # Validating the bottom limit
    while True:
        try:
            bottom_limit = int(bottom_limit)

            if bottom_limit >= 1 and bottom_limit <= 10000:
                break
            else:
                print("You must please enter a number that is between 1 and 10000")

        except ValueError:
            print("The number must be a whole number.")

        bottom_limit = input("Please enter the bottom limit properly: ")


    # Validating the top limit
    while True:
        try:
            top_limit = int(top_limit)

            if top_limit >= bottom_limit and top_limit <= 10000:
                break
            else:
                print("Please make sure your top number is between the bottom number and 10000.")

        except ValueError:
            print("The number has to be a whole number.")

        top_limit = input("Please enter the top limit properly: ")



    # Calculating the sqaure number that are within the user's limits
    square_answers = []

    for number in range(1, 101):
        square_number = number ** 2

        if bottom_limit <= square_number <= top_limit:
            square_answers.append((square_number, number))

    # ------------------------------------------------------------------------------- #










    # --------------------------------- OUTPUT -------------------------------------- #
    # In this section I will
    # 1 - Display a nice header when the program starts 
    # 2 - Display an error message if invalid information is inputted
    # 3 - Show the user the number limits of 1 and 10000 that they can enter
    # 4 - Display all of the square numbers that are within the range that is determined by the user
    # 5 - Also show the user the corresponding square roots for each square number
    # 6 - And make the user hit a key to exit the program


    # Displaying the square numbers and their square roots

    print()
    print("Here are the square numbers between", bottom_limit, "and", top_limit)
    print("---------------------------------------------------------------------")

    if len(square_answers) > 0:

        for square_number, square_root in square_answers:
            print("Square number:", square_number, "|=| Square root:", square_root)

    else:
        print("There are no valid square numbers within this range you entered...")


    # Wait for the user to decide if they want to stay or go
    # If the user enters "e" it will end the program
    print()
    try_again = input("Would you like to calculate another range? (Y/N): ")

    while try_again.lower() != "y" and try_again.lower() != "n":
        try_again = input("Please enter Y or N: ")

# ------------------------------------------------------------------------------- #

print("Thank you for using the Square Number Calculator!")
