# Import the pyplot module from the matplotlib library for graph
import matplotlib.pyplot as plt

# Line 1: From (1, 2) to (6, 8)
x1 = [1, 6]
y1 = [2, 8]

# Line 2: Dotted line from (1, 3) to (2, 8) to (6, 1) to (8, 10)
x2 = [1, 2, 6, 8]
y2 = [3, 8, 1, 10]

# Plotting the lines
plt.plot(x1, y1, label='Line 1')
plt.plot(x2, y2, 'r--', label='Line 2')  # 'r--' specifies a red dashed line

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Graph Exercise')

# Adding legend
plt.legend()

# Display the plot
plt.show()

