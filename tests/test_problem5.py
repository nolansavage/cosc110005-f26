# Practice Problem: School Fundraiser
# Description

# A school is selling chocolate bars to raise money.

# Each chocolate bar costs $3.

# The user will enter how many chocolate bars were sold.

# Your program must:

# Calculate the total money earned.
# Calculate how much money is still needed to reach a fundraising goal of $500.
# Display both values.

GOAL = 500
CHOCOLATE_BAR = 3

chocolate_sold = float(input('How many chocolate bars were sold at school? '))

money_earned = chocolate_sold * CHOCOLATE_BAR

money_needed = GOAL - money_earned

print(f'The amount of money that was raised from chocolate is ${money_earned}')
print(f'the amount of money still needed for the fundraiser is ${money_needed}')




