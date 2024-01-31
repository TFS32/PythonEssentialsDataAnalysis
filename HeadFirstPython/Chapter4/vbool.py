"""
Head First Python Chapter 4 second example

@author: Tiago Saraiva
@date: 2024-01-30
"""
def search4vowels(word:str) -> set:       # annotations
   """Display any vowels found in a supplied word."""
   vowels = set('aeiou')
   return vowels.intersection(set(word))

print(search4vowels('hitch-hiker'))
print(search4vowels('galaxy'))
print(search4vowels('sky'))
