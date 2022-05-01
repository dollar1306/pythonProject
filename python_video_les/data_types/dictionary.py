countries = {1: "Russia", 2: "Canada", 3: "China", 4: "USA"}
print(countries.values())
print(countries.keys())

salary = {"Admin": 8000, "IT": 10000, "Support": 6000, "QA": 14000, "Automation": 18000}
print(salary)
print(salary.values())
print(salary.keys())
print(salary["QA"])
print(salary["Admin"])
print(salary.get("Automation"))




print("~~~ List inside dictionary ~~~")
salary_with_list = {"Support": 6000, "QA": [14000, 10000, 12000, 18000], "Automation": [15000, 17000, 25000]}

print("That a salary of Qa team in our company: ", salary_with_list["QA"])
print("That a salary of automation-qa team in our company: ", salary_with_list["Automation"])
print(salary_with_list["QA"][3])
print(salary_with_list["Automation"][0])
print(salary_with_list["QA"].index(12000))


print(("~~~ dictionary inside dictionary ~~~" ))

emp = {"Ceo": "Ori", "VPRND": "David", "RND":{"QA": "Yoni", "Dev": "Chaim"}, "DBA": "Shlomo"}
print(emp.get("RND").get("QA"))
print(emp.get("RND").values())

print("~~~ Add Element to Dictionary ~~~")
print(emp)
emp["Team Leader"] = "Alex"
print(emp)


print("~~~ Update Element in Dictionary ~~~")
print(emp)
emp["Ceo"]= "Uri"
print(emp)

del emp["VPRND"]
print(emp)

