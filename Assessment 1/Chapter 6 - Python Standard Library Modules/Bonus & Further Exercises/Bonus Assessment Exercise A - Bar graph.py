# Chapter 6 Bonus Exercise A - Bar Grapgh

# Import the pyplot module from the matplotlib library for graph
import matplotlib.pyplot as plt

# Information for the bar graph
title = "Most valuable brands worldwide in 2023 (in billion U.S. dollars)"
brands = ["Amazon", "Apple", "Google", "Microsoft", "Walmart", "Samsung Group", "ICBC", "Verizon", "Tesla", "TikTok/Douyin"]
values = [299.28, 297.51, 281.38, 191.57, 113.78, 99.66, 69.55, 67.44, 66.21, 65.67] # Given Data

# Plotting the bar graph
plt.bar(brands, values, color='skyblue')  # Create a bar graph with brands on the x-axis and values on the y-axis
plt.xlabel('Brands')  # Label for the x-axis
plt.ylabel('Brand Value (in billion U.S. dollars)')  # Label for the y-axis
plt.title(title)  # Title of the plot
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels

# Display the bar graph
plt.show()

# End marker