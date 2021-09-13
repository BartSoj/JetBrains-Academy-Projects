input_number = input()
sum = 0
n = 0
while input_number != ".":
    sum += int(input_number)
    n += 1
    input_number = input()
print(sum / n)
