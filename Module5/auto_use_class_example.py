import auto_class_example as ace
"""
This program is an example for module 5 Python Essentials With Data Analysis

@author: Tiago Saraiva
@date: 2024-01-30
"""
car1 = ace.Automobile("Honda Civic", 100, 10)
car2 = ace.Automobile("Ford F150")              # ("Ford F150, 100, 2000")

print(car1)
print(car2)

print("car1 has a fuel efficiency of", car1.fuel_eff())
print("car2 has a fuel efficiency of", car2.fuel_eff())

print(ace.dummy())          # Not Jupyter Nootebook

