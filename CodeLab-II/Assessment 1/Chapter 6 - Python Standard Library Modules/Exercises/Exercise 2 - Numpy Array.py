import numpy as np

# Given list
a = [20, 23, 82, 40, 32, 15, 67, 52]

# Convert the list to a NumPy array
a = np.array(a)

# Find the indices of even numbers
even_indices = np.where(a % 2 == 0)
print("Indices of even numbers:", even_indices[0])

# Sort the list
sorted_list = sorted(a)
print("Sorted list:", sorted_list)

# Slice elements from index 3 to the end of the list, Here a[start:stop], here start = 5, stop = 0
slice1 = a[3:]
print("Slice from index 3 to the end:", slice1)

# Slice elements from index 0 to index 4, Here a[start:stop], here start = 0, stop = 5
slice2 = a[:5]
print("Slice from index 0 to index 4:", slice2)

# Print [32 15 67] using negative slicing, Here a[start:stop], here start = -5, stop = -2
negative_slice = a[-5:-2]
print("Negative slice:", negative_slice)

# End marker