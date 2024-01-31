"""
This program receives a word and makes a dictionary

@author: Tiago Saraiva
@date: 2024-01-26
"""
# Ask user for a word
word = input("Hello user, would you please write a word? ").upper()
# Initialize the dictionary
found = {}

# Iterate over the word catching each letter
for letter in word:
   # Use setdefault method to initialize each item in the dictionary 
   found.setdefault(letter, 0)
   # Insert and count letter in the dictionary
   found[letter] += 1
   
# Display the word in alphabetical order couting how many times it happens
for k, v in sorted(found.items()):
   print(k, 'was found', v, 'time(s).')
