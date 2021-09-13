import numpy as np

a1 = np.array([[int(input()), int(input())], [int(input()), int(input())]])
a2 = np.array([int(input()), int(input())])
print(a1.T - a2)
