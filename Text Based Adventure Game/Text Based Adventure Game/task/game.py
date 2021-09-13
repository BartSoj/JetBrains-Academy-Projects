import random
import os

with open("story/choices.txt") as file:
    choices = file.read().splitlines()
with open("story/outcomes.txt") as file:
    outcomes = file.read().split("*\n")
with open("story/story.txt") as file:
    story = file.read().split("+\n")

new_outcomes = []
for outcome in outcomes:
    if outcome.endswith("option2)\n"):
        outcome = outcome.replace(" option2", "")
        new_outcomes[-1].append(outcome)
    else:
        outcome = outcome.replace(" option1", "")
        new_outcomes.append([outcome])

outcomes = new_outcomes


def start():
    while True:
        print("""***Welcome to the Journey to Mount Qaf*** 
    
1- Press key '1' or type 'start' to start a new game
2- Press key '2' or type 'load' to load your progress
3- Press key '3' or type 'quit' to quit the game""")
        option = input().lower()
        active_user = -1
        users = []
        if option == '1' or option == 'start':
            print("Starting a new game...")
            username = input("Enter a user name to save your progress or type '/b' to go back ").lower()
            if username == "/b":
                print("Going back to menu...\n")
            else:
                user = {"username": username, "choice": 0, "life": 5, "story": 0, "inventory": [], "level": 1}
                print("Create your character:")
                user["name"] = input("1- Name ").capitalize()
                user["species"] = input("2- Species ").capitalize()
                user["gender"] = input("3- Gender ").capitalize()
                print("Pack your bag for the journey:")
                user["snack"] = input("1- Favourite Snack ").capitalize()
                user["weapon"] = input("2- A weapon for the journey ").capitalize()
                user["tool"] = input("3- A traversal tool ").capitalize()
                user["inventory"].append(user["snack"])
                user["inventory"].append(user["weapon"])
                user["inventory"].append(user["tool"])
                print("""Choose your difficulty:
1- Easy
2- Medium
3- Hard""")
                difficulty_levels = {"1": "Easy", "easy": "Easy", "2": "Medium", "medium": "Medium", "3": "Hard",
                                     "hard": "Hard"}
                while True:
                    inp = input().lower()
                    if inp in difficulty_levels:
                        user["difficulty_level"] = difficulty_levels[inp]
                        break
                    print("Unknown input! Please enter a valid one")
                print(f"""Good luck on your journey!
Your character: {user["name"]}, {user["species"]}, {user["gender"]}
Your inventory: {user["snack"]}, {user["weapon"]}, {user["tool"]}
Difficulty: {user["difficulty_level"]}""")
                save_file(user)
                users.append(user)
                active_user += 1
        elif option == '2' or option == 'load':
            print("No save data found!")
        elif option == '3' or option == 'quit':
            print("Goodbye!")
            break
        else:
            print("Unknown input! Please enter a valid one.")
        if active_user != -1:
            user = users[active_user]
            while True:
                if user["life"] <= 0:
                    print("""The darkness said, "Wrong!" You try to run but it catches your legs and drags you to the darkness...
You died! Lives remaining:  0
You've run out of lives! Game over!""")
                    break
                if user["story"] == 4:
                    return
                print("What will you do? Type the number of the option or type '/h' to show help.")
                if user["choice"] == 18:
                    user["choice"] = 0
                print_replace("1- " + choices[user["choice"]], user)
                user["choice"] += 1
                print_replace("2- " + choices[user["choice"]], user)
                user["choice"] += 1
                print_replace("3- " + choices[user["choice"]], user)
                user["choice"] += 1
                option = input()
                if option == "/i":
                    print("Inventory: ", ", ".join(user["inventory"]))
                elif option == "/c":
                    print(f"""Your character: {user["name"]}, {user["species"]}, {user["gender"]}.
Lives remaining: {user["life"]}""")
                elif option == "/h":
                    print("""Type the number of the option you want to choose.
Commands you can use:
/i => Shows inventory.
/q => Exits the game.
/c => Shows the character traits.
/h => Shows help.""")
                elif option == "/q":
                    confirm = input('You sure you want to quit the game? Y/N').lower()
                    if confirm == "y":
                        print("Goodbye!")
                        return
                elif option == "1" or option == "2" or option == "3":
                    print_replace(random.choice(outcomes[user["choice"] - 4 + int(option)]), user)
                else:
                    print('Unknown input! Please enter a valid one')
                    user["choice"] -= 3


def print_replace(text, user):
    text = text.replace("{weapon}", user["weapon"])
    text = text.replace("{tool}", user["tool"])
    text = text.replace("{snack}", user["snack"])
    actions = text[text.find("("): text.find(")")][1:].split(" and ")
    for action in actions:
        if action == "life-1":
            user["life"] -= 1
            print("decreases the number of lives by 1")
        elif action == "life+1":
            user["life"] += 1
            print("increases the number of lives by 1")
        elif action.startswith("inventory-"):
            if (action.split("-")[-1]) in user["inventory"]:
                user["inventory"].remove(action.split("-")[-1])
                print("removes an item from the inventory")
        elif action.startswith("inventory+"):
            user["inventory"].append(action.split("+")[-1])
            print("adds a new item to the inventory")
        elif action == "move":
            user["story"] += 1
            print(story[user["story"]])
            if story[user["story"]].startswith("Level "):
                user["level"] += 1
                print("Goodbye!")
                save_file(user)
                return
        elif action == "repeat":
            user["choice"] -= 3
        elif action == "save":
            save_file(user)
        elif action == "game_won":
            pass
    text = text[:text.find("(")]
    print(text)


def save_file(user):
    if not os.path.exists("saves"):
        os.mkdir("saves")
    user_file = open(f'saves/{user["username"]}.txt', "w")
    user_file.write(f'{user["name"]}, {user["species"]}, {user["gender"]}\n')
    user_file.write(f'{user["snack"]}, {user["weapon"]}, {user["tool"]}\n')
    user_file.write(f'{user["difficulty_level"]} {user["life"]}\n')
    user_file.write(f'{user["level"]}')
    user_file.close()


start()
