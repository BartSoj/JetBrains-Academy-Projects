from collections import namedtuple

template = namedtuple("Student", ["name", "age", "department"])
print(template("Alina", "22", "linguistics"))
print(template("Alex", "25", "programming"))
print(template("Kate", "19", "art"))
