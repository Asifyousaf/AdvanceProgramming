# Chapter 1 Bonus Exercise B - Location List

# List of locations
locations = ['dubai', 'paris', 'switzerland', 'London', 'amsterdam', 'New York']

# Displaying the original list and its length
print(f"Original List: \n{locations}")
print(f"\nLength of the list: {len(locations)}")

# Sorting the list in alphabetical order using casefold for case insensitivity
sorted_locations = sorted(locations, key=str.casefold)
print(f"\nSorted List: \n{sorted_locations}")
print(f"Original list: \n{locations}")

# Reverse alphabetical sort and displaying the sorted list
sorted_locations = sorted(locations, key=str.casefold, reverse=True)
print(f"\nSorted Reverse List: \n{sorted_locations}")

# Reversing the original list and displaying it
locations.reverse()
print(f"\nReversed List: \n{locations}")

# Alphabetical sort using list.sort() method and displaying the sorted list
locations.sort(key=str.casefold)
print(f"\nAlphabetical order: \n{locations}")

# Reverse alphabetical sort using list.sort() method and displaying the sorted list
locations.sort(reverse=True, key=str.casefold)
print(f"\nReverse alphabetical:\n{locations}")

# End marker