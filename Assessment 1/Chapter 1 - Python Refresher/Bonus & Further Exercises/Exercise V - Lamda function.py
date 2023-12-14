# Chapter 1 Further Exercise V - Lamda function

# Listing of tuples representing marks for various courses
marks = [("CodeLab I", 67), ("web Development", 75), ("CodeLabII", 74), 
         ("Smartphone Apps", 68), ("Games Development", 70), ("Responsive web", 65)]

# Sorting low to high based on marks using lambda function
low_to_high = sorted(marks, key=lambda x: x[1])

# Sorting high to low based on marks using lambda function
high_to_low = sorted(marks, key=lambda x: x[1], reverse=True)

# Displaying the results
print("Low to High:", low_to_high)
print("High to Low:", high_to_low)

# End marker