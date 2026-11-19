# MAIN INFORMATION
# Course: COSC 1100-05
# Name: Assignment #2 - Arrays & Functions
# Author: Nolan Savage
# Date: 2026-11-17
# Group: (individual)


# ---------------------------- PROGRAM DESCRIPTION -----------------------------------

# This program will let the user encode and decode messages by using a substitution cipher. The cipher
# is based off of the Al Bhed language. The program will ask the user whether they want to encode or
# decode a message, or to just simply exit the program.


# ----------------------------------------------------------------------------------------

# ------------------------------------- FUNCTIONS -----------------------------------------

# main menu function
def display_secret_code_menu():
    print("\n=-=-=-=-= SECRET CODE TRANSLATOR =-=-=-=-=")
    print("1. Encode a message")
    print("2. Decode a message")
    print("3. Exit the program")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

# Function to encode a message into Al Bhed language
def encode(message, key=1):

    current_message = message

    for key_count in range(key):

        encrypted_message = ""

        for letter_index in range(len(current_message)):

            letter_matched = False

            for alphabet_index in range(len(english_letters)):

                if current_message[letter_index] == english_letters[alphabet_index]:

                    encrypted_message += al_bhed_letters[alphabet_index]

                    letter_matched = True

            if letter_matched == False:

                encrypted_message += current_message[letter_index]

        current_message = encrypted_message

    return current_message

# Function to translate an Al Bhed message back into English

def decode(coded_message, key=1):

    current_translation = coded_message

    for key_count in range(key):

        translated_message = ""

        for character_position in range(len(current_translation)):

            letter_matched = False

            for alphabet_position in range(len(al_bhed_letters)):

                if current_translation[character_position] == al_bhed_letters[alphabet_position]:

                    translated_message += english_letters[alphabet_position]

                    letter_matched = True

            if letter_matched == False:

                translated_message += current_translation[character_position]

        current_translation = translated_message

    return current_translation

# ------------------------------------------------------------------------------------------

# --------------------------------------- MY PLAN ----------------------------------------



# --------------------------------------------------------------------------------------



# -------------------------------- INPUT -----------------------------------------------

# The starting value for user menu selection

menu_choice = ""

# --------------------------------------------------------------------------------------

# ------------------------------------- PROCESS ----------------------------------------
english_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
al_bhed_letters = "YPLTAVKREZGMSHUBXNCDIJFQOWypltavkrezgmshubxncdijfqow"


# --------------------------------------------------------------------------------------



# ---------------------------------- OUTPUT --------------------------------------------



# --------------------------------------------------------------------------------------