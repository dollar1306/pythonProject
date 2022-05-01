nums_list = [1, 2, 3, 3]

nums_set = {1, 2, 3, 3}

print(nums_list) #if we have duplicate value in list, we can see them in print
print(nums_set) #if we have duplicate value in set, we not see them in print

cars = {"Toyota", "Mazda", "BMW"}
print(len(cars))
print(cars)
cars.remove("BMW")
print(cars)

cars.clear() # clear all set
print(cars)

cars = {"Toyota", "Mazda", "BMW", "Audi"}
print(cars)

cars_new = {"Mitsubishi", "Audi"}
print(cars_new)

cars_all = cars.union(cars_new)
print(cars_all)

print(cars.difference(cars_new))

