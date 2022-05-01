from work_python_testers.lesson_3.max_number import find_max
from work_python_testers.lesson_3.min_number import find_min
from work_python_testers.lesson_3.sqrt_number import sqrt_nums
from work_python_testers.lesson_3.sum_module import sum_list

numbers = [100, 2, 3, 75, 88, 95, 159, 951, 65, 0, 12, 158, 999]

count = len(numbers)
print("The maximum number is:", find_max(numbers))

print("The Minimum number in list is: ", find_min(numbers))

print("The summary of list is: ", sum_list(numbers))

print("The avg of list is: ", sum_list(numbers) / count)

print("The sqrt of summary list is: ", sqrt_nums(numbers))
