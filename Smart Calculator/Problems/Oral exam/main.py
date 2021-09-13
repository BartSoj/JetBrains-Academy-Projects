from collections import deque

n = int(input())
queue = deque()
for _ in range(n):
    inp = input()
    if inp.startswith("READY"):
        queue.appendleft(inp.split()[1])
    elif inp.startswith("EXTRA"):
        it = queue.pop()
        queue.appendleft(it)
    else:
        print(queue.pop())
