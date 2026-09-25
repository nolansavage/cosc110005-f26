# Practice Problem: Video Game Store
# Description

# A video game store is having a sale.

# A game costs $80.

# The store is offering a 15% discount.

# The user will enter how many games they want to buy.

# Your program must:

# Calculate the cost before the discount.
# Calculate the discount amount.
# Calculate the final cost after the discount.
# Display all three values.

# Constant game price of $80 
GAME = 80
discount = 0.15



games_bought = int(input('How many games would you like to buy? '))

price = GAME * games_bought

discount_amount = GAME * games_bought * discount



total_cost = games_bought * discount

print(f'The total amount for the purchase is ${total_cost}')
print(f'The total discount amount is ${discount_amount}')
print(f'The cost before the discount is ${price}')