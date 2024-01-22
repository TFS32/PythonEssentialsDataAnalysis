"""
This program is a palindrome checker

@author: Tiago Saraiva
@date: 2024-01-19
"""
# Creates a function that checks if the word is a palindrome or not
def palindrome(word):
   # Checking if the words are equal even if backwards
   # Using lower method so there are no erros if the input contains uppercase
   if word.lower() == word[::-1].lower():
       print(f"Yes, {word} and {word[::-1]} are equals, this is a palindrome!")
   else:    
       print(f"{word} and {word[::-1]} aren't same, this isn't a palindrome.")

# Asking the user to input a word       
word = input("Please say a word and we will check if it is a palindrome: ")
palindrome(word) # Calling the function to check if the word is a palindrome
