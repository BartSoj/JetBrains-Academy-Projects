def fibonacci(n):
    a = 0
    b = 1
    yield a
    yield b
    for _ in range(n - 2):
        c = a + b
        a = b
        b = c
        yield c
