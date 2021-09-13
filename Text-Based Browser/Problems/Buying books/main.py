from collections import deque

n = int(input())
books = deque()
readed_books = deque()
for _ in range(n):
    data = input()
    if data.startswith("BUY"):
        books.append(data.lstrip("BUY "))
    else:
        readed_books.append(books.pop())

for book in readed_books:
    print(book)
