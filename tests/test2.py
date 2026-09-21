import random

# -------------------------
# PLAYER
# -------------------------

name = input("What is your name? ")

health = 100
money = 20
inventory = ["pistol", "water"]


# -------------------------
# GAME INTRO
# -------------------------

print()
print("================================")
print("       SPACE SURVIVOR")
print("================================")
print()

print("Welcome,", name)
print("You wake up alone aboard a damaged spaceship.")
print("You have", money, "credits.")
print("Your health is", health)
print()


# -------------------------
# MAIN GAME LOOP
# -------------------------

while health > 0:

    print()
    print(f"What do you want to do, {name}?")
    print("1. Explore")
    print("2. Check inventory")
    print("3. Rest")
    print("4. Quit")

    choice = input("> ")

    # -------------------------
    # EXPLORE
    # -------------------------

    if choice == "1":

        print()
        print("You explore the ship...")

        event = random.randint(1, 3)

        if event == 1:

            print("You found 10 credits!")
            money += 10

        elif event == 2:

            print("A space monster attacks!")

            enemy_health = 30

            while enemy_health > 0 and health > 0:

                print()
                print("Your health:", health)
                print("Monster health:", enemy_health)

                attack = input("Attack or run? ")

                if attack == "attack":

                    damage = random.randint(5, 15)

                    enemy_health -= damage

                    print("You dealt", damage, "damage!")

                    if enemy_health > 0:

                        enemy_damage = random.randint(3, 10)

                        health -= enemy_damage

                        print("The monster hit you for",
                              enemy_damage, "damage!")

                elif attack == "run":

                    print("You escaped!")
                    break

                else:

                    print("You don't know how to do that.")

            if enemy_health <= 0:
                print("You defeated the monster!")
                print("You found 15 credits!")

                money += 15

        else:

            print("You found nothing.")

    # -------------------------
    # INVENTORY
    # -------------------------

    elif choice == "2":

        print()
        print("Your inventory:")

        for item in inventory:
            print("-", item)

    # -------------------------
    # REST
    # -------------------------

    elif choice == "3":

        print()
        print("You rest for a while.")

        health += 10

        if health > 100:
            health = 100

        print("You recovered some health.")
        print("Health:", health)

    # -------------------------
    # QUIT
    # -------------------------

    elif choice == "4":

        print()
        print("You leave the spaceship.")
        break

    # -------------------------
    # INVALID INPUT
    # -------------------------

    else:

        print()
        print("That's not a valid choice.")


# -------------------------
# GAME OVER
# -------------------------

if health <= 0:

    print()
    print("================")
    print("    GAME OVER")
    print("================")

print()
print("You finished with", money, "credits.")
print("Thanks for playing!")