import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(np.linalg.svd(np.array([[a, b], [c, d]])))
