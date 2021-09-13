amount = int(input())
final_amount = int(input())
days = 0
while amount > final_amount:
    days += 12
    amount //= 2
print(days)
