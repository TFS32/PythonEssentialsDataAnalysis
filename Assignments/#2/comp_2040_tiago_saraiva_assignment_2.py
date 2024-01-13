from datetime import datetime
import time
import math
"""
This program is assignment #2 from Python Essentials With Data Analysis

@author: Tiago Saraiva
@date: 2024-01-12
"""
# Use a loop to repeat the action 5 times
for i in range(5):
   # From datetime takes the actual minute 
   minute_now = datetime.today().minute
   # Verify if the minute is odd
   is_minute_odd = minute_now % 2 != 0 
   
   # Check if the minute is odd or not
   if is_minute_odd:
       print("This is an odd minute.")
   else:
       print("Minute ain't odd.")
   # Wait time to loop each 60 seconds    
   wait_time = time.sleep(60)

print("----------------------------------------------------------------------")

# String that contais 26 letters of alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
# Get the total number of letters in the string
lenght = len(alphabet)

# Loop over each item in a range from last item to first, decreasing
# The range starts at last index, 25, stops at the first index, 0,
# Stepping, -2, so it jumps 1 index each time it decreases
for i in range(lenght-1, 0, -2):
   print(alphabet[i])

print("----------------------------------------------------------------------")

# Copy and paste the list from the assignment
pop = [73.79693173, 41.76429734, 53.66368384, 24.60911367,
       73.60414637, 62.26858213, 13.9670495, 70.97809816, 
       17.9978692, 56.10505197
]

# Calculate the population mean
pop_mean = sum(pop) / len(pop)
# For each item in the list calculate the squared difference
squared_differences = [(i - pop_mean) ** 2 for i in pop]
# Variance is the sum of each item divided by the list pop size
variance = sum(squared_differences) / len(pop)
# Standard Deviation is the square root of the variance
standard_deviation = math.sqrt(variance)

# Display the result   
print(f'The population variance of the list pop is: {variance}\n'
     f'and the population standard deviation is: {standard_deviation}.')
