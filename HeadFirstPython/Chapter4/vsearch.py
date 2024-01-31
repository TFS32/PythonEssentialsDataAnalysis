"""
Head First Python Chapter 4 first example

@author: Tiago Saraiva
@date: 2024-01-30
"""
def search4vowels(word):
   """Display any vowels found in a supplied word."""
   vowels = set('aeiou')
   # word = input("Provide a word to search for vowels: ")
   found = vowels.intersection(set(word))
   for vowel in found:
       print(vowel)

search4vowels('hitch-hiker')
search4vowels('galaxy')
