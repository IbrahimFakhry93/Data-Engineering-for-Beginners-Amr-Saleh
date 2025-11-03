import numpy as np

r = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("r", "\n", r, "\n")

r1 = np.insert(r, 2, [[11, 12, 13, 14]], axis=0)
print("r1", "\n", r1, "\n")
