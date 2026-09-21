kiddie = int(input("Enter number of kiddie cones sold: "))
small = int(input("Enter number of small cones sold: "))
medium = int(input("Enter number of medium cones sold: "))
large = int(input("Enter number of large cones sold: "))

total_scoops = (kiddie * 0.5) + (small * 1) + (medium * 2) + (large * 3)

total_ml = total_scoops * 120

print("Total ice cream sold:", total_ml, "mL")