count = 0

# while count < 10:
#     print("The count is: ", count)
#     count += 1


# while count < 10:
#     if count < 5:
#         print("The count is:", count)
#     count += 1

# number = 15
# while number >= 0:
#     count += number
#     number -= 1
# print("The sum from 0 to 5 is:", count)


print("~~ Prime Number ~~")

num = int(input("Enter number: "))

for i in range(2, num):
    if num % i == 0:
        print("The number not prime: ", num)
        break
else:
    print("The number is prime: ", num)
