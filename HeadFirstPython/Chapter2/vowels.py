"""
Book Head First Python, chapter 2, example, page 56

@author: tiago
@date: Jan 24
"""
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"

for letter in word:
   if letter in vowels:
       print(letter)

found = []
print(len(found))
found.append('a')
print(len(found))
print(found)
found.append('e')
found.append('i')
found.append('o')
print(len(found))
print(found)

