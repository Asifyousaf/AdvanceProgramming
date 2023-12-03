marks = [("CodeLab I", 67), ("web Development", 75), ("CodeLabII", 74), ("Smartphone Apps", 68), ("Games Development", 70), ("Responsive web", 65)]

# Sorting without specifying a key (default behavior)
sorted_result = sorted(marks, key=lambda x: x)

print("Sorted without specifying a key:", sorted_result)
