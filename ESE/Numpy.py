# Q18: Indexing and Slicing in NumPy

import numpy as np

# Create a 1D NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Indexing
print("Element at index 2:", arr[2])

# Slicing
print("Slice from index 1 to 4:", arr[1:4])
print("Every second element:", arr[::2])

# 2D Array indexing/slicing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Element at (1,2):", arr2d[1, 2])
print("First two rows:\n", arr2d[:2])
print("Last column:\n", arr2d[:, -1])