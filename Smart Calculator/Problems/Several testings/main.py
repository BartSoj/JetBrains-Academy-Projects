def check(x):
    if not x.isnumeric():
        print("It is not a number!")
        return
    x = int(x)
    if 202 <= x:
        print(x)
    else:
        print("There are less than 202 apples! You cheated on me!")
