text = input()
words = text.split()
for word in words:
    if "https://" in word.lower() or "http://" in word.lower() or "www." in word.lower():
        print(word)
