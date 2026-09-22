while True:
    try:
        kiddie = int(input("Enter number of kiddie cones sold: "))
        break
    except ValueError:
        print("Please only type a whole number. Try again.")

while True:
    try:
        small = int(input("Enter number of small cones sold: "))
        break
    except ValueError:
        print("Please only type a whole number. Try again.")

while True:
    try:
        medium = int(input("Enter number of medium cones sold: "))
        break
    except ValueError:
        print("Please only type a whole number. Try again.")

while True:
    try:
        large = int(input("Enter number of large cones sold: "))
        break
    except ValueError:
        print("Please only type a whole number. Try again.")

# PROCESSING
total_scoops = (kiddie * 0.5) + (small * 1) + (medium * 2) + (large * 3)
total_ml = total_scoops * 120

# OUTPUT
print("Total ice cream sold:", total_ml, "mL")