

# תרגיל 2 String
str = "python is a general purpose computer programming language"

print(str.index("computer"))

print(str.count("computer"))

my_list = str.split(" ")
print(my_list)
#print(str.split(" "))
str =str.replace(" ","")
print(str)

print(my_list.index("computer"))
print(str.find("computer"))


# תרגיל 3 String
str = "Hello World"

my = str.split(" ")
print(my)
print(my[len(my) - 1])



# תרגיל 1 list
country = ["Russia", "Usa", "Canada", "Israel", "America", "Brazil"]

print(country[:3])
temp = country[0]
country[0] = country[1]
country[1] = temp
print(country)
country.reverse()
print(country)
country.sort()
print(country)

len_of_list = len(country)

print(len_of_list)

print(country[:len_of_list - 1])

country.pop(len_of_list - 1)
print(country)


print("Hello")
country.remove(last_word)
print(country)