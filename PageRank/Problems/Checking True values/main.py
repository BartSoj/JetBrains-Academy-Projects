import numpy as np

a = int(input())
b = int(input())
c = int(input())
print(np.all(np.array([a, b, c]) > 15))
