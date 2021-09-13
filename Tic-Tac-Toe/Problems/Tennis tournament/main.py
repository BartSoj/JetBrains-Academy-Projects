n = int(input())
winners = []
for _ in range(n):
    line = input()
    data = line.split()
    if "win" in data:
        winners.append(data[0])

print(winners)
print(len(winners))
