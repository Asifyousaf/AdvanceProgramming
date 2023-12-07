from tkinter import *

def analyze_petrol_data():
    try:
        file_path = 'Chapter 4 - File Handling and Regular Expressions/Bonus & Further Exercises/Exercise A - Petrol Price/petrolPrice.txt'
        total_liters = 0
        total_cost = 0
        under_3_5_liters = 0

        # Read the data from the file and process each line
        with open(file_path, 'r') as file:
            # Skip the header line
            next(file)

            for line in file:
                # Split the line into columns
                columns = line.strip().split('\t')

                # Extract liters and cost from the columns
                liters, cost = float(columns[0]), float(columns[1])

                # Accumulate totals
                total_liters += liters
                total_cost += cost

                # Check if the cost per liter is under 3.5AED
                if liters > 0 and cost / liters < 3.5:
                    under_3_5_liters += liters

        # Calculate average cost per liter
        average_cost_per_liter = total_cost / total_liters if total_liters > 0 else 0

        # Display statistics
        result_text = f"Statistics:\nTotal Liters: {total_liters}\nTotal Cost: {total_cost}\n"
        result_text += f"Average Cost per Liter: {average_cost_per_liter:.2f}\n"
        result_text += f"Liters bought at under 3.5AED per liter: {under_3_5_liters}"
        result_label.config(text=result_text)

    except FileNotFoundError:
        result_label.config(text="File not found. Please make sure the file exists.")

# Creating the main window
root = Tk()
root.title("Petrol Data Analyzer")

# Label for displaying the result
result_label = Label(root, text="")
result_label.pack(pady=10)

# Button to analyze the petrol data
analyze_button = Button(root, text="Analyze Petrol Data", command=analyze_petrol_data)
analyze_button.pack(pady=10)

# Run the main event loop
root.mainloop()
