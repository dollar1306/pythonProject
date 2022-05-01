from work_python_testers.lesson_2_functions.interiance.car import Car
from work_python_testers.lesson_2_functions.interiance.family import FamilyCar
from work_python_testers.lesson_2_functions.interiance.student import StudentCar

car1 = Car()
car1.show_car()
Car.number_of_wheels = 6
car1.show_car()

car2 = FamilyCar()
car2.show_car()
car2.show_famaly_car("Toyota")

car3 = StudentCar()
car3.show_car()
car3.show_student_car("BMW")
print(car3.color)
