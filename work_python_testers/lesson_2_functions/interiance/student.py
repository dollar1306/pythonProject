from work_python_testers.lesson_2_functions.interiance.car import Car


class StudentCar(Car):
    engine_size = 1200
    color = "Black"
    def show_student_car(self, model):
        self.show_car()
        print("Student car: " + model + " ,Engine Size: ", self.engine_size)
