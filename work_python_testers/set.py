



country = ["Russia", "Usa", "Canada", "Israel", "America", "Brazil"]


last = country[len(country)-1]

print(country)

country.remove(last)
print(country)


middle = int(len(country)/2)
print(middle)
country[middle] = "Australia"

print(country)