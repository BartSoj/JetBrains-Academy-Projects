# the following line creates a list from the input, do not modify it, please
prices = [float(price) for price in input().split()]

prices.sort()
prices.reverse()
print(prices)
