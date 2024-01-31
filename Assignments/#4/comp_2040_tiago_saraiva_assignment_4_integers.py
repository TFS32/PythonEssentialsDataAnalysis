"""
This program gives a list of sorted integers after user's input 

@author: Tiago Saraiva
@date: 2024-01-26
"""
# Initializng the list
user_integers = []

# Ask the user to input an integer 5 times
for i in range(5):
   while True:
       user_input = input("User, provide this program an integer: ")
       # Only accept input if they are integers
       try:
           user_input = int(user_input)
           break
       except ValueError:
           print("User, please, just integers are accepted.")
   # Add the user input to a list
   user_integers.append(user_input)

# Use copy method to copy the list to another list
integers = user_integers.copy()

# Bubble-sort algorithm to sort the items
# Iterate over each element of the array, counting based in length of list
for i in range(len(integers)):
   # Boolean set to false to verify if list is sorted
   swapped = False
   # Start in the first index, end in the last index, after each pass
   # largest element will be placed in the correct position
   for j in range(0, len(integers) - 1):
       # From the list swaps element if found is greater
       # Check if the current element is greater than next element
       if integers[j] > integers[j + 1]:
           # if true, change place of item
           integers[j], integers[j + 1] = integers[j + 1], integers[j]
           # When items are placed correctly set the boolean variable to True
           swapped = True
   if (swapped == False):
       break   # Breaks the code when it is sorted, to optimize code

# Display both lists
print("\nUser input list: ", user_integers)
print("\nSorted list: ", integers)
