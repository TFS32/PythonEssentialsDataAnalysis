"""
This program is an example for module 5 Python Essentials With Data Analysis

@author: Tiago Saraiva
@date: 2024-01-30
"""
class Automobile:
   def __init__(self, model, kms = 0, fuel = 0):
       self.model = model        # make and model of vehicle
       self.kms = kms            # kilometers driven
       self.fuel = fuel          # litres of fuel used

   def __repr__(self):
       a = "***********************************\n"
       b = "The make and model is: " + str(self.model) + '\n'
       c = "Kilometers driven: " + str(self.kms) + '\n'
       d = "Fuel consumed: " + str(self.fuel) + '\n'
       return a + b + c + d + a
          
   def fuel_eff(self):
       """Determines litres per 100km"""
       if self.kms > 0:
           eff = self.fuel/self.kms * 100
       else:
           eff = -1
       return eff
       

def dummy():
   return 'Successful use of dummy function'  