import numpy as np

a = np.array([1, 2, 3, 4, 5], dtype=float)
print(a + 2)  # [3. 4. 5. 6. 7.]
print(a - 1)  # [0. 1. 2. 3. 4.]

print("---------------------------------------")

a = np.array([[1, 2, 3],
              [0, 1, 2]])

b = np.array([[ 1, 2],
              [ 0, 4],
              [-1, 0]])

c = np.dot(a, b)
print(c)