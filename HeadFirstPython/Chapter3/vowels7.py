"""
Book Head First Python, chapter 3, example, page 124

@author: Tiago Saraiva
@date: Jan 24
"""
vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")
found = ()

found = vowels.intersection(set(word))
for vowel in found:
   print(vowel)
