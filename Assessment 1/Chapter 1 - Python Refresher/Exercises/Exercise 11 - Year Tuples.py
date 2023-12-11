# Given tuple values
year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)
 
# Accessing the value at index -3
value_index_3 = year[-3]
print(f"Value at index -3: {value_index_3}")

# Reversing the tuple using slicing [start:stop:step]
reversed_year = year[::-1]

print(f"Original Tuple: {year}")
print(f"Reversed Tuple: {reversed_year}")

# Counting the number of times 2009 is in the tuple using a loop
count_2009 = 0
for value in year:
    if value == 2009:
        count_2009 += 1

# Get the index value of 2018
value_index = year.index(2018)
print(f"Index value of 2018: {value_index}")

# Find the length of the given tuple
tuple_length = len(year)
print(f"Length of the tuple: {tuple_length}")

