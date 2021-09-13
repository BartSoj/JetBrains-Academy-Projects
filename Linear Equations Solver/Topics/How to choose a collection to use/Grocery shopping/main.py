shopping_list = input().split()
shopping_dict = dict()
for item in shopping_list:
    shopping_dict.setdefault(item, 0)
    shopping_dict[item] += 1

print("\n".join([" ".join((str(value), key)) for key, value in shopping_dict.items()]))
