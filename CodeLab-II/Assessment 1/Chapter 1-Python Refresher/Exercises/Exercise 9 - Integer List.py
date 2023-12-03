# Creating an integer list with 10 values
integer_list = [5, 79, 8, 1, 7, 3, 12, 4, 9, 6]

# Output the list using a for loop
print("Original List:")
for i in integer_list:
    print(i, end=" ")
print()

# the highest and lowest value
print("Highest Value is:", max(integer_list))
print("Lowest Value is:", min(integer_list))

# Sorting the elements in ascending order
integer_list.sort()
print("Sorted List Ascending:", integer_list)

# Sorting the elements in descending order
integer_list.sort(reverse=True)
print("Sorted List Descending:", integer_list)

# Appending two elements
integer_list.append(91)
integer_list.append(0)

# Printin the list after appending
print("List after Appending:", integer_list)
