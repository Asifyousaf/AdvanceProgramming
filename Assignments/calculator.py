# Declaring a varible namd (first) to egt user to choose a shape 
shape_choice = int(input("Which shape's are do you want \n 1.Circle \n 2.triangle \n 3.Rectangle : \n"))

# Using if statements to check user's shape choice from the 3 options

if shape_choice == 1: # if they choose circle
    # Again using if statement to ask what they want to calculate of the circle
    choice1 = int(input("You want to calculate \n 1. Area \n 2. cicumference: \n"))

    if choice1 == 1: # if they want to calculate area
         radius = float(input("write the radius: "))
         Area = (3.14*radius**2)
         print(Area, "is the area of th circle")

    elif choice1 == 2:# if they want to calculate the circum
         radius = float(input("write the radius: "))
         circum = (2*radius*3.14)
         print(circum, "is the circum of th circle")

    else:     # if user input's a invalid choice there will be an error
         print("invalid choice")

elif shape_choice == 2: # if they choose triangle
    # Again using if statement to ask what they want to calculate of the triangle
    choice2 = int(input("You want to calculate \n 1. Area \n 2. circumference: \n"))

    if choice2 == 1: # if they want to calculate the area
         base = float(input("what's the base of the triangle: "))
         height = float(input("what's the base of the height: "))
         area = (1/2*base*height)
         print(area, "is the area of triangle") 

    elif choice2 == 2: # if they want to calculate the volume
        vol1 = float(input("what's the side 1 of the triangle: "))
        vol2 = float(input("what's the side 2 of the triangle: "))
        vol3 = float(input("what's the side 3 of the triangle: "))
        vol = (vol1+vol2+vol3)
        print(vol ,"Is the volume of triangle ")

    else:
         print("invalid choice")
elif shape_choice == 3: # if they choose rectangle
    # Again using if statement to ask what they want to calculate of the rectangle
    choice3 = int(input("You want to calculate \n 1. Area \n 2. circumference: \n"))
    if choice3 == 1: # if they want to calculate the area
        length =float(input("what's the lenght: "))
        width = float(input("what's the width: "))
        area = (length*width)
        print(area ,"is the area of rectangle")

    elif choice3 == 2: # if they want to calculate the circum
        length =float(input("what's the lenght: "))
        width = float(input("what's the width: "))
        circum = (2*length*+2*width)
        print(circum ,"is the area of rectangle")

    else: # if user input's a invalid choice there will be an error
         print("invalid choice")