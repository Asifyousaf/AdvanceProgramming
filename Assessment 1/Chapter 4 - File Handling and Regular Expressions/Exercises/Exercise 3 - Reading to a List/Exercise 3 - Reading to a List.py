# Read numbers from the file and output them as integers

# Open and read the numbers from the file
with open('numbers.txt', 'r') as file:
    # Read each line, convert to integer, and store in a list
    numbers_list = [int(line.strip()) for line in file]

# Output the numbers in integer format
print("Numbers in integer format:")
for num in numbers_list:
    print(num)
