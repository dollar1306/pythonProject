class Mobile:
    def __init__(self, model, os, version, has_flash, price, screen_width, screen_height):
        self.model = model
        self.os = os
        self.version = version
        self.has_flash = has_flash
        self.price = price
        self.screen_width = screen_width
        self.screen_height = screen_height

    def print_param(self):
        print("model: " + self.model +
              "\nos: " + self.os +
              "\nversion: " + str(self.version) +
              "\nhas_flash: " + str(self.has_flash) +
              "\nprice: " + str(self.price) +
              "\nscreen_width: " + str(self.screen_width) +
              "\nscreen_height: " + str(self.screen_height))

    def calc_area(self):
        print("The area of screen is: ",self.screen_width * self.screen_width)
