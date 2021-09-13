file = open("animals.txt", "r")
new_file = open("animals_new.txt", "w")

for line in file:
    new_file.write(line.rstrip("\n") + " ")

file.close()
new_file.close()
