"""
Head First Python Chapter 4 fourth example

@author: Tiago Saraiva
@date: 2024-01-30
"""
def double(arg):
   print('Before: ', arg)
   arg = arg * 2
   print('After: ', arg)
   
def change(arg):
   print('Before: ', arg)
   arg.append('More data')
   print('After: ', arg)  
 