prime_numbers = []
for num in range(2, 1000):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        prime_numbers.append(num)
