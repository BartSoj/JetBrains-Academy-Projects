nums = input().split()
x = input()
found = [str(i) for i, num in enumerate(nums) if num == x]
print(" ".join(found) if found else "not found")
