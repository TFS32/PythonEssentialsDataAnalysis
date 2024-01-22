"""
This program is a palindrome checker

@author: Tiago Saraiva
@date: 2024-01-19
"""
# The animals dictionary
animals = {'dog': 0, 
           'cat': 1,
           'frog': 2}

# Initializing the lists
labels = []
encoded_labels = []

# This loop guarantees that the input will happen 5 times
for i in range(5):
    while True: # While the input is correct the code goes on, otherwise, it loops again
       user_input = input("User, choose an animal: dog, cat or frog? ")
       # If the user input is correct, the while loop stops
       if user_input in animals:
           break
       # If not, the user will have to write again
       else:
           print("The input accepted is dog, cat or frog.")
    # With the user input the labels list is populated, adding with append method
    labels.append(user_input)

# This loop goes over each animal given in the user input and then
# Append the values in the dictionary to the encoded_labels list     
for animal in labels:
   encoded_labels.append(animals[animal])

# Display the results   
print(labels)
print(encoded_labels)