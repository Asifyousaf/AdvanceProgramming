# using the time module
import time

# Burger Shack
print(" **WELCOME TO BURGER SHACK** ")

# Defining the prices of each burger
Beef_Burger = 10.00
Chicken_Burger = 8.00
Vegetarian_Burger = 6.50

time.sleep(1)
print("\nThere are 3 delicious burgers to choose from:\n")
time.sleep(2)

# Displaying various options and the pricing for each burger to the user.
print(" Burger                    Costs\n"
" ------                    ------\n"
" 1. Beef Burger            10.00 Dhs\n "
" 2. Chicken Burger          8.00 Dhs\n "
" 3. Vegetarian Burger       6.50 Dhs\n "
"-------------------------------------\n"
)

time.sleep(1)

while True:
    try:
        # Getting the user's input
        money = int(input("Please Enter The Amount of Money: "))
        break
    except ValueError:
        # Displaying an error message if the input is not a valid integer
        print("Sorry, that is not a valid amount. Please enter a whole number (e.g. 10, 100, 1000).")

# Printing line to separate
print("-" * 40)
time.sleep(1)
print("The amount of money you have entered is: " + str(money) + " Dhs")
print("-" * 40)
time.sleep(1)

# To store the items selected by the user
transactions = []

# Function to store the transaction history
def vend(item, price, quantity, total_cost):
    # Calculate the total cost of the purchase
    total_cost = price * quantity
    # Adding the transaction to the history
    transactions.append((item, price, quantity, total_cost))

def get_transaction_history():
    # Returning the transaction history
    return transactions


# Loop until the user has no more money or chooses to exit
while money > 0:
    while True:
        try:
            burger_choice = int(input("\nPlease enter your choice (Once you are finish type 0 to Quit): "))
            if burger_choice in [0, 1, 2, 3]:
                break
            else:
                print("Sorry, that is not a valid option. Please select a number between 1 and 3.")
        except ValueError:
            print("Sorry, that is not a valid option. Please enter a number between 1 and 3.")

    # To Check which burger the user has chosen
    if burger_choice == 0:
        break
    elif burger_choice == 1:
        burger_type = "Beef Burger"
        burger_price = Beef_Burger
    elif burger_choice == 2:
        burger_type = "Chicken Burger"
        burger_price = Chicken_Burger
    elif burger_choice == 3:
        burger_type = "Vegetarian Burger"
        burger_price = Vegetarian_Burger

    # To Check if the user has enough money for the chosen burger
    if money < burger_price:
        print(f"Insufficient funds to purchase {burger_type}")
    else:
        time.sleep(1)
        print(f"\nYou have selected {burger_type}")
        # Loop until the user enters a valid quantity
        while True:
            try:
                # Prompt the user to specify the quantity of burgers they want
                quantity = int(input(f"How many {burger_type}s would you like to purchase? "))
                total_cost = burger_price * quantity

                # Checking if the total cost of the purchase is greater than the user's balance
                if total_cost > money:
                    print("You do not have enough money to make this purchase. Please enter a lower quantity.")
                else:
                    # Calculating the total cost of the purchase
                    money = money - total_cost
                    # Adding the purchase to the transaction history
                    vend(burger_type, burger_price, quantity, total_cost)
                    print(
                        f"Thank you for your purchase! Your remaining balance is: {money} Dhs"
                    )
                    # Printing line to separate
                    print("-" * 40)
                    # Break out of the loop
                    break
            except ValueError:
                print("Sorry, that is not a valid option. Please enter a number.")

        # Offer additional items to add to the purchase
        print("\nWould you like to customize your burger with toppings and condiments?")
        print("1. Add Toppings")
        print("2. Add Condiments")
        print("3. Skip customization")

        while True:
            try:
                customization_choice = int(input("Enter your choice (1-3): "))
                if customization_choice in [1, 2, 3]:
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if customization_choice == 1:
            # Adding toppings
            print("\nAvailable Toppings:")
            print("1. Cheese (1.50 Dhs)")
            print("2. Peanut Butter (1.00 Dhs)")
            print("3. Avocado (2.00 Dhs)")

            while True:
                try:
                    topping_choice = int(input("Select a topping (1-3): "))
                    if 1 <= topping_choice <= 3:
                        toppings = ["Cheese", "Peanut Butter", "Avocado"]
                        selected_topping = toppings[topping_choice - 1]
                        topping_price = {"Cheese": 1.50, "Peanut Butter": 1.00, "Avocado": 2.00}[selected_topping]
                        
                        # Adding the selected topping to the burger
                        money -= topping_price
                        print(f"{selected_topping} added to your burger. Remaining balance: {money} Dhs")
                        vend(selected_topping, topping_price, 1, topping_price)
                        
                        break
                    else:
                        print("Invalid choice. Please select a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif customization_choice == 2:
            # Adding condiments
            print("\nAvailable Condiments:")
            print("1. Ketchup (0.50 Dhs)")
            print("2. Mayonnaise (0.75 Dhs)")
            print("3. BBQ Sauce (1.00 Dhs)")

            while True:
                try:
                    condiment_choice = int(input("Select a condiment (1-3): "))
                    if 1 <= condiment_choice <= 3:
                        condiments = ["Ketchup", "Mayonnaise", "BBQ Sauce"]
                        selected_condiment = condiments[condiment_choice - 1]
                        condiment_price = {"Ketchup": 0.50, "Mayonnaise": 0.75, "BBQ Sauce": 1.00}[selected_condiment]
                        
                        # Adding the selected condiment to the burger
                        money -= condiment_price
                        print(f"{selected_condiment} added to your burger. Remaining balance: {money} Dhs")
                        vend(selected_condiment, condiment_price, 1, condiment_price)
                        
                        break
                    else:
                        print("Invalid choice. Please select a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        # Adding sides
        print("\nAvailable Sides:")
        print("1. Fries (3.00 Dhs)")
        print("2. Drink (2.50 Dhs)")

        while True:
            try:
                side_choice = int(input("Select a side (1-2): "))
                if 1 <= side_choice <= 2:
                    sides = ["Fries", "Drink"]
                    selected_side = sides[side_choice - 1]
                    side_price = {"Fries": 3.00, "Drink": 2.50}[selected_side]
                    
                    # Adding the selected side to the order
                    money -= side_price
                    print(f"{selected_side} added to your order. Remaining balance: {money} Dhs")
                    vend(selected_side, side_price, 1, side_price)
                    
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    time.sleep(1)
    # Asking the user if they want to make an additional selection
    additional_selection = input('Would you like to make another purchase? (y/n): ')
    if additional_selection.lower() == 'no' or additional_selection.lower() == 'n':
        break
    else:
      continue

# Displaying the transaction history and total
print("\n-----\033[92mTransaction History\033[0m-----")
history = get_transaction_history()
total = 0

for item, price, quantity, total_cost in history:
    total += total_cost
    print(f"\n{item}: {price} Dhs x {quantity} = {total_cost} Dhs")

print(f"\nTotal: {total} Dhs ")
print(f"\nRemaining balance: {money} Dhs")
print("\nEnjoy your meal at Burger Shack!")

# end marker