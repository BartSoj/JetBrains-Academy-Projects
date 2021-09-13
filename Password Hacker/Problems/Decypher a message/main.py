msg = input()
key = int(input())
key_bytes = key.to_bytes(2, 'little')
key_sum = sum(key_bytes)
for l in msg:
    print(chr(ord(l) + key_sum), end="")
