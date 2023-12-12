# Chapter 1 Exercise 3 - Is it Triangle

# Asking user for lengths of the three sides
side_a = float(input("Enter the length of the first side: "))
side_b = float(input("Enter the length of the second side: "))
side_c = float(input("Enter the length of the third side: "))

# Checking the triangle inequality to determine if its a valid triangle
if side_a + side_b >= side_c and side_a + side_c >= side_b and side_b + side_c >= side_a:
    print("It is a valid triangle")
else:
    print("It is not a valid triangle")

# Checking all sides if equal it is Equilateral
if side_a == side_b == side_c:
    print(" The triangle is Equilateral")

    # Checking all sides if any one is equal it is Isosceles
elif side_a == side_b or side_a == side_c or side_b == side_c:
    print("The triangle is Isosceles")

    # if none of the side is equal then it is scalene 
else:
    print("The triangle is scalene")