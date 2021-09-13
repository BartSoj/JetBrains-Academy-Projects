import random
from string import ascii_lowercase


def game():
    word_list = ("python", "java", "kotlin", "javascript")
    answer = random.choice(word_list)
    user_letters = set()

    word = "-" * len(answer)
    tries = 8
    while tries > 0:
        print("\n" + word)

        user_letter = input("Input a letter: ")
        if len(user_letter) != 1:
            print("You should input a single letter")
        elif user_letter not in ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        elif user_letter in user_letters:
            print("You already typed this letter")
        elif user_letter not in answer:
            print("TNo such letter in the word")
            tries -= 1

        user_letters.add(user_letter)
        word = list()
        for answer_letter in answer:
            if answer_letter in user_letters:
                word.append(answer_letter)
            else:
                word.append("-")
        word = "".join(word)

        if word == answer:
            break

    if word == answer:
        print(word)
        print("You guessed the word!\nYou survived!\n")
    else:
        print("You lost!\n")


print("H A N G M A N")
option = ""
while option != "exit":
    option = input('Type "play" to play the game, "exit" to quit: ')
    if option == "play":
        game()
