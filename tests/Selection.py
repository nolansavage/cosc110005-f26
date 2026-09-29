while True:

    try:
        age = int(input("Enter your age: "))
        break

    except ValueError:
        print("Please enter a number!")

if age >= 100:
    print("Your gonna die soon old head!")

elif age >= 50:
    print("Your getting close to retirement.")

elif age > 0:
    print("You're badly hurt!")

else:
    print("YOU DIED")