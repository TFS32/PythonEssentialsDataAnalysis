"""
This program is the class examples of module 6

@author: Tiago Saraiva
@date: 2024-02-05
"""
a = "************************************************************************"

myfile = open('test.txt', 'r')
print(myfile.read())
print(type(myfile))
myfile.close()

print(a)

with open('test.txt', 'r') as myfile:
    print(myfile.read())

print(a)

import csv
with open('data.csv') as mydata:
    for line in csv.reader(mydata):
      print(line)    

print(a)    

with open('data.csv') as mydata:
   for line in csv.DictReader(mydata):
       print(line)
       
print(a)

with open('data.csv') as mydata:
   for line in csv.DictReader(mydata):
       for k, v in line.items():
           print(k, v)

print(a)

with open('data2.csv') as mydata:
    for line in csv.reader(mydata):
      print(line)

print(a)

with open('data2.csv', 'w') as mydata:
    mywriter = csv.writer(mydata)
    mywriter.writerow(['item1', 'item2', 'item3'])

       