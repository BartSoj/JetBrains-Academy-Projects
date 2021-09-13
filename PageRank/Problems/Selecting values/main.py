import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())
array = np.array([a, b, c, d])
spec = np.where(array >= 45)
print(array[spec])
