# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

groups_dict = dict.fromkeys(groups)
n = int(input())
for num in [int(input()) for _ in range(n)]:
    groups_dict[groups.pop(0)] = num

print(groups_dict)
