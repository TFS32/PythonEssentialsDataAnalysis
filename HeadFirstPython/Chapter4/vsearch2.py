"""
Head First Python Chapter 4 third example

@author: Tiago Saraiva
@date: 2024-01-30
"""


def search4vowels(phrase: str) -> set:
    """Display any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


print(search4vowels('hitch-hiker'))
print(search4vowels('galaxy'))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


print(search4letters('El magico de Oz', 'xyz'))
print(search4letters('life, the universe, and everything'))

print((search4letters('life, the universe, and everything'))
      == (search4vowels('life, the universe, and everything')))

print(search4letters(letters='xyz', phrase='El magico de Oz'))
