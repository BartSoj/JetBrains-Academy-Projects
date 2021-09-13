import collections

n = int(input())
queue = collections.deque()
for _ in range(n):
    inp = input()
    if inp.startswith("ISSUE"):
        queue.appendleft(inp.split()[1])
    else:
        queue.pop()
for _ in range(len(queue)):
    print(queue.pop())
