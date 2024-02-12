# -*- coding: utf-8 -*-
"""
This program is codes in the PDF variable scope module 5

@author: Tiago Saraiva
@date: 2024-02-05
"""
a = "\n********************************************************************\n"
print(a)

x = 10


def increase_x(x):
   x += 5
   return x


print(x)
print(increase_x(x))
print(x)

print(a)

y = 10


def increase_y(y):
   y += 5
   return y


print(y)
print(increase_y(y))
print(y)

print(a)

class Employee():
   """This class contains employee data."""
   def __init__(self, id, name, income):
    self.name = name
    self.id = id
    self.income = income
    
   def income_taxes(self):
       """This function calculates taxes based on income."""
       rate = 0.20
       return rate * self.income

employee1 = Employee(1, 'Max', 20000)
print(employee1.income_taxes())

print(a)

class Color():
   YELLOW = 1
   RED = 2
   BLUE = 3
   

















