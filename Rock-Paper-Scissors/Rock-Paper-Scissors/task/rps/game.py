from random import choice


def get_username():
    name = input("Enter your name: ")
    print("Hello, {}".format(name))
    return name


def get_rating():
    rating = 0
    rating_file = open("rating.txt")
    for line in rating_file:
        if line.startswith(user_name):
            rating = int(line[line.rindex(" "):])
            break
    rating_file.close()
    return rating


def get_options():
    options_input = input()
    print("Okay, let's start")
    return options_input.split(",") if options_input else ["rock", "paper", "scissors"]


def print_rating():
    print("Your rating: {}".format(user_rating))


def determine_winner(user_option, computer_option):
    if user_option == computer_option:
        return "draw"
    computer_option_index = options.index(computer_option)
    determine_options = options[computer_option_index + 1:] + options[:computer_option_index]
    if determine_options.index(user_option) < len(determine_options) // 2:
        return "user"
    else:
        return "computer"


def play(user_option):
    global user_rating
    computer_option = choice(options)
    result = determine_winner(user_option, computer_option)
    if result == "user":
        user_rating += 100
        print('Well done. The computer chose {} and failed'.format(computer_option))
    elif result == "computer":
        print("Sorry, but the computer chose {}".format(computer_option))
    else:
        user_rating += 50
        print("There is a draw ({})".format(computer_option))


user_name = get_username()
user_rating = get_rating()
options = get_options()
while True:
    user_input = input()
    if user_input == "!exit":
        break
    elif user_input == "!rating":
        print_rating()
    elif user_input in options:
        play(user_input)
    else:
        print("invalid input")
print("Bye!")
