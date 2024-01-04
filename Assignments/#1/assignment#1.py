"""
Python Essentials With Data Analysis - Assignment #1

@author: tiago
@date: 2024-01-03
"""
# Create a list that stores following integers
numbers_list = [5, 0, -10, 4, 9, -5, 13, 26, -17, 18]

# Loop to iterate over each number to get them from the list, and then print
print_list = ""  # Just to print without the brackets
for number in range(len(numbers_list)):
   # If the number is not the last one in index, insert a comma 
   if number != len(numbers_list) - 1:
       print_list += str(numbers_list[number]) + ", "
   else:
       # In the last number there is no need for comma
       print_list += str(numbers_list[number])

print(print_list)

# Calculate the sum and display the result neatly
# Do not use the "sum" function
# Initialize a variable to have the sum of numbers
sum_numbers = 0

# Iterate in each number on the list, and then sum
for number in numbers_list:
   sum_numbers += number
   
print(sum_numbers)
   
# Calculate the average and display the result neatly
# Do this in a way that will work for a list of any lenght
average = sum_numbers / len(numbers_list)
print(average)

# Find the largest number and display the result neatly 
# Do this in a way that will work for any list of integers
# Initialize a variable to have the largest number
largest = numbers_list[0]

# Iterate in each number comparing and discarding in case it is not the largest
for number in numbers_list:
   if number > largest:
       largest = number   

print(largest)