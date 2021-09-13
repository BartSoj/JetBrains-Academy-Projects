from random import random
import sqlite3

conn = sqlite3.connect('card.s3db')


def get_luhn_algorithm_number(initial_number):
    sum_digits = 0
    for i, num in enumerate(initial_number):
        num = int(num)
        if i % 2 == 0:
            num *= 2
        if num > 9:
            num -= 9
        sum_digits += num
    return initial_number + str(sum_digits * 9 % 10)


class Card:
    cards_number = 0

    def __init__(self, bin):
        self.id = Card.cards_number
        self.number = get_luhn_algorithm_number(bin + str(self.id).zfill(9))
        self.pin = str(int(random() * 10000)).zfill(4)
        self.balance = 0
        self.logged_in = False
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO card VALUES ({self.id}, {self.number}, {self.pin}, {self.balance})")
        conn.commit()
        Card.cards_number += 1

    def check_card(self, card_number, card_pin):
        return self.number == card_number and self.pin == card_pin

    def log_in(self):
        self.logged_in = True

    def log_out(self):
        self.logged_in = False

    def add_income(self):
        print("Enter income:")
        income = int(input())
        print("Income was added")
        self.balance += income
        cursor = conn.cursor()
        cursor.execute(f"UPDATE card SET balance = {self.balance} WHERE id = {self.id}")
        conn.commit()


class Bank:

    def __init__(self, bin):
        self.cards = []
        self.bin = bin

    def create_an_account(self):
        card = Card(self.bin)
        self.cards.append(card)
        print("Your card has been created")
        print("Your card number:")
        print(card.number)
        print("Your card PIN:")
        print(card.pin)

    def log_into_account(self):
        print("Enter your card number:")
        card_number = input()
        print("Enter your PIN:")
        card_pin = input()
        for card in self.cards:
            if card.check_card(card_number, card_pin):
                card.log_in()
                print("You have successfully logged in!")
                return card
        print("Wrong card number or PIN!")

    def do_transfer(self, card):
        print("Transfer")
        print("Enter card number:")
        number_to_transfer = input()
        card_to_transfer = None
        if card.number == number_to_transfer:
            print("You can't transfer money to the same account!")
            return
        elif get_luhn_algorithm_number(number_to_transfer[:-1]) != number_to_transfer:
            print("Probably you made a mistake in the card number. Please try again!")
            return
        for c in self.cards:
            if c.number == number_to_transfer:
                card_to_transfer = c
                break
        else:
            print("Such a card does not exist.")
            return
        print("Enter how much money you want to transfer:")
        money_to_transfer = int(input())
        if card.balance < money_to_transfer:
            print("Not enough money!")
            return
        card.balance -= money_to_transfer
        card_to_transfer.balance += money_to_transfer
        print("Success!")
        cursor = conn.cursor()
        cursor.execute(f"UPDATE card SET balance = {card.balance} WHERE id = {card.id}")
        conn.commit()
        cursor.execute(f"UPDATE card SET balance = {card_to_transfer.balance} WHERE id = {card_to_transfer.id}")
        conn.commit()

    def close_account(self, card):
        print("The account has been closed!")
        self.cards.remove(card)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM card WHERE id = {card.id}")
        conn.commit()


def init_db():
    cursor = conn.cursor()
    try:
        cursor.execute("DROP TABLE card")
    except sqlite3.OperationalError:
        pass
    cursor.execute(
        "CREATE TABLE card(id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)")
    conn.commit()


def start():
    init_db()
    bank = Bank("400000")
    card = None
    while True:
        if card:
            print("1. Balance")
            print("2. Add income")
            print("3. Do transfer")
            print("4. Close account")
            print("5. Log out")
            print("0. Exit")
            option = input()
            if option == "0":
                print("Bye!")
                break
            if option == "1":
                balance = card.balance
                print(f"Balance: {balance}")
            elif option == "2":
                card.add_income()
            elif option == "3":
                bank.do_transfer(card)
            elif option == "4":
                bank.close_account(card)
            elif option == "5":
                card = card.log_out()
                print("You have successfully logged out!")
            else:
                print("Invalid input")
        else:
            print("1. Create an account")
            print("2. Log into account")
            print("0. Exit")
            option = input()
            if option == "0":
                print("Bye!")
                break
            if option == "1":
                bank.create_an_account()
            elif option == "2":
                card = bank.log_into_account()
            else:
                print("Invalid input")


start()
