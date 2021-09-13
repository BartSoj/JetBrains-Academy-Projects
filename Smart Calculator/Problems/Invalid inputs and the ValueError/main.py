def check():
    try:
        x = int(input())
        assert 25 <= x <= 37
        print(x)
    except (ValueError, AssertionError):
        print("Correct the error!")
