import auto

car1 = auto.Automobile("Honda Civic", 100, 10)
car2 = auto.Automobile("Ford F150")

print(car1)
print(car2)

print("car1 has a fuel efficiency of", car1.fuel_eff())
print("car2 has a fuel efficiency of", car2.fuel_eff())

print(auto.dummy())