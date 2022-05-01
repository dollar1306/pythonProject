

country = ["Russia","Israel","Bolgaria","Kazahstan","USA"]
#1
print(country)
print(country[:3])

#2
temp = country[0]
country[0] = country[1]
country[1] = temp
print(country)

#3
country.reverse()
print(country)

#4
country.sort()
print(country)


#5
# last_index = len(country) - 1
# last_country = country[last_index]
# country.reverse()
# print(country[:last_index])
#
# print(country.pop(last_index))
# print(country)
#
# country.remove(last_country)
# print(country)

#6
middle_index =int(len(country)/2)
# print(middle_index)
country.insert(middle_index,"Canada")
print(country)

country.insert(middle_index,"Brazil")
print(country)