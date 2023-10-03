# Importing from library random to randomize the selection 
import random
#Assiging
Choices = ["Rock","Paper","Scissor"]

while True:
    # To ask user input and capitalize it
    User_input = input("Choose \n 1.Rock \n 2.Paper \n 3.Scissor or 'n' to quit: ").capitalize()
    # Break loop if user types "n"
    if User_input == "N":
        break
    #Checking if the input is valid 
    if User_input not in Choices:
        print("inavlid choice")
        continue
        
    # Using random to generate random choice for cpu_choice
    cpu_choice = random.choice(Choices)
    
    # Checking both user and cpu inputs 
    # logic involves comparing each choice with every other choice (i.e ROCK with paper and ROCK with scissor)
    if User_input == cpu_choice:
        print("\n Tie")
    
    elif (User_input == "Rock" and cpu_choice == "Scissor"):
        print("\n You win "+User_input +" beats "+ cpu_choice)

    elif (User_input == "Paper" and cpu_choice == "Rock"):
        print("\n You win "+User_input +" beats "+ cpu_choice)

    elif (User_input == "Scissor" and cpu_choice == "Paper"):
        print("\n You win "+User_input +" beats "+ cpu_choice)
    # if the user input not match so they lose 
    else:
        print("\n You lose "+cpu_choice+ " beats " +User_input)
    
    
    