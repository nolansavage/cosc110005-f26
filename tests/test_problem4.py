# Practice Problem: Movie Theater

# Description:
# A movie theater has a total of 120 seats available for a movie showing.
#
# The user will enter the number of tickets sold for the movie.
#
# Your program must:
# 1. Determine how many seats are filled.
# 2. Determine how many seats are still empty.
# 3. Display both values in a clear and readable format.
#
# Assume that every ticket sold fills one seat.



# Constant is 120 seats always available to purchase
SEATS_AVAILABLE = 120

# This shows how many seats have been sold at the theatre
seats_sold = int(input(f"How many seats have been sold at the theatre: "))

# this shows how many seats have been sold out of the 120 seats
seats_taken = seats_sold - SEATS_AVAILABLE

# This shows how many seats are left
seats_left = SEATS_AVAILABLE - seats_sold

# This is the output that shows how many seats were sold and how many seats are left
print(f'There are {seats_sold} seats sold, and {seats_left} seats left')
























































































