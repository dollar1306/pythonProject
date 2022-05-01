from work_python_testers.lesson_2_functions.interiance.car import Car


class FamilyCar(Car):
    engine_size = 1600

    def show_famaly_car(self, model):
        self.show_car()
        print("Family car: " + model + " ,Engine Size: ", self.engine_size)
