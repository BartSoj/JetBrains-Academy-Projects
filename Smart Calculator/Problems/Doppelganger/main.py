import collections

sum = 0
for i, val in enumerate(object_list):
    if isinstance(val, collections.Hashable) and val in (object_list[:i] + object_list[i + 1:]):
        sum += 1

print(sum)