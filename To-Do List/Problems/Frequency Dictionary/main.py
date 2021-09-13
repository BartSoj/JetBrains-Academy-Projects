words = {}
for word in input().lower().split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

for key, value in words.items():
    print(key, value)
