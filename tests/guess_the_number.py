import random

# Pick a random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask the player for a guess
guess = int(input("Guess the number from 1-10: "))

# Check the guess
if guess == secret_number:
    print("YOU GOT IT!")

elif guess > secret_number:
    print("Too high!")

else:
    print("Too low!")

# Temporary: show the answer
print("The number was:", secret_number)