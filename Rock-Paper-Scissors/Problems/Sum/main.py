file = open("sums.txt")
for line in file:
    a, b = line.split(" ")
    print(int(a) + int(b))
file.close()
