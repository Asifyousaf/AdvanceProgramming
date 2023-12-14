# Chapter 5 Further Exercise I - Stack Bar Graph

# Import the pyplot module from the matplotlib library for graph
import matplotlib.pyplot as plt

# Define data from the table
categories = ['Game', 'Commercials', "Wont'watch"]
male_responses = [279, 81, 132]
female_responses = [200, 156, 160]

# Plotting the bar chart
plt.bar(categories, male_responses, label='Male')  # Plotting bars for male responses

# Plotting bars for female responses on top of male responses
plt.bar(categories, female_responses, bottom=male_responses, label='Female') 

# Adding labels, title, and legend
plt.xlabel('Response Categories')  # Label for the x-axis
plt.ylabel('Number of Responses')  # Label for the y-axis
plt.title('Super Bowl Watching Preferences by Gender')  # Title of the plot
plt.legend()  # Displaying legend to differentiate between male and female responses

# Display the bar chart
plt.show()

# End marker