while True:
    input_number = int(input())
    if input_number < 10:
        continue
    if input_number > 100:
        break
    print(input_number)
