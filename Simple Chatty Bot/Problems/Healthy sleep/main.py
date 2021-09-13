a = int(input())
b = int(input())
h = int(input())
if h < a:
    print("Deficiency")
else:
    if h > b:
        print("Excess")
    else:
        print("Normal")
