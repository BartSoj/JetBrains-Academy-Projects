brackets = 0
for char in input():
    if brackets < 0:
        break
    elif char == "(":
        brackets += 1
    elif char == ")":
        brackets -= 1

print("OK" if brackets == 0 else "ERROR")
