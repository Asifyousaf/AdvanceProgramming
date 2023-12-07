def display_menu():
    print("Welcome to Burger Shack!")
    print("1. Beef Burger")
    print("2. Chicken Burger")
    print("3. Vegetarian Burger")

def choose_burger():
    burger_type = input("Choose a burger (1-3): ")
    while burger_type not in ["1", "2", "3"]:
        print("Invalid choice. Please choose a valid option.")
        burger_type = input("Choose a burger (1-3): ")
    return int(burger_type)

def choose_toppings():
    toppings = []
    print("\nChoose toppings (comma-separated):")
    print("1. Cheese")
    print("2. Peanut Butter")
    print("3. Avocado")
    
    selected_toppings = input("Enter topping numbers: ")
    topping_choices = selected_toppings.split(",")
    for choice in topping_choices:
        if choice == "1":
            toppings.append("Cheese")
        elif choice == "2":
            toppings.append("Peanut Butter")
        elif choice == "3":
            toppings.append("Avocado")
    return toppings

def choose_condiments():
    condiments = []
    print("\nChoose condiments (comma-separated):")
    print("1. Ketchup")
    print("2. Mayonnaise")
    print("3. BBQ Sauce")
    
    selected_condiments = input("Enter condiment numbers: ")
    condiment_choices = selected_condiments.split(",")
    for choice in condiment_choices:
        if choice == "1":
            condiments.append("Ketchup")
        elif choice == "2":
            condiments.append("Mayonnaise")
        elif choice == "3":
            condiments.append("BBQ Sauce")
    return condiments

def choose_sides():
    print("\nChoose sides:")
    print("1. Fries")
    print("2. Drink")
    
    selected_sides = input("Enter side numbers: ")
    sides = []
    side_choices = selected_sides.split(",")
    for choice in side_choices:
        if choice == "1":
            sides.append("Fries")
        elif choice == "2":
            sides.append("Drink")
    return sides

def calculate_total(items):
    prices = {"Beef Burger": 5.00, "Chicken Burger": 4.50, "Vegetarian Burger": 4.00,
              "Cheese": 0.50, "Peanut Butter": 0.75, "Avocado": 1.00,
              "Ketchup": 0.25, "Mayonnaise": 0.30, "BBQ Sauce": 0.50,
              "Fries": 2.00, "Drink": 1.50}

    total = sum(prices[item] for item in items)
    return total

def handle_payment(total):
    print(f"\nYour total is ${total:.2f}")
    payment = float(input("Enter payment amount: $"))
    while payment < total:
        print("Insufficient payment. Please enter a valid amount.")
        payment = float(input("Enter payment amount: $"))

    change = payment - total
    print(f"Thank you for your payment! Your change is ${change:.2f}")

if __name__ == "__main__":
    order_items = []

    display_menu()

    burger_choice = choose_burger()
    order_items.append(["Beef Burger", "Chicken Burger", "Vegetarian Burger"][burger_choice - 1])

    toppings = choose_toppings()
    order_items.extend(toppings)

    condiments = choose_condiments()
    order_items.extend(condiments)

    sides = choose_sides()
    order_items.extend(sides)

    total_price = calculate_total(order_items)

    handle_payment(total_price)

    print("\nYour order:")
    for item in order_items:
        print(f"- {item}")

    print(f"\nTotal: ${total_price:.2f}")
