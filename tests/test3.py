sales = float(input("Enter gross sales:$ "))

try:
    number = float(input("Enter a number: "))
    print(f"You entered {number}")
except ValueError:
    print("Please enter a number, not a word.")

if sales < 10000:
    rate = 0.04
elif sales <= 15000:
    rate = 0.065
else:
    rate = 0.09

commission = sales * rate

print("Commission:", commission)