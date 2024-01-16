"""
This are class examples ADVANCED DATA TYPES

@author: tiago
@date: Jan 24
"""
# STRINGS
# Add strings
my_string = "This sentence" + "is broken into" + "three parts!"
my_other_string = "My grammer is terrible."
my_final_string = my_string + my_other_string

# Converting
my_string = str(10)
my_string = str(True)
my_string = str([1, 2, 3, 4])

# Useful methods to format strings
my_string = " Python, is a great language. "
my_string.lower() # -> "python, is a great language."
my_string.upper() # -> "PYTHON, IS A GREAT LANGUAGE."
my_string.lstrip() # -> "Python, is a great language. "
my_string.rstrip() # -> " Python, is a great language."
my_string.strip() # -> "Python, is a great language."

my_string = "Violet is a colour in the rainbow."
my_string.find("colour") # -> 12
"rainbow" in my_string # -> True
"blue" not in my_string # -> True
my_string.startswith("Vio") # -> True
my_string.endswith(".") # -> True

my_string = "Python is an object oriented, interpreted language."
my_string.split(",") # -> ['Python is an object oriented', 'interpreted language.']
list(my_string) # -> ['P', 'y', 't', 'h', 'o', 'n', ' ', ...]
my_string.replace(",", "~") # -> "Python is an object oriented~ interpreted language."
my_string[7:] # -> "is an object oriented, interpreted language."
my_string[:6] # -> "Python"
my_string[-9:] # -> "language."

# LISTS
# Accessing
mylist = ['apples', 'oranges', 'pears']
mylist [1] # -> 'oranges'

# Changing
mylist [1] = 'bananas' # -> -> ['apples', 'bananas', 'pears']

# Adding items
mylist = [1, 2, 3]
mylist.append(4) # -> [1, 2, 3, 4]
mylist + [4, 5, 6] # -> [1, 2, 3, 4, 5, 6]
mylist.insert(0, 9) # -> [9, 1, 2, 3]

# Removing items
mylist = ['red', 'black', 'yellow']
# mylist.remove('black') # -> ['red', 'yellow]
del mylist[:1] # -> ['black', 'yellow']
mylist.clear() # -> []

# Slices
mylist = [1, 2, 3, 4, 5]
# mylist[start:stop:step]
mylist[1:3] # -> [2, 3]
mylist[:2] # -> [1, 2]
mylist[-1:] # -> [5]
mylist[::2] # -> [1, 3, 5]

# Membership
mylist = ['apple', 'orange', 'banana']
'apple' in mylist # -> True
"pinneapple" not in mylist # -> True
mylist.index('orange') # -> 1

# Lenght
len(mylist)

# Sorting
myslist = [5, 1, 2, 4, 3]
mylist.sort() # -> [1, 2, 3, 4, 5]
sorted(mylist) # -> [1, 2, 3, 4, 5]

# TUPLES
mytuple = (1, 2, 3, 4, 5)
mytuple[2] # -> 3

# To create a tuple
mytuple = (99,)

# Adding or removing
my_1st_tuple = (1, 2, 3, 4, 5)
my_2nd_tuple = (6, 7, 8, 9, 10)
my_3rd_tuple = my_1st_tuple + my_2nd_tuple # -> (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Another way to create
mytuple = (1, 2, 3, 4, 5)
mytuple = mytuple + (999, )
mytuple # -> (1, 2, 3, 4, 5, 999)

# Convert a list to a tuple
mylist = [1, 2, 3, 4, 5]
mytuple = tuple(mylist)
mytuple = (1, 2, 3, 4, 5)

# Slices
mytuple = (1, 2, 3, 4, 5)
# mytuple[start:stop:step]
mytuple[1:3] # -> (2, 3)
mytuple[:2] # -> (1, 2)
mytuple[1:] # -> (5)
mytuple[::2] # -> (1, 3, 5)

# Check if an item is in the tuple
mytuple = ('apple', 'orange', 'banana')
'apple' in mytuple # -> True
"pineapple" not in mytuple # -> True

# Find the index
mytuple.index('orange') # -> 1

# DICTIONARIES
my_fruit_dictionary = { 'apples': 52, 'oranges': 105, 'bananas': 9}
my_num_dictionary = {1: 2, 2: 3, 3: 4}
my_fancy_dictionary = {'fruit': ['apples', 'oranges', 'bananas'], 
                       'bread': ("rye", "marble")
                      }
my_empty_dictionary = {}

# How to write a dictionary
mydictionary = {'Gru': 1001,
                'Agnes': 3389,
                'Kevin': 1276,
                'Nefario': 1000}

# Accessing
mydictionary = {'Gru': 1001, 'Agnes': 3389, 'Kevin': 1276, 'Nefario': 1900}
mydictionary['Agnes'] # -> 3389

# Adding
mydictionary = {'Gru': 1001, 'Agnes': 3389, 'Kevin': 1276, 'Nefario': 1900}
mydictionary['Margo'] = 5647 
# mydictionary
# -> {'Gru':
#    'Agnes': 3389,
#    'Kevin': 1276,
#    'Nefario': 1900,
#    'Margo': 5647}

# Initialize
mydictionary = {}

# Modifying
mydictionary = {'Gru': 1001, 'Agnes': 3389,' Kevin': 1276, 'Nefario': 1900}
mydictionary[' Kevin'] = 9999
# mydictionary
# -> {'Gru':
#    'Agnes': 3389,
#    'Kevin': 9999,
#    'Nefario': 1900}

# Sorting
mydictionary = {'Gru': 1001, 'Agnes': 3389, 'Kevin': 1276, 'Nefario': 1900}
sorted(mydictionary) # -> ['Agnes', 'Gru', 'Kevin', 'Nefario']
sorted(mydictionary.items())
# -> [('Agnes': 3389), ('Gru': 1001), ('Kevin': 1276), ('Nefario':1900)]

# Delete
mydictionary = {'Gru': 1001, 'Agnes': 3389, 'Kevin': 1276, 'Nefario': 1900}
del mydictionary['Agnes']
# mydictionary = {'Gru': 1001, 'Kevin': 1276, 'Nefario': 1900}

# SETS
myset1 = {1, 2, 3, 4, 5}
myset2 = {4, 5, 6, 7, 8, 9, 10}

# Intersection
myset1.intersection(myset2) # -> {4,5}

# Difference
myset1.difference(myset2) # -> {1, 2, 3}
myset2.difference(myset1) # -> {6, 7, 8, 9, 10}

# Union
myset1.union(myset2) # -> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Convert to a set
mygroceries = ['apples', 'oranges', 'bananas', 'apples', 'bananas']
set(mygroceries) # -> {'apples', 'oranges', 'bananas'}

# Then convert it back to a list
list(set(mygroceries)) # -> ['apples', 'oranges', 'bananas']











