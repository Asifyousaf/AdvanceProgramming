# Chapter 1 Exercise 6 - FizzBuzz

#  Loop to start numbers from 1 to 100
for number in range(1, 101):

    # Checking if the number is a multiple of both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    
     # Checking if the number is a multiple of 3
    elif number % 3 == 0:
        print("Fizz")

     # Checking if the number is a multiple of 3
    elif number % 5 == 0:
        print("Buzz")
    
     # if not the multiple of '3' and '5' just prints the number
    else:
        print(number)

# End marker