"""
Book Head First Python, chapter 3, example, page 121

@author: Tiago Saraiva
@date: Jan 24
"""
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}

for letter in word:
   if letter in vowels:
       found.setdefault(letter, 0)
       found[letter] += 1

for k, v in sorted(found.items()):
   print(k, 'was found', v, 'time(s).')            
