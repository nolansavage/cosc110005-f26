import random


# -------------------------
# PLAYER
# -------------------------

player = {
    "name": "Captain",
    "health": 100,
    "credits": 50
}


# -------------------------
# FUNCTIONS
# -------------------------

def show_status():
    print("\n====================")
    print("SHIP STATUS")
    print("====================")
    print("Captain:", player["name"])
    print("Health:", player["health"])
    print("Credits:", player["credits"])


def explore():
    print("\nYou leave the ship and begin exploring...")

    events = [
        "You find an abandoned supply crate!",
        "A space pirate attacks you!",
        "You discover an old research station!",
        "You find a strange alien plant.",
        "You find absolutely nothing."
    ]

    event = random.choice(events)

    print("\n" + event)

    if event == "You find an abandoned supply crate!":
        player["credits"] += 25
        print("You found 25 credits!")

    elif event == "A space pirate attacks you!":
        damage = random.randint(10, 30)
        player["health"] -= damage
        print("You take", damage, "damage!")

    elif event == "You discover an old research station!":
        player["credits"] += 50
        print("You found 50 credits!")

    elif event == "You find a strange alien plant.":
        player["health"] += 10
        print("The plant restores 10 health!")


def repair_ship():
    if player["credits"] >= 30:
        player["credits"] -= 30
        print("\nYou spend 30 credits repairing the ship.")
        print("The ship is looking better!")

    else:
        print("\nYou don't have enough credits.")


# -------------------------
# GAME LOOP
# -------------------------

print("================================")
print("      SPACE SURVIVAL")
print("================================")

player["name"] = input("What is your name, Captain? ")

while player["health"] > 0:

    show_status()

    print("\nWhat would you like to do?")
    print("1. Explore")
    print("2. Repair ship")
    print("3. Quit")

    choice = input("\nChoose an action: ")

    if choice == "1":
        explore()

    elif choice == "2":
        repair_ship()

    elif choice == "3":
        print("\nYou return to the ship.")
        break

    else:
        print("\nThat's not a valid choice!")

print("\nGAME OVER")
print("Thanks for playing!")