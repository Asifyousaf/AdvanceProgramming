# Chapter 1 Exercise 13 - Product of list items

# making a random list
my_list = [2, 3, 5, 7, 11,66]

def calculate_product(input_list):
    # Initialize the product to 1 so can multiply
    product = 1
    
    # to Calculate the product of values in the list
    for value in input_list:
        product *= value
    
    # Return the calculated product
    return product

# Printing the result
print("Product of the list values:", calculate_product(my_list))

# End marker