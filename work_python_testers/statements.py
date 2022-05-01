

#1
# x = 12
#
# y = 12
#
# if(x>y):
#     print("first number is a bigger")
# elif(x<y):
#     print("second number is a bigger")
# elif(x==y):
#     print("The numbers is equal" , x+y)



    #2



# nums = (8,5,9)
# print(nums)
#
# if(nums[0]>nums[1]):
#     print("The first one is biger")
# elif(nums[0]<nums[1]):
#     print("The second one is biger")
# elif(nums[0]==nums[1]):
#     print("both are equal")




    #3

#   #3A
# for num in range(1,10):
#     print(num+1)
#
# count = 0
# while  count <= 10:
#     print(count)
#     count+=1

#   #3B
# for i in range(20, 50,2):
#     print(i)
#   #3C
# for i in range(30, 50):
#     if(i % 2 == 0):
#         print(i)
#
#   #3C
# for y in range(20, 40):
#     if(y % 2 == 1):
#         print(y)



#4
country = ["Austria", "Germany", "Canada", "Peru", "Israel"]
#   #4A
# for cou in country:
#     print(cou)
#
#   #4B
# for cou in country:
#     if(cou == "Israel"):
#         print(cou)
#   #4C
# count = len(country)
# while(count > 0):
#     if(count == 3 ):
#         if(country[count] == "China"):
#             print("Yes")
#         else:print("no")
#     count-=1


#   #4D
# first = len(country[0])
# print(first)



    #5

# age = int(input("What your age?: "))
# if 0 < age <= 6:
#     print("Go to Kindergarten")
# elif 6 < age <= 18:
#     print("Go to School")
# elif 18 < age <= 67:
#     print("Go to Work")
# elif 67 < age <= 120:
#     print("Collecting Pension")



#     #6
#
# prof = input("What your profession? ")
# if prof.lower() == "teacher":
#     print("Salary: 5000")
# elif prof.lower() == "bank teller":
#     print("Salary: 10000")
# elif prof.lower() == "qa":
#     print("Salary: 15000")
# elif prof.lower() == "average":
#     print("Salary: 9100")



#     #7

# names = {1: 'Alex', 2: 'Elena', 3: 'Liza', 4: 'Janna'}
# for key in names.keys():
#     print("ID:", key)
# for name in names.values():
#         print("Name:", name)


#     #8
#
# numbers = {9,15,120,40,55,240}
# for num in numbers:
#     if num % 3 == 0 and num % 5 == 0:
#         print(num)



#     #9
#
# word = ['o', 'l', 'l', 'e', 'H']
# while len(word) > 0:
#     print(word.pop(), end='')


    #10

    #10 A

nums = [15,2,36,20,7]
# if nums[0] > nums[1]:
#     if nums[0]>nums[2]:
#         print(nums[0])
#     else:
#         print(nums[2])
# else:
#     if nums[1]>nums[2]:
#         print(nums[1])
#     else:
#         print(nums[2])

        # 10 B

# max = nums[0]
# for num in nums:
#     if num > max:
#         max = num
# print("The maximu number is: ", max)


    #10 C


# sum = 0
# for num in nums:
#     sum += num
# print("The sum is: ", sum)



    #11

# num = int(input("Enter a number: "))
# prime = True
# for x in range(2, int(num / 2)):
#     if num % x == 0:
#         prime = False
#         break
# if prime:
#     print("The number is prime", num)
# else:
#     print("The number not prime", num)

