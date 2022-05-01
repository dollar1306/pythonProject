from work_python_testers.lesson_2_functions.mobileDevice.mobile_device import Mobile


# model, os, version, has_flash, price, screen_width, screen_height
mob1 = Mobile("Apple", "IOS", 15.5, True, 5500, 9.9, 12)
mob1.print_param()
mob1.calc_area()

print("```````````````````````````````````")
mob2 = Mobile("Samsung", "Android", 9.5, False, 1200, 8.5, 10)
mob2.print_param()
mob2.calc_area()


