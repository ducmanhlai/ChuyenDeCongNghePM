import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Get the indices of the top 10 elements
indices = np.argsort(arr)[-2:]

# Print the indices
print(indices)
