import numpy as np

array = np.array([[-34, 2, 0],
                  [0, -4, 123],
                  [-201, 0, -3]], dtype=np.int64)

print(array[int(input())].astype(np.str_))
print(array[int(input())].astype(np.float64))
