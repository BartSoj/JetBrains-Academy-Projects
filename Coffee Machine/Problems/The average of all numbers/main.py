a = int(input())
b = int(input())
sum_of_numbers = 0
n = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        n += 1
        sum_of_numbers += i
print(sum_of_numbers / n)
