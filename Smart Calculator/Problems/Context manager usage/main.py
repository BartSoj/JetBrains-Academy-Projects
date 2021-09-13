import shelve

with shelve.open("my_library", flag="c") as lib:
    lib["anna Karenina"] = "Happy families are all alike; every unhappy family is unhappy in its own way..."
    print("A new book has been added to the library!")
