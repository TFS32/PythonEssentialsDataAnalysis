"""
Book Head First Python, chapter 2, example, page 67

@author: Tiago
@date: Jan 24
"""
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for letter in plist:
   if letter not in "on tap":
       plist.remove(letter)

plist.pop()
plist.pop()
plist.insert(2, plist.pop(3))
plist.insert(4, plist.pop(5))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)