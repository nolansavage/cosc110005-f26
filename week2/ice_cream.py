#Name: Planning an event
#Author: Nolan
#Date: 2026-09-21
#Description: Calculates the total amount of ice cream sold in 
#milliliters based on user input for different cone sizes


#My plan:
#1. Get the number of cones sold for each size from the user.
#2. Calculate the total number of scoops sold.
#3. Calculate the total amount of ice cream sold in milliliters.
#4. Display the total amount of ice cream sold.



#getting the number of kiddie cones sold from the user
kiddie = int(input("Enter number of kiddie cones sold: "))

#getting the number of small cones sold from the user
small = int(input("Enter number of small cones sold: "))

#getting the number of medium cones sold from the user
medium = int(input("Enter number of medium cones sold: "))

#getting the number of large cones sold from the user
large = int(input("Enter number of large cones sold: "))

#calculating the total number of scoops sold
total_scoops = (kiddie * 0.5) + (small * 1) + (medium * 2) + (large * 3)

#calculating the total amount of ice cream sold in milliliters
total_ml = total_scoops * 120


#displays the total amount of ice cream sold in milliliters
print("Total ice cream sold:", total_ml, "mL")