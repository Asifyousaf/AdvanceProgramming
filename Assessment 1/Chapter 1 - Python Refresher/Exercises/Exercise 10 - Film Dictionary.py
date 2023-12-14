# Chapter 1 Exercise 10 - Film Directory

# Creating a dictionary for a film
film_detail = {
    "Title": "Inception",
    "Director": "Christopher Nolan",
    "Year": 2010,
    "Genre": "Science Fiction",
    "Rating": 8.8
}

# Display film details using a loop
print("Film Details:")

# Using items() to directly access key-value pairs in the loop
for key, value in film_detail.items():
    print(f"{key}: {value}")

# End marker