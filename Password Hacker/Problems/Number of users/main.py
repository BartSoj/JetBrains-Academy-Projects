import json

with open("users.json", "r") as f:
    users = json.load(f)

print(len(users["users"]))
