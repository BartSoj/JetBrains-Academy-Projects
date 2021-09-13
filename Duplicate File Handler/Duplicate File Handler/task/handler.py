import os
import sys
import hashlib

sys_args = sys.argv

if len(sys_args) <= 1:
    print("Directory is not specified")
    exit()

root_dir = sys_args[1]
print("Enter file format:")
file_format = input()
if file_format:
    file_format = "." + file_format

while True:
    print("\nSize sorting options:\n1. Descending\n2. Ascending\n\nEnter a sorting option:")
    desc_input = input()
    if desc_input == "1" or desc_input == "2":
        desc = True if desc_input == "1" else False
        break
    else:
        print("\nWrong option")

files_dict = dict()

for root, _, files in os.walk(root_dir):
    for name in files:
        if name.endswith(file_format):
            file_path = rf"{root}\{name}"
            size = os.path.getsize(file_path)
            if size not in files_dict:
                files_dict[size] = dict()
            with open(file_path, "rb") as file:
                file_data = file.read()
            file_hash = hashlib.md5()
            file_hash.update(file_data)
            file_hash_hex = file_hash.hexdigest()
            if file_hash_hex not in files_dict[size]:
                files_dict[size][file_hash_hex] = []
            files_dict[size][file_hash_hex].append(file_path)

for size in sorted(files_dict.keys(), reverse=desc):
    print(f"\n{size} bytes")
    for names in files_dict[size].values():
        for name in names:
            print(name)

print("\nCheck for duplicates?")
while True:
    duplicate_check = input()
    if duplicate_check == "yes":
        break
    elif duplicate_check == "no":
        exit()
    else:
        print("\nWrong option")

i = 1
file_duplicates = []
for size in sorted(files_dict.keys(), reverse=desc):
    hash_duplicates = {file_hash: file_list for file_hash, file_list in files_dict[size].items() if len(file_list) > 1}
    if len(hash_duplicates) < 1:
        continue
    print(f"\n{size} bytes")
    for file_hash, names in hash_duplicates.items():
        print("Hash:", file_hash)
        for name in names:
            print(f"{i}. {name}")
            file_duplicates.append(name)
            i += 1

print("\nDelete files?")
while True:
    duplicate_check = input()
    if duplicate_check == "yes":
        break
    elif duplicate_check == "no":
        exit()
    else:
        print("\nWrong option")

while True:
    print("\nEnter file numbers to delete:")
    try:
        file_numbers = [int(num) - 1 for num in input().split()]
    except ValueError:
        file_numbers = []
    if 0 < len(file_numbers) <= 5 and min(file_numbers) >= 0 and max(file_numbers) < len(file_duplicates):
        break
    else:
        print("\nWrong format")

total_space = 0
for file_number in file_numbers:
    total_space += os.path.getsize(file_duplicates[file_number])
    os.remove(file_duplicates[file_number])

print("\nTotal freed up space:", total_space, "bytes")
