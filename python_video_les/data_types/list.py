cars = ["Toyota", "Mazda", "Subaru"]

cars_empty = []

print(cars)
print(cars_empty)

count = len(cars)
print(count)

cars.append("BMW") #Enter in end of list at bmw
print(cars)

cars.insert(1, "Audi") #Enter audi in index 1
print(cars)


cars.pop()  #out the last item BMW
print(cars)

cars.remove("Subaru")
print(cars)


cars.insert(len(cars), "BMW")
cars.insert(len(cars), "Subaru")
print(cars)

cars.sort()
print(cars)