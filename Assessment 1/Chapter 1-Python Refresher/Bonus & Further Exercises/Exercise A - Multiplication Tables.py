# Chapter 1 Bonus Exercise A - Multiplication Tables

# Outer loop for tables from 1 to 10
for i in range(1, 11):
    print(f"Multiplication table of : {i}")
    
    # Inner loop for multiplying numbers from 1 to 10
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")

    # Print a separator line between tables
    print("-" * 20)

# End marker