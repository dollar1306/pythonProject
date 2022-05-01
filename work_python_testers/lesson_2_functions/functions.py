
#     #1
# def reverse(str):
#     last = len(str) - 1
#     while last >= 0:
#         print(str[last], end='')
#         last -= 1
# str = "1234abcd"
# reverse(str)


#       #2

# def max_num(num1,num2,num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     elif num3 > num1 and num3 > num2:
#         return num3

# num1 = 4
# num2 = 5
# num3 = 12
# maximum = max_num(num1,num2,num3)
# print(maximum)





        #3
# def sort(nums):
#     new_nums = []
#     for elem in nums:
#         if elem not in new_nums:
#             new_nums.append(elem)
#     return new_nums
#
#
# def sort_set(nums):
#     new_list = set(nums)
#     return new_list
#
# def sort_index(nums):
#     new_list = []
#     for index in range(0, len(nums)):
#         if nums[index] not in new_list:
#             new_list.append(nums[index])
#     return new_list
#
#
# nums = [1,1,2,3,2,3,5,4,6,6,5,2,1,3,5]
# print(sort_index(nums))
# print(sort(nums))
# print(sort_set(nums))



        #4

# def fact(num):
#     count = 1
#     if num == 0:
#         return 1
#     else:
#         while num > 0:
#             count *= num
#             num -= 1
#         return count
#
# num = int(input("Enter number for factorial:" ))
# print(fact(num))